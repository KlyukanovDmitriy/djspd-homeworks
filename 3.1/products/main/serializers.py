from rest_framework import serializers
from main.models import Product, Review


class ReviewSerializer(serializers.ModelSerializer):
    # реализуйте все поля
    class Meta:
        model = Review
        fields = ['text', 'mark']

class ProductListSerializer(serializers.Serializer):
    # реализуйте поля title и price
    title = serializers.CharField()
    price = serializers.DecimalField(10, 2)


class ProductDetailsSerializer(serializers.ModelSerializer):
    # реализуйте поля title, description, price и reviews (список отзывов к товару)
    reviews = ReviewSerializer(many = True, read_only = True)

    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'reviews']

