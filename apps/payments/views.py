from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.conf import settings
import razorpay
from apps.orders.models import Order


class CreateRazorpayOrderView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        try:
            order_id = request.data.get("order_id")
            total_amount = request.data.get("total_amount")
            if not order_id or not total_amount:
                return Response({"error": "Missing order_id or total_amount"}, status=status.HTTP_400_BAD_REQUEST)

            
            client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

            # Razorpay amount in paise
            amount_paise = int(float(total_amount) * 100)

            razorpay_order = client.order.create({
                "amount": amount_paise,
                "currency": "INR",
                "payment_capture": 1,
            })

            return Response({
                "order_id": razorpay_order["id"],
                "amount": razorpay_order["amount"],
                "currency": razorpay_order["currency"],
                "key": settings.RAZORPAY_KEY_ID
            })
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class VerifyRazorpayPaymentView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        try:
            # Payload from frontend Razorpay handler
            razorpay_payment_id = request.data.get("razorpay_payment_id")
            razorpay_order_id = request.data.get("razorpay_order_id")
            razorpay_signature = request.data.get("razorpay_signature")

            if not razorpay_payment_id or not razorpay_order_id or not razorpay_signature:
                return Response({"error": "Missing payment data"}, status=status.HTTP_400_BAD_REQUEST)

            # Verify signature
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': razorpay_payment_id,
                'razorpay_signature': razorpay_signature
            }
            client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
            client.utility.verify_payment_signature(params_dict)


            # Mark order as paid (prepaid)
            order = Order.objects.get(id=request.data.get("order_id"))
            order.status = "Confirmed"
            order.save()

            return Response({"success": True, "message": "Payment verified and order updated"})
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
