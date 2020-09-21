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
    number = models.CharField(max_length=20, blank=True)
    complement = models.CharField(max_length=200, blank=True)
    city = models.ForeignKey(City, on_delete=models.PROTECT)

    def __str__(self):
        return self.city.name
    





SEX = [('M', 'Male'),
       ('F', 'Female'),
       ('O', 'Other'),]


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
    addresses = models.ManyToManyField(Address)
    notifications = models.ManyToManyField('Notification')

    def __str__(self):
        return self.firstname

PERMISSION = [('A','Admin'),
              ('S','Student'),
              ('T','Teacher'),
              ('P', 'Poster'),
              ('O', 'Owner'),]

# ManyToOne: University, Group, StandardUser, Group, Question;
class UserPermission(models.Model):
    standard_user = models.ForeignKey(StandardUser, on_delete=models.CASCADE)
    permission = models.CharField(max_length=1, choices=PERMISSION)





class Report(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    note = models.CharField(max_length=2000)

    reporter = models.ForeignKey(StandardUser, on_delete=models.CASCADE)





# OneToMany:
class Like(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    standard_user = models.ForeignKey(StandardUser, on_delete=models.CASCADE)

# OneToMany:
class Deslike(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    standard_user = models.ForeignKey(StandardUser, on_delete=models.CASCADE)





# OneToMany: 
class Commentary(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    text = models.CharField(max_length=2000)

    standard_user = models.ForeignKey(StandardUser, on_delete=models.CASCADE)
    likes = models.ManyToManyField(Like)
    like_count = models.IntegerField(default=0)
    deslikes = models.ManyToManyField(Deslike)
    deslike_count = models.IntegerField(default=0)
    reports = models.ManyToManyField(Report)






# Create UserPermition poster and teacher if asked;
# OneToOne: Address;
class University(models.Model):
    profile_pic = models.ImageField(default='profile1.png', null=True, blank=True)  
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    name = models.CharField(max_length=200)
    initials = models.CharField(max_length=5, blank= True)
    addresses = models.ManyToManyField(Address)
    users = models.ManyToManyField(UserPermission) 
    commentaries = models.ManyToManyField(Commentary)
    likes = models.ManyToManyField(Like)
    like_count = models.IntegerField(default=0)
    deslikes = models.ManyToManyField(Deslike)
    deslike_count = models.IntegerField(default=0)
    reports = models.ManyToManyField(Report)

    def __str__(self):
        return self.initials





    
# ManyToOne: Discipline; OneToMany: Question;
class Subject(models.Model):
    name = models.CharField(max_length=100)
    reports = models.ManyToManyField(Report)

    def __str__(self):
        return self.name

# OneToMany: Subject;
class Discipline(models.Model):
    name = models.CharField(max_length=100)

    subjects = models.ManyToManyField(Subject)
    reports = models.ManyToManyField(Report)

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
    standard_user = models.ForeignKey(StandardUser, on_delete=models.CASCADE)
    text = models.CharField(max_length=10000)
    commentaries = models.ManyToManyField(Commentary)
    likes = models.ManyToManyField(Like)
    like_count = models.IntegerField(default=0)
    deslikes = models.ManyToManyField(Deslike)
    deslike_count = models.IntegerField(default=0)
    reports = models.ManyToManyField(Report)


# ManyToOne: OneToOne: Teacher, University;
class Question(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    text = models.CharField (max_length=5000)
    right_answear = models.CharField(max_length=1, choices=ANSWEARS)
    education_Level = models.CharField(max_length=1, choices=EDUCATIONS)
    teacher_name = models.CharField(max_length=300)
    university = models.ForeignKey(University, blank=True, null=True, on_delete=models.SET_NULL)
    subject = models.ForeignKey(Subject, null=True, on_delete=models.SET_NULL)
    users = models.ManyToManyField(UserPermission)
    wrong_answears_count = models.IntegerField(default=0)
    answears_count = models.IntegerField(default=0)
    answears = models.ManyToManyField(Answear)
    commentaries = models.ManyToManyField(Commentary)
    likes = models.ManyToManyField(Like)
    like_count = models.IntegerField(default=0)
    deslikes = models.ManyToManyField(Deslike)
    deslike_count = models.IntegerField(default=0)
    reports = models.ManyToManyField(Report)







# OneToOne: Teacher, StandardUser; OneToMany: Question;
class Book(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    title = models.CharField(max_length=100)
    note = models.CharField(max_length=400, blank=True, null=True)
    questions = models.ManyToManyField(Question)
    subject = models.ManyToManyField(Subject)
    users = models.ManyToManyField(UserPermission) 
    commentaries = models.ManyToManyField(Commentary)
    likes = models.ManyToManyField(Like)
    like_count = models.IntegerField(default=0)
    deslikes = models.ManyToManyField(Deslike)
    deslike_count = models.IntegerField(default=0)
    reports = models.ManyToManyField(Report)


    def __str__(self):
        return self.title






# OneToOne: StandardUser;
class ChatMessage(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    text = models.CharField(max_length=5000)

    standard_user = models.ForeignKey(StandardUser, on_delete=models.CASCADE)
    reports = models.ManyToManyField(Report)
    
class Chat(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)


    chat_pic = models.ImageField(default='chat.png', null=True, blank=True)
    title = models.CharField(max_length=200)

    messages = models.ManyToManyField(ChatMessage)
    users = models.ManyToManyField(UserPermission)
    reports = models.ManyToManyField(Report)





# ManyToOne: StandardUser, Question, Answear, Book, University, Report;
class Notification(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    not_pic = models.ImageField(default='notification.png', null=True, blank=True)
    message = models.CharField(max_length=1000)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    answear = models.ForeignKey(Answear, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    report = models.ForeignKey(Report, on_delete=models.CASCADE)




# ManyToOne: StandardUser;
class Requisition(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    title = models.CharField(max_length=200)
    about = models.CharField(max_length=200)
    text = models.TextField

    standard_user = models.ForeignKey(StandardUser, on_delete=models.CASCADE)