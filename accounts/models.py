from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
import datetime

class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None):
        if not phone_number:
            raise ValueError("Phone number is required")
        user = self.model(phone_number=phone_number)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone_number, password):
        user = self.create_user(phone_number, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=20, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.phone_number

class PhoneOTP(models.Model):
    phone_number = models.CharField(max_length=20, unique=True)
    otp = models.CharField(max_length=6)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        return timezone.now() > self.created_at + datetime.timedelta(minutes=5)
