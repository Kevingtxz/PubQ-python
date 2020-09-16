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
        return self.name

class Address(models.Model):
    neighborhood = models.CharField(max_length=200)
    complement = models.CharField(max_length=200, null=True)
    city = models.ForeignKey(City, on_delete=models.PROTECT)

class Person(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=200)
    phone = models.CharField(max_length=11, blank= True)
    email = models.CharField(max_length=200)
    sex = models.CharField(max_length=1, blank= True)
    birth = models.CharField(max_length=8)
    profile_pic = models.ImageField(default='profile1.png', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    address = models.OneToOneField(Address, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.firstname

class University(models.Model):
    name = models.CharField(max_length=200)
    data_created = models.DateTimeField(auto_now_add=True, null=True)
    initials = models.CharField(max_length=5, blank= True)
    address = models.OneToOneField(Address, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class Student(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.SET_NULL, null= True, blank= True)

    def __str__(self):
        return self.person

class Teacher(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.SET_NULL, null= True, blank=True)

    def __str__(self):
        return self.person

class Exam(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)

class Question(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    text = models.TextField(blank= True)
    exam = models.ForeignKey(Exam, blank=True, on_delete=models.CASCADE, null=True)  
    poster = models.ForeignKey(Person, on_delete=models.PROTECT)
    right_answear = models.CharField(max_length=1, blank= True)
    answears = ArrayField(models.TextField(null=True, blank=True), size=5, null=True, blank=True)

    teacher_owner = models.ForeignKey(Teacher, blank=True, on_delete=models.PROTECT)
    university = models.ForeignKey(University, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.text

class Performance(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.person


class Subject(models.Model):
    name = models.CharField(max_length=200)
    question = models.ManyToManyField(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Discipline(models.Model):
    name = models.CharField(max_length=200)
    subject = models.ManyToManyField(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=200)

    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    questions = models.ManyToManyField(Question, blank=True)
    exams = models.ManyToManyField(Exam,  blank=True)

    def __str__(self):
        return self.name


class QuestionRightWrong(models.Model):
    is_right = models.BooleanField
    performance = models.ForeignKey(Performance, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.is_right   


class Commentary(models.Model):
    person = models.ForeignKey(Person, on_delete=models.PROTECT)
    text = models.TextField

    def __str__(self):
        return self.person

class CommentaryQuestion(Commentary):
    questions = models.ManyToManyField(Question, on_delete=models.CASCADE)

class CommentaryExam(Commentary):
    exams = models.ManyToManyField(Exam, on_delete=models.CASCADE)

class CommentaryBook(Commentary):
    books = models.ManyToManyField(Book, on_delete=models.CASCADE)

class CommentaryUniversity(Commentary):
    universities = models.ManyToManyField(University, on_delete=models.CASCADE)


class Like(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

class LikeQuestion(Like):
    questions = models.ManyToManyField(Question, on_delete=models.CASCADE, blank=True)

class LikeExam(Like):
    exams = models.ManyToManyField(Exam, on_delete=models.CASCADE, blank=True)

class LikeCommentaryQuestion(Like):
    commentaries_questions = models.ManyToManyField(CommentaryQuestion, on_delete=models.CASCADE, blank=True)

class LikeCommentaryExam(Like):
    commentaries_exams = models.ManyToManyField(CommentaryExam, on_delete=models.CASCADE, blank=True)

class LikeCommentaryUniversity(Like):
    commentaries_universities = models.ManyToManyField(CommentaryUniversity, on_delete=models.CASCADE, blank=True)

class LikeCommentaryBook(Like):
    commentaries_books = models.ManyToManyField(CommentaryBook, on_delete=models.CASCADE, blank=True)
    
class LikeBook(Like):
    books = models.ManyToManyField(Book, on_delete=models.CASCADE, blank=True)

class LikeUniversity(Like):
    universities = models.ManyToManyField(University, on_delete=models.CASCADE, blank=True)


class UniversityStudent(models.Model):
    university = models.OneToOneField(University, on_delete=models.PROTECT, blank=True)
    student = models.ManyToManyField(Student, on_delete=models.CASCADE, blank=True)

class UniversityTeacher(models.Model):
    university = models.OneToOneField(University, on_delete=models.PROTECT, blank=True)
    teachers = models.ManyToManyField(University, on_delete=models.CASCADE, blank=True)


# report