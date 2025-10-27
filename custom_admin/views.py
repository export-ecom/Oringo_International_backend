from django.shortcuts import render

# Create your views here.
# custom_admin/views.py
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from .permissions import IsAdminUserType
from .serializers import (
    ProductSerializer, BlogSerializer, OrderSerializer, QuotationSerializer, CategorySerializer,ProductImageSerializer
)
from apps.products.models import Product
from apps.products.models import Category
from apps.blog.models import Blog
from apps.orders.models import Order
from apps.quotations.models import QuotationRequest
from apps.products.models import ProductImage


# ----------------- CATEGORY MANAGEMENT -----------------
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_category(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_category(request, pk):
    try:
        category = Category.objects.get(pk=pk)
        category.delete()
        return Response({'message': 'Category deleted successfully'})
    except category.DoesNotExist:
        return Response({'error': 'Category not found'}, status=404)

# ----------------- PRODUCT MANAGEMENT -----------------
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([AllowAny])
def add_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'PATCH'])
@permission_classes([AllowAny])
def edit_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=404)

    serializer = ProductSerializer(product, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response({'message': 'Product deleted successfully'})
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=404)
# ----------------- PRODUCT IMAGE MANAGEMENT -----------------

@api_view(['POST'])
def add_product_image(request):
    serializer = ProductImageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'PATCH'])
@parser_classes([MultiPartParser, FormParser])
def edit_product_image(request, pk):
    try:
        product_image = ProductImage.objects.get(pk=pk)
    except ProductImage.DoesNotExist:
        return Response({"error": "Product image not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = ProductImageSerializer(product_image, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_product_image(request, pk):
    try:
        product_image = ProductImage.objects.get(pk=pk)
    except ProductImage.DoesNotExist:
        return Response({"error": "Product image not found"}, status=status.HTTP_404_NOT_FOUND)

    # Optional: delete file from storage
    if product_image.image:
        product_image.image.delete(save=False)

    product_image.delete()
    return Response({"message": "Product image deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
# ----------------- BLOG MANAGEMENT -----------------
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_blogs(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([AllowAny])
def add_blog(request):
    serializer = BlogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_blog(request, pk):
    try:
        blog = Blog.objects.get(pk=pk)
        blog.delete()
        return Response({'message': 'Blog deleted successfully'})
    except Blog.DoesNotExist:
        return Response({'error': 'Blog not found'}, status=404)

# ----------------- ORDER MANAGEMENT -----------------
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_orders(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

# ----------------- QUOTATION MANAGEMENT -----------------
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_quotations(request):
    quotations = QuotationRequest.objects.all()
    serializer = QuotationSerializer(quotations, many=True)
    return Response(serializer.data)
