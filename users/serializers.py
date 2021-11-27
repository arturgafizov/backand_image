from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterUserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password', 'email', )
