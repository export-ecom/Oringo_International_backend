# apps/orders/tasks.py
from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_order_confirmation(email, order_id):
    send_mail(
        subject="Order Confirmation",
        message=f"Your order #{order_id} has been placed.",
        from_email="no-reply@example.com",
        recipient_list=[email],
        fail_silently=True,
    )
