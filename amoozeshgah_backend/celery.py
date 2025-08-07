import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "amoozeshgah_backend.settings")

app = Celery("amoozeshgah_backend")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    from students.tasks import check_receipts_and_update_paid  # ایمپورت داخل تابع

    # هر ۳۰ ثانیه یک بار اجرا می‌شود
    sender.add_periodic_task(30.0, check_receipts_and_update_paid.s(), name='Run every 30 seconds')
