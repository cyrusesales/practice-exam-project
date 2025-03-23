from django.db import models
from django.contrib.auth.models import User

class Exam(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    time_limit = models.IntegerField(help_text="Time limit in minutes")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_questions(self):
        return self.question_set.all()
    
    def get_total_score(self):
        return sum(question.points for question in self.get_questions())
    
class Question(models.Model):
    QUESTION_TYPES = (
        ('MCQ', 'Multiple Choice'),
        ('TF', 'True/False'),
        ('SHORT', 'Short Answer'),
    )

    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question_text = models.TextField()
    question_type = models.CharField(max_length=5, choices=QUESTION_TYPES)
    points = models.IntegerField(default=1)

    def __str__(self):
        return self.question_text[:50]
    
    def get_choices(self):
        return self.choice_set.all()
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text
    
class ExamAttempt(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    score = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s attempt on {self.exam.title}"
    
    def calculate_score(self):
        answers = self.answer_set.all()
        total_points = self.exam.get_total_score()
        earned_points = 0

        for answer in answers:
            if answer.is_correct():
                earned_points += answer.question.points

        self.score = (earned_points / total_points) * 100 if total_points > 0 else 0
        self.save()
        return self.score
    
class Answer(models.Model):
    attempt = models.ForeignKey(ExamAttempt, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_choice = models.ForeignKey(Choice, on_delete=models.CASCADE, null=True, blank=True)
    text_answer = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Answer to {self.question}"
    
    def is_correct(self):
        if self.question.question_type == 'MCQ':
            return self.selected_choice and self.selected_choice.is_correct
        elif self.question.question_type == 'TF':
            return self.selected_choice and self.selected_choice.is_correct
        elif self.question.question_type == 'SHORT':
            # For short answer, we'll need manual grading
            return False
        return False
    