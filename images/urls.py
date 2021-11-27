from django.urls import path

from .api import JWTTokenView


urlpatterns = [
    path('jwt/token/',  JWTTokenView.as_view(), name='jwt_token'),

]
