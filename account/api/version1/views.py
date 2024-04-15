from django.contrib.auth import get_user_model
from rest_framework import generics

from .serializers import UserCreateSerializer

User = get_user_model()


class UserCreateAPIView(generics.CreateAPIView):
    user = User.objects.all()
    serializer_class = UserCreateSerializer


