from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, PhoneOTP
from .serializers import PhoneSerializer, OTPVerifySerializer, PasswordSetSerializer
from .utils import generate_otp, send_otp
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializers import LoginSerializer


class SendOTPView(APIView):
    def post(self, request):
        serializer = PhoneSerializer(data=request.data)
        if serializer.is_valid():
            phone = serializer.validated_data["phone_number"]
            otp = generate_otp()
            PhoneOTP.objects.update_or_create(
                phone_number=phone, defaults={"otp": otp, "is_verified": False}
            )
            send_otp(phone, otp)
            return Response({"message": "کد ارسال شد"})
        return Response(serializer.errors, status=400)


class VerifyOTPView(APIView):
    def post(self, request):
        serializer = OTPVerifySerializer(data=request.data)
        if serializer.is_valid():
            phone = serializer.validated_data["phone_number"]
            otp_input = serializer.validated_data["otp"]
            print(request.data)
            try:
                otp_obj = PhoneOTP.objects.get(phone_number=phone)
                if otp_obj.is_expired():
                    return Response({"error": "کد منقضی شده"}, status=400)
                if otp_obj.otp != otp_input:
                    return Response({"error": "کد اشتباه است"}, status=400)
                otp_obj.is_verified = True
                otp_obj.save()
                return Response({"message": "کد تأیید شد"}, status=200)
            except PhoneOTP.DoesNotExist:
                return Response({"error": "کدی برای این شماره ثبت نشده"}, status=404)
        return Response(serializer.errors, status=400)


class SetPasswordView(APIView):
    def post(self, request):
        serializer = PasswordSetSerializer(data=request.data)
        if serializer.is_valid():
            phone = serializer.validated_data["phone_number"]
            password = serializer.validated_data["password"]
            try:
                otp_obj = PhoneOTP.objects.get(phone_number=phone)
                if not otp_obj.is_verified:
                    return Response({"error": "شماره تأیید نشده"}, status=403)
                user, _ = User.objects.get_or_create(phone_number=phone)
                user.set_password(password)
                user.save()
                otp_obj.delete()

                # توکن بساز
                token, _ = Token.objects.get_or_create(user=user)
                return Response({"message": "رمز تنظیم شد", "token": token.key})
            except PhoneOTP.DoesNotExist:
                return Response({"error": "کد تأیید پیدا نشد"}, status=404)
        return Response(serializer.errors, status=400)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            phone = serializer.validated_data["phone_number"]
            password = serializer.validated_data["password"]

            user = authenticate(request, phone_number=phone, password=password)
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                return Response(
                    {"message": "ورود موفقیت‌آمیز بود", "token": token.key},
                    status=status.HTTP_200_OK,
                )
            return Response(
                {"error": "شماره یا رمز نادرست است"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
