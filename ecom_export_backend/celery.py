# backend_project/celery.py
import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "celery -A ecom_export_backend worker -l info.settings")
app = Celery("celery -A ecom_export_backend worker -l info")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
