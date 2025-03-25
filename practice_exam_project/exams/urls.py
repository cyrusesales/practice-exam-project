from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('exams/', views.exam_list, name='exam_list'),
    path('exams/<int:exam_id>/', views.exam_detail, name='exam_detail'),
    path('exams/<int:exam_id>/start/', views.start_exam, name='start_exam'),
    path('attempt/<int:attempt_id>/', views.take_exam, name='take_exam'),
    path('results/<int:attempt_id>/', views.exam_results, name='exam_results'),
]
