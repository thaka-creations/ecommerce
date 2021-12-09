from django.urls import path
from rest_framework import urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns
from users import views
from rest_framework.authtoken import views


urlpatterns = [
    path('', views.api_root, name='user-api-endpoint'),
    path('register/', views.registration_view, name='register'),
    path('login/', views.obtain_auth_token, name='login' ),
    path('logout/', views.logout, name='logout'),
]

urlpatterns = format_suffix_patterns(urlpatterns)