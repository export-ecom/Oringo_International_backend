from rest_framework import serializers
from .models import CartItem
from apps.products.serializers import ProductSerializer

class CartItemSerializer(serializers.ModelSerializer):
    product_detail = ProductSerializer(source='product', read_only=True)

    class Meta:
        model = CartItem
        fields = [
            "id",
            "quantity",
            "product",         # product ID
            "product_detail",  # nested full product details
        ]
        read_only_fields = ["user"]
