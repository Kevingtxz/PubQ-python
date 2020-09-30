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

class Address(models.Model):
    neighborhood = models.CharField(max_length=200)
    number = models.CharField(max_length=20, blank=True, null=True)
    complement = models.CharField(max_length=200, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.PROTECT)

    def __str__(self):
        return self.neighborhood
    





SEX = [('M', 'Male'),
       ('F', 'Female'),
       ('O', 'Other'),]

COLORS = [('W', 'White'),
          ('B', 'Black'),
          ('G', 'Grey'),]

# OneToOne: Address, Student, Teacher, University; 
class StandardUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    profile_pic = models.ImageField(default='profile1.png', blank=True, null=True)
    
    nickname = models.CharField(max_length=200, blank=True, null=True)
    firstname = models.CharField(max_length=100, blank=True, null=True)
    lastname = models.CharField(max_length=200, blank=True, null=True)
    birth = models.CharField(max_length=8, blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True)
    education = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=1, choices=COLORS, default='W', blank=True)


    addresses = models.ManyToManyField(Address, blank=True)
    notifications = models.ManyToManyField('Notification', blank=True)





class Report(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    note = models.CharField(max_length=2000)

    standarduser = models.ForeignKey(StandardUser, on_delete=models.CASCADE)





# Create UserPermission poster and teacher if asked;
# OneToOne: Address;
class University(models.Model):
    profile_pic = models.ImageField(default='profile1.png', null=True, blank=True)  
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    name = models.CharField(max_length=200)
    initials = models.CharField(max_length=10)

    addresses = models.ManyToManyField(Address, blank=True)
    reports = models.ManyToManyField(Report, blank=True)
    questions = models.ManyToManyField('Question', blank=True)

    def __str__(self):
        return self.initials





    
# ManyToOne: Discipline; OneToMany: Question;
class Subject(models.Model):
    name = models.CharField(max_length=100)
    discipline_name = models.CharField(max_length=100)

    reports = models.ManyToManyField(Report, blank=True)

    def __str__(self):
        return self.name

# OneToMany: Subject;
class Discipline(models.Model):
    name = models.CharField(max_length=100)

    subjects = models.ManyToManyField(Subject, blank=True)

    def __str__(self):
        return self.name






EDUCATIONS = [('M', 'Master'),
              ('H', "High School"),
              ('P', 'Phd'),
              ('D', "Degree"),
              ('T', 'Tecnical'),
              ('F', "Fundamental"),]

ANSWEARS = [('A', 'a'), ('B', 'b'), ('C', 'c'), ('D', 'd'), ('E', 'e'), ]

# ManyToOne: StandardUser;
class Answear(models.Model):
    standarduser = models.ForeignKey(StandardUser, on_delete=models.CASCADE)
    text = models.CharField(max_length=5000)
    is_public = models.BooleanField(default=True, blank=True)

    reports = models.ManyToManyField(Report, blank=True)

# ManyToOne: OneToOne: Teacher, University;
class Question(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    text = models.CharField (max_length=10000)
    teacher_name = models.CharField(max_length=200)
    university_name = models.CharField(max_length=200, blank=True, null=True)
    education_Level = models.CharField(max_length=1, choices=EDUCATIONS)
    answear = models.CharField(max_length=5000, blank=True, null=True)
    is_public = models.BooleanField(default=True, blank=True)
    wrong_answears_count = models.IntegerField(default=0, blank=True)
    pic_1 = models.ImageField(blank=True, null=True)
    pic_2 = models.ImageField(blank=True, null=True)

    exam = models.ForeignKey('Exam', on_delete=models.CASCADE, null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True)
    answears = models.ManyToManyField(Answear, blank=True)
    reports = models.ManyToManyField(Report, blank=True)







class Exam(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    teacher_name = models.CharField(max_length=200)
    education_Level = models.CharField(max_length=1, choices=EDUCATIONS)
    university_name = models.CharField(max_length=200, blank=True, null=True)
    wrong_answears_count = models.IntegerField(default=0, blank=True)
    is_public = models.BooleanField(default=True, blank=True)
    pic_1 = models.ImageField(blank=True, null=True)
    pic_2 = models.ImageField(blank=True, null=True)
    pic_3 = models.ImageField(blank=True, null=True)
    pic_4 = models.ImageField(blank=True, null=True)
    pic_5 = models.ImageField(blank=True, null=True)
    
    subjects = models.ManyToManyField(Subject, blank=True)  
    reports = models.ManyToManyField(Report, blank=True)

    def __str__(self):
        return self.teacher_name









# OneToOne: Teacher, StandardUser; OneToMany: Question;
class Book(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    title = models.CharField(max_length=100)
    is_public = models.BooleanField(default=True, blank=True)
    note = models.CharField(max_length=400, blank=True, null=True)

    questions = models.ManyToManyField(Question, blank=True)
    subject = models.ManyToManyField(Subject, blank=True)
    reports = models.ManyToManyField(Report, blank=True)

    def __str__(self):
        return self.title







# ManyToMany: 
class Commentary(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    text = models.CharField(max_length=2000)
    is_public = models.BooleanField(default=True, blank=True)

    standarduser = models.ForeignKey(StandardUser, on_delete=models.CASCADE)
    reports = models.ManyToManyField(Report, blank=True)
    
    class Meta:
        abstract = True
    
class CommentaryQuestion(Commentary):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

class CommentaryBook(Commentary):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

class CommentaryAnswear(Commentary):
    answear = models.ForeignKey(Answear, on_delete=models.CASCADE)

class CommentaryUniversity(Commentary):
    university = models.ForeignKey(University, on_delete=models.CASCADE)






PERMISSION = [('S', 'Student'),
              ('T', 'Teacher'),
              ('P', 'Poster'),
              ('O', 'Owner'),]

# ManyToOne: University, Group, StandardUser, Group, Question;
class UserPermission(models.Model):
    standarduser = models.ForeignKey(StandardUser, on_delete=models.PROTECT)
    permission = models.CharField(max_length=1, choices=PERMISSION)
    
    class Meta:
        abstract = True


class UserPermissionQuestion(UserPermission):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

class UserPermissionBook(UserPermission):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

class UserPermissionAnswear(UserPermission):
    answear = models.ForeignKey(Answear, on_delete=models.CASCADE)

class UserPermissionUniversity(UserPermission):
    university = models.ForeignKey(University, on_delete=models.CASCADE)








# ManyToOne: StandardUser, Question, Answear, Book, University, Report;
class Notification(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    not_pic = models.ImageField(default='notification.png', blank=True)
    message = models.CharField(max_length=1000, blank=True, null=True)

    reports = models.ManyToManyField(Report, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, blank=True, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null=True)
    answear = models.ForeignKey(Answear, on_delete=models.CASCADE, blank=True, null=True)
    university = models.ForeignKey(University, on_delete=models.CASCADE, blank=True, null=True)
    commentary_question = models.ForeignKey(CommentaryQuestion, on_delete=models.CASCADE, blank=True, null=True)
    commentary_book = models.ForeignKey(CommentaryBook, on_delete=models.CASCADE, blank=True, null=True)
    commentary_answear = models.ForeignKey(CommentaryAnswear, on_delete=models.CASCADE, blank=True, null=True)
    commentary_university = models.ForeignKey(CommentaryUniversity, on_delete=models.CASCADE, blank=True, null=True)






# OneToMany:
class LikeDeslike(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    standarduser = models.ForeignKey(StandardUser, on_delete=models.CASCADE)
    
    class Meta:
        abstract = True
    


class LikeCommentaryQuestion(LikeDeslike):
    commentary = models.ForeignKey(CommentaryQuestion, on_delete=models.CASCADE)
    
class LikeCommentaryBook(LikeDeslike):
    commentary = models.ForeignKey(CommentaryBook, on_delete=models.CASCADE)
    
class LikeCommentaryAnswear(LikeDeslike):
    commentary = models.ForeignKey(CommentaryAnswear, on_delete=models.CASCADE)
    
class LikeCommentaryUniversity(LikeDeslike):
    commentary = models.ForeignKey(CommentaryUniversity, on_delete=models.CASCADE)

class LikeUniversity(LikeDeslike):
    university = models.ForeignKey(University, on_delete=models.CASCADE)

class LikeAnswear(LikeDeslike):
    answear = models.ForeignKey(Answear, on_delete=models.CASCADE)

class LikeBook(LikeDeslike):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    
class LikeNotification(LikeDeslike):
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE)






class DeslikeCommentaryQuestion(LikeDeslike):
    commentary = models.ForeignKey(CommentaryQuestion, on_delete=models.CASCADE)
    
class DeslikeCommentaryBook(LikeDeslike):
    commentary = models.ForeignKey(CommentaryBook, on_delete=models.CASCADE)
    
class DeslikeCommentaryAnswear(LikeDeslike):
    commentary = models.ForeignKey(CommentaryAnswear, on_delete=models.CASCADE)
    
class DeslikeCommentaryUniversity(LikeDeslike):
    commentary = models.ForeignKey(CommentaryUniversity, on_delete=models.CASCADE)

class DeslikeUniversity(LikeDeslike):
    university = models.ForeignKey(University, on_delete=models.CASCADE)

class DeslikeAnswear(LikeDeslike):
    answear = models.ForeignKey(Answear, on_delete=models.CASCADE)

class DeslikeBook(LikeDeslike):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    
class DeslikeNotification(LikeDeslike):
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE)






# ManyToOne: StandardUser;
class Requisition(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    about = models.CharField(max_length=200, blank=True, null=True)
    text = models.TextField

    standarduser = models.ForeignKey(StandardUser, on_delete=models.CASCADE, blank=True)