from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import OrderCreateSerializer, OrderSerializer
import urllib.parse
from .models import Order

class PlaceOrderView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        try:
            serializer = OrderCreateSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            order = serializer.save()

            # WhatsApp notification for COD
            if order.payment_method.lower() == "cod":
                admin_number = "917995950354"
                items_text = "\n".join(
                    [f"{i.quantity} x {i.product.name} @ ₹{i.price}" for i in order.items.all()]
                )
                message = f"""
🛒 *New COD Order*

👤 Customer: {order.full_name}
📧 Email: {order.email}
📱 Phone: {order.phone}
🏠 Address: {order.address}, {order.city}, {order.state}, {order.pincode}
💳 Payment Method: {order.payment_method}

📦 Items:
{items_text}

💰 Total: ₹{order.total_amount}
"""
                wa_link = f"https://wa.me/{admin_number}?text={urllib.parse.quote(message)}"
                # Optional: for testing
                # import webbrowser
                # webbrowser.open(wa_link)

            return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)

        except Exception as e:
            print("Order creation error:", str(e))
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class MyOrdersView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        orders = Order.objects.filter(user=request.user).order_by("-created_at")
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
