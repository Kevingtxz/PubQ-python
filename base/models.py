from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


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

    def __str__(self):
        return self.person

class Teacher(models.Model):
    person = models.OneToOneField(Person, null=True, blank=True, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.person

class Exam(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)

class Question(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    text = models.TextField
    exam = models.ForeignKey(Exam, null=True, blank=True, on_delete=models.CASCADE)  
    poster = models.ForeignKey(Person, on_delete=models.PROTECT)
    right_answear = models.CharField(max_length=1)
    answears = ArrayField(models.TextField(blank=True), size=5)

    def __str__(self):
        return [self.text, self.poster]

class Performance(models.Model):
    person = models.OneToOneField(Person, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.person

class QuestionWrong(models.Model):
    performance = models.ForeignKey(Performance, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

class QuestionRight(models.Model):
    performance = models.ForeignKey(Performance, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

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
    text = models.TextField

    def __str__(self):
        return self.person

class CommentaryQuestion(Commentary):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

class CommentaryExam(Commentary):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)

class CommentaryBook(Commentary):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

class CommentaryUniversity(Commentary):
    university = models.ForeignKey(University, on_delete=models.CASCADE)

class LikeDeslike(Commentary):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.person

class Interaction(models.Model):
    islike = models.BooleanField
    like_deslike = models.ForeignKey(LikeDeslike, blank= True, on_delete=models.CASCADE)

    def __str__(self):
        return self.islike


class InteractionQuestion(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, blank=True)

class InteractionExam(models.Model):
    islike = models.BooleanField
    like_deslike = models.ForeignKey(LikeDeslike, blank= True, on_delete=models.CASCADE)
    models.ForeignKey(Exam, on_delete=models.CASCADE, blank=True)

class InteractionCommentaryQuestion(models.Model):
    islike = models.BooleanField
    like_deslike = models.ForeignKey(LikeDeslike, blank= True, on_delete=models.CASCADE)
    models.ForeignKey(CommentaryQuestion, on_delete=models.CASCADE, blank=True)

class InteractionCommentaryExam(models.Model):
    islike = models.BooleanField
    like_deslike = models.ForeignKey(LikeDeslike, blank= True, on_delete=models.CASCADE)
    models.ForeignKey(CommentaryExam, on_delete=models.CASCADE, blank=True)

class InteractionCommentaryUniversity(models.Model):
    islike = models.BooleanField
    like_deslike = models.ForeignKey(LikeDeslike, blank= True, on_delete=models.CASCADE)
    models.ForeignKey(CommentaryUniversity, on_delete=models.CASCADE, blank=True)

class InteractionCommentaryBook(models.Model):
    islike = models.BooleanField
    like_deslike = models.ForeignKey(LikeDeslike, blank= True, on_delete=models.CASCADE)
    models.ForeignKey(CommentaryBook, on_delete=models.CASCADE, blank=True)
    

class InteractionBook(models.Model):
    islike = models.BooleanField
    like_deslike = models.ForeignKey(LikeDeslike, blank= True, on_delete=models.CASCADE)
    models.ForeignKey(Book, on_delete=models.CASCADE, blank=True)

class InteractionUniversity(models.Model):
    islike = models.BooleanField
    like_deslike = models.ForeignKey(LikeDeslike, blank= True, on_delete=models.CASCADE)
    models.ForeignKey(University, on_delete=models.CASCADE, blank=True)

class StudentUniversity(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.CASCADE)

class TeacherUniversity(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.CASCADE)

