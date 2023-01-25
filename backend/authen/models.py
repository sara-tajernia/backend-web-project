from urllib import request
from uuid import uuid4
from django.db import models
import random
import string
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.core.validators import RegexValidator
from datetime import timedelta
from django.utils import timezone


class User(AbstractUser):
    name =models.CharField(max_length=20,blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

