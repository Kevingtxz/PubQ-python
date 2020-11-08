import django_filters
from .models import *

class QuestionFilter(django_filters.FilterSet):
    note = django_filters.CharFilter(field_name='text', lookup_expr='icontains')
    teacher = django_filters.CharFilter(field_name='teacher_name', lookup_expr='icontains')
    class Meta:
        model = Question
        fields = ['education_Level', 'year', 'difficult', 'exams', 'subject', 'university', 'books',]