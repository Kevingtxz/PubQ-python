from django.db import models
from django.contrib.auth.models import User
# from django.db.models.signals import pre_save


class State(models.Model):
    name = models.CharField(max_length=100, null=True)

class City(models.Model):
    name = models.CharField(max_length=100, null=True)
    state = models.ForeignKey(State, on_delete=models.PROTECT, null=True)

class Address(models.Model):
    neighborhood = models.CharField(max_length=200, null=True)
    complement = models.CharField(max_length=200, null=True)
    city = models.ForeignKey(City, on_delete=models.PROTECT, null=True)

class Person(models.Model):
    # user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=11, null=True)
    email = models.CharField(max_length=200, null=True)
    sex = models.CharField(max_length=1, null=True)
    birth = models.CharField(max_length=8, null=True)
    profile_pic = models.ImageField(default='profile1.png', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    address = models.OneToOneField(Address, null=True, blank=True, on_delete=models.PROTECT)

class Student(models.Model):
    # user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    universities = []

class Teacher(models.Model):
    # user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    universities = []

class Performance(models.Model):
    # user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
 	question_wrong = []
 	question_right = []

class Exam(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    diciplines = []
    subject = []
    questions = []
    user_like = []
    user_deslike = []

class Question(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    text = models.CharField(max_length=10000, null=True)
    answears = [models.CharField(max_length=500, null=True)]
    right_answear = models.CharField(max_length=1, null=True)

    # exam = 
    # user_poster = models
    # commentaties = 
    # users_like = 
    # users_deslike =
    # wrong_answer =
    # right_answer = 


# class Book(models.Model):
    # user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    # questions = []
    # exams = []


# class Commentary(models.Model):
    # user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    # questions = 
    # users_like = 
    # users_deslike =


class Subject(models.Model):
 	name = models.CharField(max_length=200, null=True)
 	# exam = []

class Discipline(models.Model):
	name = models.CharField(max_length=200, null=True)
    # subjects = []

class University(models.Model): 
	data_created = models.DateTimeField(auto_now_add=True, null=True)
	name = models.CharField(max_length=200, null=True)
	initials = models.CharField(max_length=5, null=True)
    
	# students = []
	# teachers = []
	# address = 
