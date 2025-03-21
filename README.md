# practice_exam_project

# README.md

"""
# Practice Exam System

A Django application for creating and taking practice exams.

## Features

- Create exams with multiple question types (Multiple Choice, True/False, Short Answer)
- Take exams with time limits
- Automatic grading for Multiple Choice and True/False questions
- View detailed exam results
- Admin interface for managing exams and questions

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/practice-exam-system.git
   cd practice-exam-system
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Configure MySQL database settings in `practice_exam_project/settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'practice_exam_db',
           'USER': 'your_db_user',
           'PASSWORD': 'your_db_password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

5. Create the MySQL database:
   ```
   mysql -u root -p
   CREATE DATABASE practice_exam_db;
   CREATE USER 'your_db_user'@'localhost' IDENTIFIED BY 'your_db_password';
   GRANT ALL PRIVILEGES ON practice_exam_db.* TO 'your_db_user'@'localhost';
   FLUSH PRIVILEGES;
   EXIT;
   ```

6. Run migrations:
   ```
   python manage.py makemigrations exams
   python manage.py migrate
   ```

7. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

8. Load sample data (optional):
   ```
   python manage.py populate_sample_data
   ```

9. Run the development server:
   ```
   python manage.py runserver
   ```

10. Access the application at http://127.0.0.1:8000/

## Usage

1. Log in as an admin user
2. Create exams and questions through the admin interface or Django shell
3. Users can browse available exams and take them
4. After completing an exam, users can see their results

## Requirements File

Create a `requirements.txt` file with the following:

```
Django>=4.2.0,<5.0.0
mysqlclient>=2.1.0
python-dotenv>=1.0.0
```
"""

# Create a .env.example file to show environment variables needed

"""
# Database configuration
DB_NAME=practice_exam_db
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=3306

# Django configuration
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
"""