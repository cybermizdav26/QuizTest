from django.urls import path

from account.api.version1.views import UserCreateAPIView

urlpatterns = [
    path('create', UserCreateAPIView.as_view(), name='create')
]