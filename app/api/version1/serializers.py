from rest_framework import serializers

from app.models import Category, Result


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug']


class ResultListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'
