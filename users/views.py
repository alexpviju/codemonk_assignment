from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import RegisterSerializer, LoginSerializer,ParagraphInputSerializer
from rest_framework.views import APIView
from .models import Paragraph,WordIndex
from rest_framework.permissions import IsAuthenticated

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class ParagraphUploadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ParagraphInputSerializer(data=request.data)
        if serializer.is_valid():
            full_text = serializer.validated_data['text']
            paragraphs = [p.strip() for p in full_text.split("\n\n") if p.strip()]

            created_paragraphs = []

            for para_text in paragraphs:
                paragraph = Paragraph.objects.create(text=para_text)
                created_paragraphs.append(paragraph)

                # Tokenize, clean, lowercase
                words = para_text.lower().split()
                for word in words:
                    WordIndex.objects.create(word=word, paragraph=paragraph)

            return Response({
                "message": f"{len(created_paragraphs)} paragraphs indexed successfully."
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)