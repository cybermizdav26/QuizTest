from django.contrib import admin

from .models import Category, Question, Answer, Result
from import_export.admin import ImportExportModelAdmin

# admin.site.register(Category)
# admin.site.register(Question)
# admin.site.register(Answer)
# admin.site.register(Result)

from django.contrib import admin

from .models import Category, Question, Answer, Result


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ['id', 'name', 'question_count']
    search_fields = ['name']

    def question_count(self, obj):
        return obj.question_set.count()
    question_count.short_description = 'Question count'


class AnswerInlineModel(admin.TabularInline):
    model = Answer
    fields = ['name', 'is_correct']
    can_delete = False


@admin.register(Question)
class QuestionAdmin(ImportExportModelAdmin):
    fields = ['name', 'category']
    list_display = ['name', 'category', ]
    list_filter = ['category',]
    search_fields = ['name', 'category__name']
    inlines = [AnswerInlineModel]


@admin.register(Answer)
class AnswerAdmin(ImportExportModelAdmin):
    list_display = ['name', 'is_correct', 'question']


@admin.action(description='Return score')
def selected_zero(modeladmin, request, queryset):
    queryset.update(score=0)


class ResultAdmin(ImportExportModelAdmin):
    list_display = ['user', 'category', 'total_questions', 'total_correct', 'score']
    list_filter = ['user', 'category']
    search_fields = ['user__phone', 'category__name']
    actions = [selected_zero]


admin.site.register(Result, ResultAdmin)

