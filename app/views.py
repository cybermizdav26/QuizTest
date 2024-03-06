from django.shortcuts import render
from django.views.generic import TemplateView

from .filters import ResultFilter
from .models import Category, Question, Result
from .services import check_answer


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        cd = super().get_context_data(**kwargs)
        cd['categories'] = Category.objects.all()
        return cd


def question_list(request, slug):
    category = Category.objects.get(slug=slug)
    questions = Question.objects.filter(category=category)
    # if cache.get('questions'):
    #     questions = cache.get('questions')
    # else:
    #     cache.set('questions', question_list)
    #     questions = question_list
    if request.method == "POST":
        context = check_answer(request, questions, category)
        return render(request, 'result.html', context)

    context = {
        'questions': questions,
        'category': category,
    }

    return render(request, template_name='question_list.html', context=context)


def result_list(request):
    filters = ResultFilter(request.GET, queryset=Result.objects.all())

    context = {
        'filter': filters
    }

    return render(request, 'result_list.html', context)


# def result_list(request):
#     queryset = Result.objects.all()
#
#     context = {
#         'filter': ResultFilter(queryset=queryset)
#     }
#
#     return render(request, 'result_list.html', context)


class TestsView(TemplateView):
    template_name = 'tests.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context['categories'] = categories
        return context


# Create your views here.
