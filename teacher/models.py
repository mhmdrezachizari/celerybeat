# teacher/models.py
from django.db import models
from django.conf import settings


class Teacher(models.Model):
    name_last = models.CharField(max_length=100)
    name_first = models.CharField(max_length=100)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='teacher_profile'
    )
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='teachers/', blank=True, null=True)

    def __str__(self):
        return self.user.phone_number
