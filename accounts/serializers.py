from rest_framework import serializers
from .models import User

class PhoneSerializer(serializers.Serializer):
    phone_number = serializers.CharField()

class OTPVerifySerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    otp = serializers.CharField()

class PasswordSetSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    password = serializers.CharField()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'phone_number']

class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=11)
    password = serializers.CharField(write_only=True)