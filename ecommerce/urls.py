"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
        openapi.Info(
            title='Ecommerce system',
            default_version='v1',
            description='django ecommerce platform',
        ),
        public=True,
        permission_classes = (permissions.AllowAny,),
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('', include('products.urls')),
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('docs/', include_docs_urls(title='Ecommerce API')),
    path('schema/', schema_view),

    #routes for simple jwt
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    #api documentation
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='swagger-redoc'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-swagger'),
]
