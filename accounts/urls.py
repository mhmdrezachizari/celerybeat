from django.urls import path
from .views import SendOTPView, VerifyOTPView, SetPasswordView ,LoginView

urlpatterns = [
    path('send-otp/', SendOTPView.as_view()),
    path('verify-otp/', VerifyOTPView.as_view()),
    path('set-password/', SetPasswordView.as_view()),
    path('login/', LoginView.as_view(), name='login'),
]
