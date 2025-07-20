from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone
import uuid

class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, dob, password=None):
        if not email:
            raise ValueError("Email is required")
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            dob=dob
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, dob, password):
        user = self.create_user(email, name, dob, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

#user Model
class CustomUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    dob = models.DateField()
    createdAt = models.DateTimeField(default=timezone.now)
    modifiedAt = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'dob']

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Paragraph(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Paragraph {self.id}"


class WordIndex(models.Model):
    word = models.CharField(max_length=100, db_index=True)
    paragraph = models.ForeignKey(Paragraph, on_delete=models.CASCADE, related_name='words')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.word} -> Paragraph {self.paragraph.id}"
