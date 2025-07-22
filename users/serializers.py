from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = CustomUser
        fields = ['id', 'name', 'email', 'dob', 'password', 'createdAt', 'modifiedAt']
        read_only_fields = ['id', 'createdAt', 'modifiedAt']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            dob=validated_data['dob'],
            password=validated_data['password']
        )
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(email=data['email'], password=data['password'])
        if user and user.is_active:
            refresh = RefreshToken.for_user(user)
            return {
                'access': str(refresh.access_token),
                'refresh': str(refresh),
                'user': {
                    'id': str(user.id),
                    'name': user.name,
                    'email': user.email
                }
            }
        raise serializers.ValidationError("Invalid credentials")


class ParagraphInputSerializer(serializers.Serializer):
    text = serializers.CharField()

    def validate_text(self, value):
        if not value.strip():
            raise serializers.ValidationError("Text cannot be empty.")
        return value


class WordSearchSerializer(serializers.Serializer):
    word = serializers.CharField()

    def validate_word(self, value):
        return value.lower().strip()