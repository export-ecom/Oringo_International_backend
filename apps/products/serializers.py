from rest_framework import serializers
from .models import Product, Category, ProductImage



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]  # include other fields if needed

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["id", "image"]


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)  # multiple images

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "price",
            "quantity_available",
            "images",  # use 'images' instead of 'image'
            "origin_country",
            "hs_code",
            "unit",
            "attributes",
            "created_at",
            "updated_at",
            "category",
        ]