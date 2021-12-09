from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
import uuid
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from rest_framework import authentication

# Create your models here.

class BearerAuthentication(authentication.TokenAuthentication):
    """
    Simple token based authentication

    Client authenticate by passing the token key in the Authorization
    HTTP header prepending keyword bearer before it. For example:

    Authorization: Bearer 8bba67647313194787f75085dd0b3165a6381068
    """
    keyword = 'Bearer'
    

class User(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) #universally unique identifiers
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        ordering = ['-created_at']

    objects = BaseUserManager()

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)