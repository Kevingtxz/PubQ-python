from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = "__all__"


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = "__all__"


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )


class StandardUserForm(ModelForm):
    class Meta:
        model = StandardUser
        fields = "__all__"


class UserPermissionForm(ModelForm):
    class Meta:
        model = UserPermission
        fields = "__all__"


class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = "__all__"


class CommentaryForm(ModelForm):
    class Meta:
        model = Commentary
        fields = (
            "text",
            "standarduser",
        )


class UniversityForm(ModelForm):
    class Meta:
        model = University
        fields = "__all__"


class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = "__all__"


class DisciplineForm(ModelForm):
    class Meta:
        model = Discipline
        fields = "__all__"


class AnswearForm(ModelForm):
    class Meta:
        model = Answear
        fields = (
            "text",
        )


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = (
            "teacher_name",
            "text",
            "education_Level",
            "pic_1",
            "pic_2",
            "answear",
            "is_public",
        )


class ExamForm(ModelForm):
    class Meta:
        model = Exam
        fields = "__all__"

    def clean(self):
        questions = self.cleaned_data.get("questions")
        if questions and questions.count() > 20:
            raise ValidationError("Maximum twenty questions are allowed.")
        return self.cleaned_data


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = (
            "title",
            "note",
        )

    def clean(self):
        questions = self.cleaned_data.get("questions")
        if questions and questions.count() > 50:
            raise ValidationError("Maximum twenty questions are allowed.")
        return self.cleaned_data


class TimeToApplyExamForm(ModelForm):
    class Meta:
        model = TimeToApplyExam
        fields = (
            "date_to_apply",
            "date_to_finish",
        )


class NotificationForm(ModelForm):
    class Meta:
        model = Notification
        fields = "__all__"


class RequisitionForm(ModelForm):
    class Meta:
        model = Requisition
        fields = "__all__"
