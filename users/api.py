from django.contrib.auth.hashers import make_password
from rest_framework import generics
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from .serializers import RegisterUserSerializer

User = get_user_model()


class RegisterApi(generics.CreateAPIView):
    serializer_class = RegisterUserSerializer

    def perform_create(self, serializer):
        raw_password = serializer.validated_data.get('password')
        username = serializer.validated_data.get('username')
        email = serializer.validated_data.get('email')
        user = User.objects.create(
            username=username,
            password=make_password(raw_password),
            email=email,

        )
        token, created = Token.objects.get_or_create(user=user)



