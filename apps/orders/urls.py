from django.urls import path
from .views import PlaceOrderView, MyOrdersView

urlpatterns = [
    path("place-order/", PlaceOrderView.as_view(), name="place-order"),
    path("my-orders/", MyOrdersView.as_view(), name="my-orders"),
]
