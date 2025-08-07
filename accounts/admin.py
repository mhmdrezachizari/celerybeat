from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User , PhoneOTP

admin.site.register(PhoneOTP)

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        "id",
        "phone_number",
        "is_active",
        "is_staff",
        "is_superuser",
    )
    search_fields = ("phone_number",)
    list_filter = (
        "is_active",
        "is_staff",
        "is_superuser",
    )
    ordering = ("id",)

    fieldsets = (
        (None, {"fields": ("phone_number", "password")}),
        ("اطلاعات شخصی", {"fields": ()}),
        (
            "دسترسی‌ها",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("تاریخچه", {"fields": ("last_login",)}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "phone_number",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )
