from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from products.views import ProductViewSet, CategoryViewSet, SubcategoryViewSet, OrderViewSet, AddToCartView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'categories', CategoryViewSet)
router.register(r'subcategories', SubcategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += format_suffix_patterns(
    urlpatterns = [
       path('add-to-cart/', AddToCartView.as_view(), name='add-to-cart'),
    ]
)