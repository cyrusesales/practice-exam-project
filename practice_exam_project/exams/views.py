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

@login_required
def start_exam(request, exam_id):
    """Initialize an exam attempt and redirect to the exam page"""
    exam = get_object_or_404(Exam, pk=exam_id)
    attempt = ExamAttempt.objects.create(
        exam=exam,
        user=request.user
    )
    return redirect('take_exam', attempt_id=attempt.id)

@login_required
def take_exam(request, attempt_id):
    """View for taking an exam"""
    attempt = get_object_or_404(ExamAttempt, pk=attempt_id)

    # Check if the exam has already been completed
    if attempt.end_time:
        return redirect('exam_results', attempt_id=attempt.id)
    
    # Check if time limit has expired
    if attempt.start_time:
        elapsed_time = timezone.now() = attempt.start_time
        if elapsed_time.total_seconds() > (attempt.exam.time_limit * 60):
            attempt.end_time = timezone.now()
            attempt.calculate_score()
            attempt.save()
            return redirect('exam_results', attempt_id=attempt.id)
        
    if request.method == 'POST':
        # Process submitted answers
        questions = attempt.exam.get_questions()

        for question in questions:
            if question.question_type in ['MCQ', 'TF']:
                choice_id = request.POST.get(f'question_{question.id}')
                if choice_id:
                    choice = get_object_or_404(Choice, pk=choice_id)
                    Answer.objects.update_or_create(
                        attempt=attempt,
                        question=question,
                        defaults={'selected_choice': choice}
                    )
            elif question.question_type == 'SHORT':
                text_answer = request.POST.get(f'question_{question.id}')
                if text_answer:
                    Answer.objects.update_or_create(
                        attempt=attempt,
                        question=question,
                        defaults={'text_answer': text_answer}
                    )

        # Check if the form was submitted for grading
        if 'submit_exam' in request.POST:
            attempt.end_time = timezone.now()
            attempt.calculate_score()
            attempt.save()
            return redirect('exam_results', attempt_id=attempt.id)
        
    questions = attempt.exam.get_questions()
    answers = {answer.question_id: answer for answer in Answer.objects.filter(attempt=attempt)}

    context = {
        'attempt': attempt,
        'questions': questions,
        'answers': answers,
    }
    return render(request, 'exams/take_exam.html', context)

@login_required
def exam_results(request, attempt_id):
    """Show exam results"""
    attempt = get_object_or_404(ExamAttempt, pk=attempt_id)

    if not attempt.end_time:
        return redirect('take_exam', attempt_id=attempt.id)
    
    answers = Answer.objects.filter(attempt=attempt)

    context = {
        'attempt': attempt,
        'answers': answers,
    }
    return render(request, 'exams/results.html', context)