from django.shortcuts import render
from rest_framework import generics, serializers, viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import views
from products.models import Category, Product, Subcategory, Order, OrderLine
from products.serializers import CategorySerializer, ProductSerializer, SubcategorySerializer, OrderSerializer
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from rest_framework import filters
from products.cart import Cart

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    #using view sets
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_fields = ['name','subcategories__name']
    permission_classes = [IsAuthenticated]

class SubcategoryViewSet(viewsets.ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    filterset_fields = ['name','category__name']

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['=name','price']
    ordering_fields = ['price','name']
    ordering = ['price']


class OrderViewSet(viewsets.ModelViewSet):
    queryset = OrderLine.objects.all()
    serializer_class = OrderSerializer

class AddToCartView(views.APIView):
    #adding an item to cart session
    #serializer = ProductSerializer(product, context={'request':request})
    def get(self,request, format=None):
        
        #add to cart method
        id = request.data['product_id']
        quantity = request.data['quantity']
        cart = Cart(request, id, quantity)
        res = cart.add_to_cart()
        
        return Response(res)

        



        
