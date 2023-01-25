from django.shortcuts import render
from .serializers import *
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from authen.models import User
# from .serializers import SignupSerializer
from .serializers import EndpointAddSerializers
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
from django.shortcuts import get_object_or_404
from endpoint.models import EndpointAdd

class EndpointAddView(generics.CreateAPIView):
    serializer_class = EndpointAddSerializers
    queryset =User.objects.all()

    permission_classes = [IsAuthenticated]

    def post(self,request):
        user = request.user
        ser= EndpointAddSerializers (data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_201_CREATED)
        return Response (ser.errors,status=status.HTTP_400_BAD_REQUEST)
