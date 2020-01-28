from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.http import FileResponse
from .serializers import *
import os
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class Teste(APIView):
    def get(self, request, format=None):
        module_dir = os.path.dirname(__file__)  # get current directory
        file_path = os.path.join(module_dir, 'images/914cc990c7bd0ba5d8b775ebe4426f9a.jpg')
        print(file_path)
        img = open(file_path, 'rb')

        response = FileResponse(streaming_content=(img), as_attachment=True, filename='image.jpg')

        return response
