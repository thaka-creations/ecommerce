from products.models import Category, Product, Subcategory, OrderLine
from rest_framework import serializers
from django.db.models import Count


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    subcategories = serializers.HyperlinkedRelatedField(many=True, view_name='subcategory-detail', read_only=True)
    class Meta:
        model = Category
        fields = ['name','description','url','subcategories']

class SubcategorySerializer(serializers.HyperlinkedModelSerializer):
    products = serializers.HyperlinkedRelatedField(many=True, view_name='product-detail', read_only=True)
    class Meta:
        model = Subcategory
        fields = ['name','description','url','category','products']

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['name','price','quantity','description','url','subcategory']

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderLine
        fields = ['product','quantity']