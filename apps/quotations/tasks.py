from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from .models import QuotationRequest

@shared_task
def handle_quotation_request(data):
    data = dict(data)
    
    # Ensure product and quantity are lists
    if not isinstance(data.get('product'), list):
        data['product'] = [data.get('product')]
    if not isinstance(data.get('quantity'), list):
        data['quantity'] = [data.get('quantity')]

    # Save to DB
    quotation = QuotationRequest.objects.create(**data)

    # Prepare email
    subject = "Quotation Request Received"
    from_email = "appname<yourmail@example.com>" # replace with your email
    to = [quotation.email]

    # Build product list HTML
    product_list_html = "<ul>"
    for prod, qty in zip(quotation.product, quotation.quantity):
        product_list_html += f"<li>{prod}: {qty}</li>"
    product_list_html += "</ul>"

    # Plain text version
    text_content = f"Hello {quotation.name},\n\nWe received your quotation request successfully!\nProducts:\n"
    for prod, qty in zip(quotation.product, quotation.quantity):
        text_content += f"- {prod}: {qty}\n"

    # HTML version
    html_content = f"""
    <p>Hello <strong>{quotation.name}</strong>,</p>
    <p>We received your quotation request successfully!</p>
    <p><strong>Products Requested:</strong></p>
    {product_list_html}
    <p>Thank you for using our service!</p>
    """

    # Send email
    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()

    return f"Quotation saved and email sent to {quotation.email}"
