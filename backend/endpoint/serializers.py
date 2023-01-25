from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import *
from dataclasses import field, fields
from os import access
from rest_framework import serializers
from authen.models import *
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from django.contrib.auth.hashers import make_password

# EndpointAdd serializer
class EndpointAddSerializers(serializers.ModelSerializer):
    class Meta:
        model = EndpointAdd
        fields = '__all__'
        





