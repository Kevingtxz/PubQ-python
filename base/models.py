from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


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
    book = models.OneToOneField('Book', blank=True, null=True, on_delete=models.CASCADE)
    performance = models.OneToOneField('Performance', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.firstname

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
class Student(models.Model):
    standardUser = models.OneToOneField(StandardUser, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.SET_NULL, null= True, blank= True)
    questions = models.ManyToManyField('Question', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.standardUser

# OneToOne: StandardUser, University;
class Teacher(models.Model):
    standardUser = models.OneToOneField(StandardUser, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.SET_NULL, null= True, blank=True)
    questions = models.ManyToManyField('Question', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.standardUser

# ManyToOne: Teacher, University;
class Exam(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    teacher_name = models.CharField(max_length=300, blank=True)
    notes = models.CharField(max_length=500, null=True, blank=True)

    university = models.ForeignKey(University, blank=True, on_delete=models.PROTECT)
    teacher_owner = models.ForeignKey(Teacher, blank=True, on_delete=models.PROTECT)
    questions = models.ManyToManyField('Question', blank=True, on_delete=models.PROTECT)


# ManyToOne: Exam; OneToOne: Teacher, University;
class Question(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    text = models.TextField(blank= True)
    right_answear = models.CharField(max_length=1, blank= True)
    answears = ArrayField(ArrayField(models.TextField(null=True, blank=True)))
    teacher_owner_name = models.CharField(max_length=200, blank=True, null=True)

    exam = models.ForeignKey(Exam, blank=True, on_delete=models.CASCADE, null=True)  
    poster = models.ForeignKey(Student, on_delete=models.PROTECT)
    teacher_owner = models.OneToOneField(Teacher, blank=True, null=True, on_delete=models.PROTECT)
    university = models.OneToOneField(University, blank=True, null=True, on_delete=models.PROTECT)
    subject = models.ForeignKey('Subject', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.text

# OneToOne: StandardUser; ManyToOne: Question;
class Performance(models.Model):
    standardUser = models.OneToOneField(StandardUser, on_delete=models.CASCADE, null=True, blank=True)
    question_right = models.ManyToManyField(Question, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.standardUser


# ManyToOne: Discipline; OneToMany: Question, Exam;
class Subject(models.Model):
    name = models.CharField(max_length=200)
    question = models.ManyToManyField(Question, on_delete=models.CASCADE)
    
    discipline = models.ForeignKey('Discipline', null= True, blank= True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

# OneToMany: Subject;
class Discipline(models.Model):
    name = models.CharField(max_length=200)
    subject = models.ManyToManyField(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# OneToOne: StandardUser; OneToMany: Question, Exam;
class Book(models.Model):
    name = models.CharField(max_length=200)
    note = models.CharField(max_length=500)

    standardUser = models.ForeignKey(StandardUser, on_delete=models.CASCADE)
    questions = models.ManyToManyField(Question, blank=True)
    exams = models.ManyToManyField(Exam,  blank=True)

    def __str__(self):
        return self.name


# ManyToOne: StandardUser;
class Commentary(models.Model):
    standardUser = models.ForeignKey(StandardUser, on_delete=models.PROTECT)
    text = ArrayField(ArrayField(models.TextField()))

    def __str__(self):
        return self.standardUser

# ManyToOne: Question;
class CommentaryQuestion(Commentary):
    questions = models.ManyToManyField(Question, on_delete=models.CASCADE)

# ManyToOne: Exam;
class CommentaryExam(Commentary):
    exams = models.ManyToManyField(Exam, on_delete=models.CASCADE)

# ManyToOne: Book;
class CommentaryBook(Commentary):
    books = models.ManyToManyField(Book, on_delete=models.CASCADE)

# ManyToOne: University;
class CommentaryUniversity(Commentary):
    universities = models.ManyToManyField(University, on_delete=models.CASCADE)


# ManyToOne: StandardUser;
class Like(models.Model):
    standardUser = models.ForeignKey(StandardUser, on_delete=models.CASCADE)

# ManyToOne: Question;
class LikeQuestion(Like):
    questions = models.ManyToManyField(Question, on_delete=models.CASCADE, blank=True)

# ManyToOne: Exam;
class LikeExam(Like):
    exams = models.ManyToManyField(Exam, on_delete=models.CASCADE, blank=True)

# ManyToOne: Comentary;
class LikeCommentary(Like):
    commentaries = models.ManyToManyField(Commentary, on_delete=models.CASCADE, blank=True)

# ManyToOne: Book;
class LikeBook(Like):
    books = models.ManyToManyField(Book, on_delete=models.CASCADE, blank=True)

# ManyToOne: University;
class LikeUniversity(Like):
    universities = models.ManyToManyField(University, on_delete=models.CASCADE, blank=True)


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