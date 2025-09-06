from rest_framework import serializers
from .models import Payment
from apps.orders.models import Order

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ("id","order","amount","method","gateway_id","status","created_at")
        read_only_fields = ("id","status","created_at")

    def validate(self, attrs):
        order = attrs["order"]
        if attrs["amount"] != order.total_amount:
            raise serializers.ValidationError("Amount must equal order total_amount")
        return attrs
