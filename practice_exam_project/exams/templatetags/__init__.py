# Create a custom template filter to lookup dictionary items
# exams/templatetags/__init__.py
# exams/templatetags/exam_extras.py

from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)