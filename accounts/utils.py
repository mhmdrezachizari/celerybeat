import random

def generate_otp():
    return str(random.randint(100000, 999999))

def send_otp(phone_number, otp):
    print(f"ارسال OTP {otp} به شماره {phone_number}")
