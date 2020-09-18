from django.db import models
from django.contrib.auth.models import User

# only for PostgreSQL
# from django.contrib.postgres.fields import ArrayField

# OneToMany: City;
class State(models.Model):
    initials = models.CharField(max_length=2)

# ManyToOne: State; OneToMany: Address;
class City(models.Model):
    name = models.CharField(max_length=100)

    state = models.ForeignKey(State, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

# ManyToOne: City; OneToOne: StandardUser;
class Address(models.Model):
    number = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=200)
    complement = models.CharField(max_length=200, null=True)

    city = models.ForeignKey(City, on_delete=models.PROTECT)


# OneToOne: Address;
class University(models.Model):
    data_created = models.DateTimeField(auto_now_add=True, null=True)
    name = models.CharField(max_length=200)
    initials = models.CharField(max_length=5, blank= True)

    address = models.OneToOneField(Address, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


# OneToOne: Address, Student, Teacher, University; 
class StandardUser(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    profile_pic = models.ImageField(default='profile1.png', null=True, blank=True)
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=200)
    phone = models.CharField(max_length=11, blank= True)
    email = models.CharField(max_length=200)
    sex = models.CharField(max_length=1, blank= True)
    birth = models.CharField(max_length=8)  

    address = models.OneToOneField(Address, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.firstname

# OneToOne: StandardUser;
class Student(models.Model):
    standard_user = models.OneToOneField(StandardUser, on_delete=models.CASCADE)

# OneToOne: StandardUser;
class Teacher(models.Model):
    standard_user = models.OneToOneField(StandardUser, on_delete=models.CASCADE)


# ManyToOne: Discipline; OneToMany: Question;
class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# OneToMany: Subject;
class Discipline(models.Model):
    name = models.CharField(max_length=100)

    subjects = models.ManyToManyField(Subject, blank=True)

    def __str__(self):
        return self.name


# ManyToOne: OneToOne: Teacher, University;
class Question(models.Model):
    teacher_name = models.CharField(max_length=300, blank=True, null=True)
    note = models.CharField(max_length=300, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    text = models.TextField(blank= True)
    right_answear = models.CharField(max_length=1, blank= True)

    poster = models.ForeignKey(StandardUser, on_delete=models.PROTECT)
    teacher_owner = models.ForeignKey(Teacher, blank=True, null= True, on_delete=models.PROTECT)
    university = models.ForeignKey(University, blank=True, null=True, on_delete=models.SET_NULL)
    subject = models.ForeignKey(Subject, blank=True, null=True, on_delete=models.SET_NULL)

    # only for PostgreSQL;
    # answears = ArrayField(ArrayField(models.TextField(blank=True)))


# OneToOne: Teacher, Student; OneToMany: Question;
class Book(models.Model):
    name = models.CharField(max_length=100)
    note = models.CharField(max_length=400, blank=True, null=True)
    data_created = models.DateTimeField(auto_now_add=True, null=True)

    standard_user = models.ForeignKey(StandardUser, on_delete=models.CASCADE)
    questions = models.ManyToManyField(Question, blank=True)

    def __str__(self):
        return self.name


# Abstract class for making clean code;
class Commentary(models.Model):
    text = models.TextField
    data_created = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:
        abstract = True

# ManyToOne: Question;
class CommentaryQuestion(Commentary):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

# class to manage commentaries;
class Commentaries(models.Model):
    standard_user = models.ForeignKey(StandardUser, blank=True, on_delete=models.CASCADE)
    commentaries_questions = models.ManyToManyField(CommentaryQuestion, blank=True)


# Abstract class : clean code;
class LikeDeslike(models.Model):
    standard_user = models.ForeignKey(StandardUser, blank=True, on_delete=models.CASCADE)
    questions = models.ManyToManyField(Question, blank=True)
    commentaries_questions = models.ManyToManyField(CommentaryQuestion, blank=True)
    # books = models.ManyToManyField(Book, blank=True)
    # universities = models.ManyToManyField(University, blank=True)

    class Meta:
        abstract = True

# class to manage likes;
class Likes(LikeDeslike):
    pass

# class to manage desliks;
class Deslikes(LikeDeslike):
    pass


# OneToOne: University; OneToMany: Teacher, Student;
class UniversityTeacherStudent(models.Model):
    university = models.OneToOneField(University, blank=True, on_delete=models.PROTECT)
    teachers = models.ManyToManyField(Teacher, blank=True)
    student = models.ManyToManyField(Student, blank=True)

class UniversityQuestion(models.Model):
    university = models.OneToOneField(University, on_delete=models.PROTECT, blank=True)

    questions = models.ManyToManyField(Question, blank=True)

class Report(models.Model):
    note = models.TextField
    data_created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        abstract = True

# ManyToOne: Question;
class ReportQuestion(Report):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

# ManyToOne: CommentaryQuestion;
class ReportCommentaryQuestion(Report):
    commentary_question = models.ForeignKey(CommentaryQuestion, on_delete=models.CASCADE)

# ManyToOne: Book;
class ReportBook(Report):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

# ManyToOne: University;
class ReportUniversity(Report):
    university = models.ForeignKey(University, on_delete=models.CASCADE)

# OneToOne: Student, Teacher; OneToMany: ReportQuestion, ReportCommentaryQuestion, ReportBook, ReportUniversity;
class reports(models.Model):
    reporter = models.ForeignKey(StandardUser, blank=True, on_delete=models.CASCADE)
    commentaries_questions = models.ManyToManyField(ReportCommentaryQuestion, blank=True)
    questions = models.ManyToManyField(ReportQuestion, blank=True)
    books = models.ManyToManyField(ReportBook, blank=True)
    universities = models.ManyToManyField(ReportUniversity, blank=True)


# OneToMany: Teacher, Student;
class Groups(models.Model):
    members = models.ManyToManyField(StandardUser, blank=True)


# Chat

# models.Manager