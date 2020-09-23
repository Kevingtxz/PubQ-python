from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class CityForm(ModelForm):
	class Meta:
		model = City
		fields = '__all__'

class AddressForm(ModelForm):
	class Meta:
		model = Address
		fields = '__all__'
		
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class StandardUserForm(ModelForm):
	class Meta:
		model = StandardUser
		fields = '__all__'

class UserPermissionForm(ModelForm):
	class Meta:
		model = UserPermission
		fields = '__all__'	

class ReportForm(ModelForm):
	class Meta:
		model = Report
		fields = '__all__'

class CommentaryForm(ModelForm):
	class Meta:
		model = Commentary
		fields = ('text', 'standard_user',)

class UniversityForm(ModelForm):
	class Meta:
		model = University
		fields = '__all__'

class SubjectForm(ModelForm):
	class Meta:
		model = Subject
		fields = '__all__'

class DisciplineForm(ModelForm):
	class Meta:
		model = Discipline
		fields = '__all__'

class AnswearForm(ModelForm):
	class Meta:
		model = Answear
		fields = ('standard_user', 'text',)

class QuestionForm(ModelForm):
	class Meta:
		model = Question
		fields = ('teacher_name', 'university_name', 'text', 'education_Level', 'pic_1', 'pic_2', 'answear', 'is_public',)

class BookForm(ModelForm):
	class Meta:
		model = Book
		fields = ('title', 'note',)

class NotificationForm(ModelForm):
	class Meta:
		model = Notification
		fields = '__all__'

class RequisitionForm(ModelForm):
	class Meta:
		model = Requisition
		fields = '__all__'
