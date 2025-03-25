from django.contrib import admin
from .models import Exam, Question, Choice, ExamAttempt, Answer

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInLine]
    list_display = ('question_text', 'exam', 'question_type', 'points')
    list_filter = ('exam', 'question_type')
    search_fields = ['question_text']

class QuestionInLine(admin.TabularInline):
    model = Question
    extra = 1

class ExamAdmin(admin.ModelAdmin):
    inlines = [QuestionInLine]
    list_display = ('title', 'created_by', 'created_at', 'time_limit')
    list_filter = ('created_at', 'created_by')
    search_fields = ['title', 'description']

admin.site.register(Exam, ExamAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(ExamAttempt)
admin.site.register(Answer)