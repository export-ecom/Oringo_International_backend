# apps/inquiries/tasks.py
from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_inquiry_received(email, subject):
    send_mail(
        subject="We received your inquiry",
        message=f"Subject: {subject}\nOur team will get back soon.",
        from_email="no-reply@example.com",
        recipient_list=[email],
        fail_silently=True,
    )
