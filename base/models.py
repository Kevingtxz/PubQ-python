from django.db import models
from django.contrib.auth.models import User
# only for PostgreSQL
# from django.contrib.postgres.fields import ArrayField
# models.Manager






# OneToMany:
class Like(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)

# OneToMany:
class Deslike(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)






class Report(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    note = models.CharField(max_length=2000)





# ManyToMany: 
class Commentary(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    text = models.CharField(max_length=2000)
    like_count = models.IntegerField(default=0)
    deslike_count = models.IntegerField(default=0)

    likes = models.ManyToManyField(Like, blank=True)
    deslikes = models.ManyToManyField(Deslike, blank=True)
    reports = models.ManyToManyField(Report, blank=True)
    standard_user = models.ForeignKey('StandardUser', on_delete=models.CASCADE)






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
        return self.neighborhood
    





SEX = [('M', 'Male'),
       ('F', 'Female'),
       ('O', 'Other'),]

ACCOUNT_TYPE = [('S', 'Student'),
                ('T', 'Teacher'),]

# OneToOne: Address, Student, Teacher, University; 
class StandardUser(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    profile_pic = models.ImageField(default='profile1.png', null=True, blank=True)
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    
    account_type = models.CharField(max_length=1, choices=ACCOUNT_TYPE)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=200)
    nickname = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=11, blank= True)
    email = models.CharField(max_length=200)
    sex = models.CharField(max_length=1, blank= True)
    birth = models.CharField(max_length=8)

    addresses = models.ManyToManyField(Address, blank=True)
    reports = models.ManyToManyField(Report, blank=True)
    notifications = models.ManyToManyField('Notification', blank=True)

    def __str__(self):
        return self.nickname

PERMISSION = [('S', 'Student'),
              ('T', 'Teacher'),
              ('P', 'Poster'),
              ('O', 'Owner'),]

# ManyToOne: University, Group, StandardUser, Group, Question;
class UserPermission(models.Model):
    standard_user = models.ForeignKey(StandardUser, on_delete=models.CASCADE)
    permission = models.CharField(max_length=1, choices=PERMISSION)






# Create UserPermition poster and teacher if asked;
# OneToOne: Address;
class University(models.Model):
    profile_pic = models.ImageField(default='profile1.png', null=True, blank=True)  
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    name = models.CharField(max_length=200)
    initials = models.CharField(max_length=10)
    like_count = models.IntegerField(default=0, blank=True)
    deslike_count = models.IntegerField(default=0, blank=True)

    addresses = models.ManyToManyField(Address, blank=True)
    users = models.ManyToManyField(UserPermission, blank=True) 
    commentaries = models.ManyToManyField(Commentary, blank=True)
    likes = models.ManyToManyField(Like, blank=True)
    deslikes = models.ManyToManyField(Deslike, blank=True)
    reports = models.ManyToManyField(Report, blank=True)

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
    reports = models.ManyToManyField(Report, blank=True)

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
    like_count = models.IntegerField(default=0, blank=True)
    deslike_count = models.IntegerField(default=0, blank=True)

    commentaries = models.ManyToManyField(Commentary, blank=True)
    likes = models.ManyToManyField(Like, blank=True)
    deslikes = models.ManyToManyField(Deslike, blank=True)
    reports = models.ManyToManyField(Report, blank=True)

# ManyToOne: OneToOne: Teacher, University;
class Question(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    text = models.CharField (max_length=10000)
    right_answear = models.CharField(max_length=1, choices=ANSWEARS)
    education_Level = models.CharField(max_length=1, choices=EDUCATIONS)
    teacher_name = models.CharField(max_length=200)
    university_name = models.CharField(max_length=200)
    wrong_answears_count = models.IntegerField(default=0, blank=True, null=True)
    answears_count = models.IntegerField(default=0, blank=True, null=True)
    like_count = models.IntegerField(default=0, blank=True)
    deslike_count = models.IntegerField(default=0, blank=True)

    university = models.ForeignKey(University, blank=True, null=True, on_delete=models.SET_NULL)
    subject = models.ForeignKey(Subject, blank=True, null=True, on_delete=models.SET_NULL)
    discipline = models.ForeignKey(Discipline, blank=True, null=True, on_delete=models.SET_NULL)
    users = models.ManyToManyField(UserPermission, blank=True)
    answears = models.ManyToManyField(Answear, blank=True)
    commentaries = models.ManyToManyField(Commentary, blank=True)
    likes = models.ManyToManyField(Like, blank=True)
    deslikes = models.ManyToManyField(Deslike, blank=True)
    reports = models.ManyToManyField(Report, blank=True)







# OneToOne: Teacher, StandardUser; OneToMany: Question;
class Book(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    title = models.CharField(max_length=100)
    note = models.CharField(max_length=400, blank=True, null=True)
    like_count = models.IntegerField(default=0, blank=True)
    deslike_count = models.IntegerField(default=0, blank=True)

    questions = models.ManyToManyField(Question, blank=True)
    subject = models.ManyToManyField(Subject, blank=True)
    users = models.ManyToManyField(UserPermission, blank=True)
    commentaries = models.ManyToManyField(Commentary, blank=True)
    likes = models.ManyToManyField(Like, blank=True)
    deslikes = models.ManyToManyField(Deslike, blank=True)
    reports = models.ManyToManyField(Report, blank=True)


    def __str__(self):
        return self.title






# ManyToOne: StandardUser, Question, Answear, Book, University, Report;
class Notification(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    not_pic = models.ImageField(default='notification.png', null=True, blank=True)
    message = models.CharField(max_length=1000, blank=True, default='Hi, you have a notification.')

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    answear = models.ForeignKey(Answear, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    commentaries = models.ForeignKey(Commentary, on_delete=models.CASCADE)




# ManyToOne: StandardUser;
class Requisition(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    title = models.CharField(max_length=200)
    about = models.CharField(max_length=200)
    text = models.TextField

    standard_user = models.ForeignKey(StandardUser, on_delete=models.CASCADE)