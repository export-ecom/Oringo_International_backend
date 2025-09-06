from rest_framework.response import Response
from rest_framework.decorators import action


from rest_framework import status
from rest_framework import viewsets, permissions
from .models import CartItem
from .serializers import CartItemSerializer

class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        product = serializer.validated_data["product"]
        cart_item, created = CartItem.objects.get_or_create(
            user=self.request.user,
            product=product,
            defaults={"quantity": serializer.validated_data.get("quantity", 1)}
        )
        if not created:
            cart_item.quantity += serializer.validated_data.get("quantity", 1)
            cart_item.save()
        return cart_item

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cart_item = self.perform_create(serializer)
        # return cart item with nested product detail
        return Response(
            self.get_serializer(cart_item).data,
            status=status.HTTP_201_CREATED
        )

    @action(detail=True, methods=['patch'])
    def update_quantity(self, request, pk=None):
        cart_item = self.get_object()
        quantity = request.data.get("quantity", cart_item.quantity)
        cart_item.quantity = quantity
        cart_item.save()
        serializer = CartItemSerializer(cart_item)  # nested product included
        return Response(serializer.data)
