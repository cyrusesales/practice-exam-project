from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Exam, Question, Choice, ExamAttempt, Answer

def index(request):
    """Home page view"""
    exams = Exam.objects.all().order_by('-created_at')[:5]
    return render(request, 'exams/index.html', {'exams': exams})

def exam_list(request):
    """List all available exams"""
    exams = Exam.objects.all().order_by('-created_at')
    return render(request, 'exams/exam_list.html', {'exams': exams})

def exam_details(request, exam_id):
    """Show exam details and option to start exam"""
    exam = get_object_or_404(Exam, pk=exam_id)
    return render(request, 'exams/exam_details.html', {'exam': exam})
