from rest_framework import generics

from app.api.version1.serializers import CategorySerializer
from app.models import Category


class CategoryCreateAPIView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


def category_detail_view(request, category_id):
    pass