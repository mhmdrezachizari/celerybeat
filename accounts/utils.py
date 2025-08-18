"""Utility helpers for account authentication."""

import secrets
import string


def generate_otp(length: int = 6) -> str:
    """Return a cryptographically secure numeric one-time password.

    Args:
        length: Number of digits in the generated OTP.

    Returns:
        str: A string containing ``length`` numeric digits.
    """

    return "".join(secrets.choice(string.digits) for _ in range(length))

def send_otp(phone_number: str, otp: str) -> None:
    """Placeholder to integrate with an SMS provider."""
    print(f"ارسال OTP {otp} به شماره {phone_number}")
