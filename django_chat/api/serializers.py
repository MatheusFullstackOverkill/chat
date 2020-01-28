from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'url']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = [
            'message',
            'from_user',
            'room'
        ]

