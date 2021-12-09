from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from users.models import User
from users.serializers import UserRegistrationSerializer
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.reverse import reverse

# Create your views here.

@api_view(['POST'])
def registration_view(request, format=None):
    #user registration
    data = {}
    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.data)
    
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "User created successfully"
            token = Token.objects.get(user=user).key
            data['token'] = token
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def logout(request, format=None):
    #user logout
    request.user.auth_token.delete() #deletes token
    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'register': reverse('register', request=request, format=format),
        'login': reverse('login', request=request, format=format),
        'logout': reverse('logout', request=request, format=format),
    })