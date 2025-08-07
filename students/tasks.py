from celery import shared_task
from .models import Enrollment

@shared_task
def check_receipts_and_update_paid():
    enrollments = Enrollment.objects.filter(is_paid=False, receipt_image__isnull=False)
    for enrollment in enrollments:
        enrollment.is_paid = True
        enrollment.save()
    return f"{enrollments.count()} enrollments updated."
