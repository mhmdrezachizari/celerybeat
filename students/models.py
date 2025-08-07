from django.db import models
from django.conf import settings

from course.models import Course


# Create your models here.
class Student(models.Model):
    student = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)


class Enrollment(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="enrollments"
    )
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="enrollments"
    )
    # image = models.ImageField()
    is_paid = models.BooleanField(default=False)
    registered_at = models.DateTimeField(auto_now_add=True)
    receipt_image = models.ImageField(upload_to="payment_receipts/")

    class Meta:
        unique_together = ("student", "course")
