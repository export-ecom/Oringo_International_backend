from rest_framework import serializers
from .models import Order, OrderItem
from apps.products.serializers import ProductSerializer
from apps.cart.models import CartItem
from django.db import transaction

class OrderItemSerializer(serializers.ModelSerializer):
    product_detail = ProductSerializer(source="product", read_only=True)
    class Meta:
        model = OrderItem
        fields = ("id", "product", "product_detail", "quantity", "price")

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = ("id", "user", "full_name", "email", "phone", "address",
                  "city", "state", "pincode", "payment_method",
                  "coupon", "status", "created_at", "total_amount", "items")
        read_only_fields = ("id", "user", "status", "created_at", "total_amount", "items")

class OrderCreateSerializer(serializers.Serializer):
    full_name = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    address = serializers.CharField()
    city = serializers.CharField()
    state = serializers.CharField()
    pincode = serializers.CharField()
    payment_method = serializers.ChoiceField(choices=[("cod","Cash on Delivery"), ("prepaid","Prepaid")], default="cod")
    coupon = serializers.CharField(required=False, allow_blank=True)

    @transaction.atomic
    def create(self, validated_data):
        user = self.context["request"].user
        cart_items = CartItem.objects.select_related("product").filter(user=user)
        if not cart_items.exists():
            raise serializers.ValidationError("Cart is empty")

        # stock check
        for ci in cart_items:
            if ci.quantity > ci.product.stock:
                raise serializers.ValidationError(f"Insufficient stock for {ci.product.name}")

        # Create order
        order = Order.objects.create(
            user=user,
            full_name=validated_data["full_name"],
            email=validated_data["email"],
            phone=validated_data["phone"],
            address=validated_data["address"],
            city=validated_data["city"],
            state=validated_data["state"],
            pincode=validated_data["pincode"],
            payment_method=validated_data["payment_method"],
            coupon=validated_data.get("coupon", ""),
            status="Pending"
        )

        for ci in cart_items:
            OrderItem.objects.create(
                order=order,
                product=ci.product,
                quantity=ci.quantity,
                price=ci.product.price,
            )
            ci.product.stock -= ci.quantity
            ci.product.save()

        cart_items.delete()
        return order
