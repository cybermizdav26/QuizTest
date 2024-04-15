from django.urls import path

from app.api.version1.views import CategoryCreateAPIView

urlpatterns = [
    path('category-create/', CategoryCreateAPIView.as_view(), name='category-create')
]