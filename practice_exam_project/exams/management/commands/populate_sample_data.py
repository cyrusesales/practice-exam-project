from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from exams.models import Exam, Question, Choice
import random

class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **options):
        # Create a superuser if none exists
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')
            self.stdout.write(self.style.SUCCESS('Superuser created'))

        # Get admin user
        admin = User.objects.get(username='admin')

        # Create sample exams
        exams_data = [
            {
                'title': 'Python Basics',
                'description': 'Test your knowledge of Python fundamentals including variables, data types, and control structures.',
                'time_limit': 30,
            },
            {
                'title': 'Database Concepts',
                'description': 'Test your understanding of database principles, SQL queries, and normalization.',
                'time_limit': 45,
            },
            {
                'title': 'Web Development',
                'description': 'Test your knowledge of HTML, CSS, JavaScript, and web frameworks.',
                'time_limit': 60,
            },
        ]

        for exam_data in exams_data:
            exam = Exam.objects.create(
                title=exam_data['title'],
                description=exam_data['description'],
                time_limit=exam_data['time_limit'],
                created_by=admin
            )
            self.stdout.write(self.style.SUCCESS(f'Created exam: {exam.title}'))

            # Create questions for each exam
            self._create_questions_for_exam(exam)

        self.stdout.write(self.style.SUCCESS('Sample data population completed'))

    def _create_questions_for_exam(self, exam):
        if exam.title == 'Python Basics':
            # Multiple choice questions
            q1 = Question.objects.create(
                exam=exam,
                question_text="What is the output of 'Hello, World[1:5]?",
                question_type='MCQ',
                points=2
            )              
            Choice.objects.create(question=q1, choice_text="H", is_correct=False)
            Choice.objects.create(question=q1, choice_text="ello", is_correct=True)
            Choice.objects.create(question=q1, choice_text="ello,", is_correct=False)
            Choice.objects.create(question=q1, choice_text="Hello", is_correct=False)

            # True/False questions
            q2 = Question.objects.create(
                exam=exam,
                question_text="In Python, lists are mutable.",
                question_type='TF',
                points=1
            )
            Choice.objects.create(question=q2, choice_text="True", is_correct=True)
            Choice.objects.create(question=q2, choice_text="False", is_correct=False)

            # Short answer questions
            Question.objects.create(
                exam=exam,
                question_text="Write a Python function to calculate the factorial of a number.",
                question_type='SHORT',
                pounts=3
            )

        elif exam.title == 'Database Concepts':
            # Multiple choice questions
            q1 = Question.objects.create(
                exam=exam,
                question_text="Which SQL clause is used to filter records?",
                question_type='MCQ',
                points=1
            )
            Choice.objects.create(question=q1, choice_text="SELECT", is_correct=False)
            Choice.objects.create(question=q1, choice_text="WHERE", is_correct=True)
            Choice.objects.create(question=q1, choice_text="GROUP BY", is_correct=False)
            Choice.objects.create(question=q1, choice_text="ORDER BY", is_correct=False)

            # True/False questions
            q2 = Question.objects.create(
                exam=exam,
                question_text="An SQL JOIN clause is used to combine rows from two or more tables.",
                question_type='TF',
                points=1
            )
            Choice.objects.create(question=q2, choice_text="True", is_correct=True)
            Choice.objects.create(question=q2, choice_text="False", is_correct=False)

            # Short answer questions
            Question.objects.create(
                exam=exam,
                question_text="Write an SQL query to retrieve all employees who earn more than the average salary.",
                question_type='SHORT',
                points=3
            )

        elif exam.title == 'Web Development':
            # Multiple choice questions
            q1 = Question.objects.create(
                exam=exam,
                question_text="Which HTML tag is used to define an unordered list?",
                question_type='MCQ',
                points=1
            )
            Choice.objects.create(question=q1, choice_text="<ol>", is_correct=False)
            Choice.objects.create(question=q1, choice_text="<ul>", is_correct=True)
            Choice.objects.create(question=q1, choice_text="<li>", is_correct=False)
            Choice.objects.create(question=q1, choice_text="<dl>", is_correct=False)

            # True/False questions
            q2 = Question.objects.create(
                exam=exam,
                question_text="CSS is used to add interactivity to web pages.",
                question_type='TF',
                points=1
            )
            Choice.objects.create(question=q2, choice_text="True", is_correct=False)
            Choice.objects.create(question=q2, choice_text="False", is_correct=True)

            # Short answer questions
            Question.objects.create(
                exam=exam,
                question_text="Explain the difference between localStorage and sessionStorage in JavaScript.",
                question_type='SHORT',
                points=3
            )
