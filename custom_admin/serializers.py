# custom_admin/serializers.py
from rest_framework import serializers
from apps.products.models import Product
from apps.products.models import Category
from apps.products.models import ProductImage
from apps.blog.models import Blog
from apps.orders.models import Order
from apps.quotations.models import QuotationRequest

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class QuotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuotationRequest
        fields = '__all__'
