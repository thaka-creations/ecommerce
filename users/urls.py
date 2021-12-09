from django.urls import path
from rest_framework import urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns
from users.views import registration_view, api_root, logout
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('', api_root, name='user-api-endpoint'),
    path('register/', registration_view, name='register'),
    path('login/', obtain_auth_token, name='login' ),
    path('logout/', logout, name='logout'),
]

urlpatterns = format_suffix_patterns(urlpatterns)