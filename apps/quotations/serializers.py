from rest_framework import serializers
from .models import QuotationRequest

class QuotationRequestSerializer(serializers.ModelSerializer):
    product = serializers.ListField(
        child=serializers.CharField(), required=True
    )
    quantity = serializers.ListField(
        child=serializers.IntegerField(), required=True
    )

    class Meta:
        model = QuotationRequest
        fields = '__all__'

    def to_internal_value(self, data):
        """
        Convert single product/quantity to list if needed.
        """
        if 'product' in data and not isinstance(data['product'], list):
            data['product'] = [data['product']]
        if 'quantity' in data and not isinstance(data['quantity'], list):
            data['quantity'] = [data['quantity']]
        return super().to_internal_value(data)
