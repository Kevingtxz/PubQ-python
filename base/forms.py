from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Question

# class QuestionForm(ModelForm):
# 	class Meta:
# 		model = Question
# 		fields = '__all__'

# class CreateUserForm(ModelForm):
# 	class Meta:
# 		model = User
# 		fields = ('username', 'email', 'password1', 'password2')

# class PersonForm(ModelForm):
# 	class Meta:
# 		model = Person
# 		fields = '__all__'
# 		exclude = ['user']

# class CityForm(ModelForm):
# 	model = City
# 	fields = '__all__'

# class CommentaryForm(ModelForm):
# 	model = Commentary
# 	fields = '__all__'

# class DisciplineForm(ModelForm):
# 	model = Discipline
# 	fields = ['name']