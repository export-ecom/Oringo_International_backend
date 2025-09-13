from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import QuotationRequestSerializer
from .tasks import handle_quotation_request   # import celery task

class QuotationRequestView(APIView):
    def post(self, request):
        serializer = QuotationRequestSerializer(data=request.data)
        if serializer.is_valid():
            # Convert validated_data to a plain dict before sending to Celery
            clean_data = dict(serializer.validated_data)
            print("Data sent to Celery:", clean_data)  # Debugging

            handle_quotation_request.delay(clean_data)

            return Response(
                {"message": "Quotation request received. You will get a confirmation email shortly."},
                status=status.HTTP_202_ACCEPTED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
