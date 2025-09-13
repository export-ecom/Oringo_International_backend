from django.urls import path
from .views import QuotationRequestView

urlpatterns = [
    path('submit/', QuotationRequestView.as_view(), name='submit-quotation'),
]
