from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView

from . import serializers
from . import models


# Create your views here.
class SignUpView(CreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        print('validated data : ',serializer.validated_data)

        self.perform_create(serializer)
        
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    