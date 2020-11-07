import django_filters
from .models import *

class QuestionFilter(django_filters.FilterSet):
    class Meta:
        model = Question
        fields = "__all__"
        exclude = ['pic_1', 'pic_2', 'date_created', 'is_public', 'reports', 'wrong_answears_count', 'answears', 'answear',]