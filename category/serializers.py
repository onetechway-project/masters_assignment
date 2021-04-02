from rest_framework import serializers

from .models import *


class CategorySerializer(serializers.ModelSerializer):
    """Handles serialization and deserialization of User objects."""

    class Meta:
        model = Categories
        fields = "__all__"


class SubCategorySerializer(serializers.ModelSerializer):
    """Handles serialization and deserialization of User objects."""

    category_name = serializers.SerializerMethodField()

    class Meta:
        model = SubCategories
        fields = ('id', 'created', 'modified', 'category_name', 'category', 'sub_category_name')

    def get_category_name(self, obj):
        if obj.category:
            return obj.category.category_name
        return ''


class ProductsSerializer(serializers.ModelSerializer):
    """Handles serialization and deserialization of User objects."""

    category_name = serializers.SerializerMethodField()
    sub_category_name = serializers.SerializerMethodField()

    class Meta:
        model = Products
        fields = ('id', 'created', 'modified', 'category_name', 'sub_category_name',
                  'product_name', 'category', 'sub_category')

    def get_category_name(self, obj):
        if obj.category:
            return obj.category.category_name
        return ''

    def get_sub_category_name(self, obj):
        if obj.sub_category:
            return obj.sub_category.sub_category_name
        return ''


class ProductsAllSerializer(serializers.ModelSerializer):
    """Handles serialization and deserialization of User objects."""

    class Meta:
        model = Products
        fields = '__all__'
