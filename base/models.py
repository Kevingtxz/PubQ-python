from django.db import models
from django.contrib.auth.models import User


class State(models.Model):
    initials = models.CharField(max_length=2)

    def __str__(self):
        return self.initials

class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.PROTECT)

    def __str__(self):
        return [self.name, self.state]

class Address(models.Model):
    neighborhood = models.CharField(max_length=200, null=True)
    complement = models.CharField(max_length=200, null=True)
    city = models.ForeignKey(City, on_delete=models.PROTECT)

    def __str__(self):
        return [self.neighborhood, self.complement, self.city]

class Person(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=11, null=True)
    email = models.CharField(max_length=200, null=True)
    sex = models.CharField(max_length=1, null=True)
    birth = models.CharField(max_length=8, null=True)
    profile_pic = models.ImageField(default='profile1.png', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    address = models.OneToOneField(Address, null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return [self.firstname, self.lastname]

class University(models.Model):
    name = models.CharField(max_length=200, null=True)
    data_created = models.DateTimeField(auto_now_add=True, null=True)
    initials = models.CharField(max_length=5, null=True)
    address = models.OneToOneField(Address, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class Student(models.Model):
    person = models.OneToOneField(Person, null=True, blank=True, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.SET_NULL, null=True)
    # universities = models.ManyToManyField(University, blank=True)

    def __str__(self):
        return self.person

class Teacher(models.Model):
    person = models.OneToOneField(Person, null=True, blank=True, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.SET_NULL, null=True)
    # universities = models.ManyToManyField(University, blank=True)

    def __str__(self):
        return self.person

class Exam(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    person_like = models.ManyToManyField(Person, blank=True)
    # person_deslike = models.ManyToManyField(Person, blank=True)

class Question(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    text = models.CharField(max_length=10000, null=True)
    answears = [models.CharField(max_length=500, null=True)]
    right_answear = models.CharField(max_length=1, null=True)

    exam = models.ForeignKey(Exam, null=True, blank=True, on_delete=models.CASCADE)  
    poster = models.OneToOneField(Person, on_delete=models.PROTECT)

    # person_like = models.ManyToManyField(Person, blank=True)
    # person_deslike = models.ManyToManyField(Person, blank=True)

    def __str__(self):
        return [self.text, self.poster]

class Performance(models.Model):
    person = models.OneToOneField(Person, null=True, blank=True, on_delete=models.CASCADE)
    question_wrong = models.ManyToManyField(Question, blank=True)
    # question_right = models.ManyToManyField(Question, blank=True)

    def __str__(self):
        return self.person

class Subject(models.Model):
    name = models.CharField(max_length=200, null=True)
    exam = models.ManyToManyField(Exam, blank=True)
    question = models.ManyToManyField(Question, blank=True)

    def __str__(self):
        return self.name

class Discipline(models.Model):
    name = models.CharField(max_length=200, null=True)
    subjects = models.ManyToManyField(Subject, blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=200)

    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    questions = models.ManyToManyField(Question, blank=True)
    exams = models.ManyToManyField(Exam, blank=True)

    def __str__(self):
        return self.name

class Commentary(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE) 
    # person_like = models.ManyToManyField(Person, blank=True)
    # person_deslike = models.ManyToManyField(Person, blank=True)
