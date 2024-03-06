from django.urls import path

from .views import HomePageView, question_list, result_list, TestsView

app_name = 'app'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('question/<slug:slug>', question_list, name='question_list'),
    path('result/', result_list, name='result_list'),
    path('tests/', TestsView.as_view(), name='tests')
]

