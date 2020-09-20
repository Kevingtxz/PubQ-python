from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class StandardUserForm(ModelForm):
	class Meta:
		model = StandardUser
		fields = '__all__'

class UniversityForm(ModelForm):
	class Meta:
		model = University
		fields = '__all__'

class CityForm(ModelForm):
	class Meta:
		model = City
		fields = '__all__'

class AddressUserForm(ModelForm):
	class Meta:
		model = AddressUser
		fields = '__all__'

class AddressUniversityForm(ModelForm):
	class Meta:
		model = AddressUniversity
		fields = '__all__'

class SubjectForm(ModelForm):
	class Meta:
		model = Subject
		fields = '__all__'

class DisciplineForm(ModelForm):
	class Meta:
		model = Discipline
		fields = '__all__'

class QuestionForm(ModelForm):
	class Meta:
		model = Question
		fields = '__all__'

# class BookForm(ModelForm):
# 	class Meta:
# 		model = Book
# 		fields = ('name')

# class CommentaryQuestionForm(ModelForm):
# 	class Meta:
# 		model = CommentaryQuestion
# 		fields = '__all__'
