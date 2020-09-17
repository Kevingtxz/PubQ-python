from django.db import models
from django.contrib.auth.models import User
# only for PostgreSQL
# from django.contrib.postgres.fields import ArrayField

# models.Manager

# OneToMany: City;
class State(models.Model):
    initials = models.CharField(max_length=2)

    def __str__(self):
        return self.initials

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

# OneToOne: Address, Student, Teacher; 
class StandardUser(models.Model):
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
    university = models.ForeignKey('University', on_delete=models.SET_NULL, null= True, blank= True)
    questions = models.ManyToManyField('Question', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        abstract = True

# OneToOne: Address;
class University(models.Model):
    name = models.CharField(max_length=200)
    data_created = models.DateTimeField(auto_now_add=True, null=True)
    initials = models.CharField(max_length=5, blank= True)

    address = models.OneToOneField(Address, on_delete=models.PROTECT)
    teachers_students = models.OneToOneField('UniversityTeacherStudent', null= True, blank= True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# OneToOne: StandardUser, University;
class Student(StandardUser):
    book = models.OneToOneField('Book', blank=True, null=True, on_delete=models.CASCADE)
    question_right = models.ManyToManyField('Question', blank=True, on_delete=models.CASCADE)

# OneToOne: StandardUser, University;
class Teacher(StandardUser):
    pass

# Abstract class for making clean code
class baseExamQuestion(models.Model):
    teacher_name = models.CharField(max_length=300, blank=True, null=True)
    note = models.CharField(max_length=300, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    teacher_owner = models.OneToOneField(Teacher, blank=True, null=True, on_delete=models.PROTECT)
    university = models.ForeignKey(University, blank=True, null=True, on_delete=models.PROTECT)
    subject = models.ForeignKey('Subject', blank=True, null=True, on_delete=models.SET_NULL)
    poster_student = models.ForeignKey(Student, null=True, blank=True, on_delete=models.PROTECT)

    class Meta:
        abstract = True

# ManyToOne: Teacher, University;
class Exam(baseExamQuestion):
    questions = models.ManyToManyField('Question', on_delete=models.CASCADE, null=True, blank=True)

# ManyToOne: Exam; OneToOne: Teacher, University;
class Question(baseExamQuestion):
    text = models.TextField(blank= True)
    right_answear = models.CharField(max_length=1, blank= True)
    # only for PostgreSQL
    # answears = ArrayField(ArrayField(models.TextField(null=True, blank=True)))

    exam = models.ForeignKey(Exam, blank=True, on_delete=models.CASCADE, null=True)


# ManyToOne: Discipline; OneToMany: Question, Exam;
class Subject(models.Model):
    name = models.CharField(max_length=100)
    
    question = models.ManyToManyField(Question, on_delete=models.CASCADE)
    discipline = models.ForeignKey('Discipline', null= True, blank= True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

# OneToMany: Subject;
class Discipline(models.Model):
    name = models.CharField(max_length=100)

    subject = models.ManyToManyField(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# OneToOne: StandardUser; OneToMany: Question, Exam;
class Book(models.Model):
    name = models.CharField(max_length=100)
    note = models.CharField(max_length=400)

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    questions = models.ManyToManyField(Question, blank=True, on_delete=models.CASCADE)
    exams = models.ManyToManyField(Exam, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Abstract class for making clean code
class Commentary(models.Model):
    text = models.TextField
    class Meta:
        abstract = True

# ManyToOne: Question, StandardUser;;
class CommentaryQuestion(Commentary):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

# ManyToOne: Exam, StandardUser;;
class CommentaryExam(Commentary):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)

# ManyToOne: Book, StandardUser;;
class CommentaryBook(Commentary):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

# ManyToOne: University, StandardUser;;
class CommentaryUniversity(Commentary):
    university = models.ForeignKey(University, on_delete=models.CASCADE)

# class to manage commentaries
class Commentaries(models.Model):
    standard_user = models.ForeignKey(StandardUser, on_delete=models.PROTECT)
    commentary_question = models.ManyToManyField(CommentaryQuestion, blank=True, null=True, on_delete=models.CASCADE)
    commentary_exam = models.ManyToManyField(CommentaryExam, blank=True, null=True, on_delete=models.CASCADE)
    commentary_book = models.ManyToManyField(CommentaryBook, blank=True, null=True, on_delete=models.CASCADE)
    commentary_university = models.ManyToManyField(CommentaryUniversity, blank=True, null=True, on_delete=models.CASCADE)


# ManyToOne: Question, StandardUser;
class LikeQuestion(models.Model):
    questions = models.ManyToManyField(Question, on_delete=models.CASCADE, blank=True)

# ManyToOne: Exam, StandardUser;
class LikeExam(models.Model):
    exams = models.ManyToManyField(Exam, on_delete=models.CASCADE, blank=True)

# ManyToOne: Commentary, StandardUser;
class LikeCommentary(models.Model):
    commentaries = models.ManyToManyField(Commentary, on_delete=models.CASCADE, blank=True)

# ManyToOne: Book, StandardUser;
class LikeBook(models.Model):
    books = models.ManyToManyField(Book, on_delete=models.CASCADE, blank=True)

# ManyToOne: University, StandardUser;
class LikeUniversity(models.Model):
    universities = models.ManyToManyField(University, on_delete=models.CASCADE, blank=True)

# class to manage likes
class Likes(models.Model):
    standard_user = models.ForeignKey(StandardUser, on_delete=models.CASCADE)
    like_question = models.ForeignKey(LikeQuestion, blank=True, null=True, on_delete=models.CASCADE)
    like_question = models.ForeignKey(LikeQuestion, blank=True, null=True, on_delete=models.CASCADE)
    like_commentary = models.ForeignKey(LikeCommentary, blank=True, null=True, on_delete=models.CASCADE)
    like_book = models.ForeignKey(LikeBook, blank=True, null=True, on_delete=models.CASCADE)


# OneToOne: University; OneToMany: Teacher, Student;
class UniversityTeacherStudent(models.Model):
    university = models.OneToOneField(University, on_delete=models.PROTECT, blank=True)
    teachers = models.ManyToManyField(University, on_delete=models.CASCADE, blank=True)
    student = models.ManyToManyField(Student, on_delete=models.CASCADE, blank=True)

class UniversityExamQuestion(models.Model):
    university = models.OneToOneField(University, on_delete=models.PROTECT, blank=True)

    questions = models.ManyToManyField(Question, on_delete=models.PROTECT, blank=True, null=True)
    exams = models.ManyToManyField(Exam, on_delete=models.PROTECT, blank=True, null=True)



# Reports

# Groups

# Chat