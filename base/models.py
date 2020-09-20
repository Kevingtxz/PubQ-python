from django.db import models
from django.contrib.auth.models import User

# only for PostgreSQL
# from django.contrib.postgres.fields import ArrayField


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

    def __str__(self):
        return self.firstname


# Create UserPermition poster and teacher if asked;
# OneToOne: Address;
class University(models.Model):
    data_created = models.DateTimeField(auto_now_add=True, null=True)

    name = models.CharField(max_length=200)
    initials = models.CharField(max_length=5, blank= True)

    def __str__(self):
        return self.name


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

class Address(models.Model):
    neighborhood = models.CharField(max_length=200)
    number = models.CharField(max_length=20, blank=True)
    complement = models.CharField(max_length=200, blank=True)
    city = models.ForeignKey(City, on_delete=models.PROTECT)

# ManyToOne: City;
class AddressUser(Address):
    standard_user = models.IntegerField(StandardUser, primary_key=True)

class AddressUniversity(Address):
    university = models.IntegerField(University, primary_key=True)


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
    date_created = models.DateTimeField(auto_now_add=True, null=True)

# cut title after tests
    title = models.CharField(max_length=200)    

    text = models.CharField (max_length=5000)
    right_answear = models.CharField(max_length=1, blank= True)
    note = models.CharField(max_length=300, blank=True, null=True)
    teacher_name = models.CharField(max_length=300)
    university = models.ForeignKey(University, blank=True, null=True, on_delete=models.SET_NULL)
    subject = models.ForeignKey(Subject, blank=True, null=True, on_delete=models.SET_NULL)

    # only for PostgreSQL;
    # answears = ArrayField(ArrayField(models.TextField(blank=True)))

    def __str__(self):
        return self.title


# OneToOne: Teacher, StandardUser; OneToMany: Question;
class Book(models.Model):
    data_created = models.DateTimeField(auto_now_add=True, null=True)
    
    name = models.CharField(max_length=100)
    note = models.CharField(max_length=400, blank=True, null=True)
    questions = models.ManyToManyField(Question, blank=True)

    def __str__(self):
        return self.name


# # Abstract class for making clean code;
# class Commentary(models.Model):
#     data_created = models.DateTimeField(auto_now_add=True, null=True)
    
#     text = models.TextField

#     class Meta:
#         abstract = True

# # ManyToOne: Question;
# class CommentaryQuestion(Commentary):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)

# # class to manage commentaries;
# class Commentaries(models.Model):
#     standard_user = models.IntegerField(StandardUser, primary_key=True)
#     commentaries_questions = models.ManyToManyField(CommentaryQuestion, blank=True)


# # Create Likes with StandardUser
# # Abstract class : clean code;
# class Likes(models.Model):
#     standard_user = models.IntegerField(StandardUser, primary_key=True)
#     questions = models.ManyToManyField(Question, blank=True)
#     commentaries_questions = models.ManyToManyField(CommentaryQuestion, blank=True)
#     books = models.ManyToManyField(Book, blank=True)
#     universities = models.ManyToManyField(University, blank=True)


# class Report(models.Model):
#     data_created = models.DateTimeField(auto_now_add=True, null=True)

#     note = models.TextField

#     class Meta:
#         abstract = True

# # ManyToOne: Question;
# class ReportQuestion(Report):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)

# # ManyToOne: CommentaryQuestion;
# class ReportCommentaryQuestion(Report):
#     commentary_question = models.ForeignKey(CommentaryQuestion, on_delete=models.CASCADE)

# # ManyToOne: Book;
# class ReportBook(Report):
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)

# # ManyToOne: University;
# class ReportUniversity(Report):
#     university = models.ForeignKey(University, on_delete=models.CASCADE)

# # Create Likes with StandardUser
# # OneToOne: StandardUser, Teacher; OneToMany: ReportQuestion, ReportCommentaryQuestion, ReportBook, ReportUniversity;
# class reports(models.Model):
#     standard_user = models.IntegerField(StandardUser, primary_key=True)
#     reporter = models.ForeignKey(StandardUser, blank=True, on_delete=models.CASCADE)
#     commentaries_questions = models.ManyToManyField(ReportCommentaryQuestion, blank=True)
#     questions = models.ManyToManyField(ReportQuestion, blank=True)
#     books = models.ManyToManyField(ReportBook, blank=True)
#     universities = models.ManyToManyField(ReportUniversity, blank=True)


# Create UserPermition members to start a group  
# # OneToMany: UserPermition;
# class Group(models.Model):
#     data_created = models.DateTimeField(auto_now_add=True, null=True)


# USERTYPE = [('S', 'Student'),
#             ('T', 'Teacher')]

# PERMISSION = [('A','Admin'), 
#               ('M','Member'),
#               ('O', 'Owner')]

# # ManyToOne: University, Group, StandardUser, Group, Question;
# class UserPermition(models.Model):
#     user_type = models.CharField(max_length=1, choices=USERTYPE)
#     permission = models.CharField(max_length=1, choices=PERMISSION)
#     university = models.ForeignKey(University, blank=True, null=True, on_delete=models.CASCADE)
#     group = models.ForeignKey(Group, blank= True, on_delete=models.CASCADE)
#     question = models.ForeignKey(Question, blank= True, on_delete=models.CASCADE)


# Chat

# models.Manager