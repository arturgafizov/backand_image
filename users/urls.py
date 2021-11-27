
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from users.api import RegisterApi

urlpatterns = [
    path('auth/login/',  obtain_auth_token),
    path('auth/register/', RegisterApi.as_view(), name='register'),

]
