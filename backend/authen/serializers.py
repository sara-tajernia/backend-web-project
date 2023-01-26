from dataclasses import field, fields
from os import access
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from authen.models import *
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from django.contrib.auth.hashers import make_password


# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['pk','name', 'username','password', 'created_at','updated_at']                
        extra_kwargs = {'password': {'write_only': True}}
        
    def validate_password(self, value: str) -> str:
        """
        Hash value passed by user.

        :param value: password of a user
        :return: a hashed version of the password
        """
        return make_password(value)   

# Sign up serializer
class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}


        
      