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
    like_count = models.IntegerField(default=0, blank=True, null=True)
    deslike_count = models.IntegerField(default=0, blank=True, null=True)
    is_public = models.BooleanField(default=True, blank=True, null=True)

    likes = models.ManyToManyField(Like, blank=True, null=True)
    deslikes = models.ManyToManyField(Deslike, blank=True, null=True)
    reports = models.ManyToManyField(Report, blank=True, null=True)
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
    color = models.CharField(max_length=1, choices=COLORS, default='W', blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True)
    education = models.CharField(max_length=100, blank=True, null=True)


    addresses = models.ManyToManyField(Address, blank=True)
    reports = models.ManyToManyField(Report, blank=True, null=True)
    notifications = models.ManyToManyField('Notification', blank=True, null=True)
    questions = models.ManyToManyField('Question', blank=True, null=True)


PERMISSION = [('S', 'Student'),
              ('T', 'Teacher'),
              ('P', 'Poster'),
              ('O', 'Owner'),]

# ManyToOne: University, Group, StandardUser, Group, Question;
class UserPermission(models.Model):
    standard_user = models.ForeignKey(StandardUser, on_delete=models.PROTECT)
    permission = models.CharField(max_length=1, choices=PERMISSION)





# Create UserPermission poster and teacher if asked;
# OneToOne: Address;
class University(models.Model):
    profile_pic = models.ImageField(default='profile1.png', null=True, blank=True)  
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    name = models.CharField(max_length=200)
    initials = models.CharField(max_length=10)
    like_count = models.IntegerField(default=0, blank=True, null=True)
    deslike_count = models.IntegerField(default=0, blank=True, null=True)

    addresses = models.ManyToManyField(Address, blank=True)
    users = models.ManyToManyField(UserPermission, blank=True) 
    comments = models.ManyToManyField(Commentary, blank=True, null=True)
    likes = models.ManyToManyField(Like, blank=True, null=True)
    deslikes = models.ManyToManyField(Deslike, blank=True, null=True)
    reports = models.ManyToManyField(Report, blank=True, null=True)
    questions = models.ManyToManyField('Question', blank=True, null=True)

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

    subjects = models.ManyToManyField(Subject, blank=True, null=True)

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
    text = models.CharField(max_length=5000)
    like_count = models.IntegerField(default=0, blank=True, null=True)
    deslike_count = models.IntegerField(default=0, blank=True, null=True)
    is_public = models.BooleanField(default=True, blank=True, null=True)

    likes = models.ManyToManyField(Like, blank=True, null=True)
    deslikes = models.ManyToManyField(Deslike, blank=True, null=True)
    reports = models.ManyToManyField(Report, blank=True, null=True)

# ManyToOne: OneToOne: Teacher, University;
class Question(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    text = models.CharField (max_length=10000)
    teacher_name = models.CharField(max_length=200)
    education_Level = models.CharField(max_length=1, choices=EDUCATIONS)
    is_public = models.BooleanField(default=True, blank=True, null=True)
    answear = models.CharField(max_length=5000, blank=True, null=True)
    university_name = models.CharField(max_length=200, blank=True, null=True)
    answears_count = models.IntegerField(default=0, blank=True, null=True)
    like_count = models.IntegerField(default=0, blank=True, null=True)
    deslike_count = models.IntegerField(default=0, blank=True, null=True)
    right_answear = models.CharField(max_length=1, choices=ANSWEARS, blank=True, null=True)
    wrong_answears_count = models.IntegerField(default=0, blank=True, null=True)
    pic_1 = models.ImageField(blank=True, null=True)
    pic_2 = models.ImageField(blank=True, null=True)

    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)  
    users = models.ManyToManyField(UserPermission, blank=True)
    answears = models.ManyToManyField(Answear, blank=True, null=True)
    comments = models.ManyToManyField(Commentary, blank=True, null=True)
    likes = models.ManyToManyField(Like, blank=True, null=True)
    deslikes = models.ManyToManyField(Deslike, blank=True, null=True)
    reports = models.ManyToManyField(Report, blank=True, null=True)






class Exam(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    teacher_name = models.CharField(max_length=200)
    education_Level = models.CharField(max_length=1, choices=EDUCATIONS)
    university_name = models.CharField(max_length=200, blank=True, null=True)
    like_count = models.IntegerField(default=0, blank=True, null=True)
    deslike_count = models.IntegerField(default=0, blank=True, null=True)
    right_answears_count = models.IntegerField(default=0, blank=True, null=True)
    wrong_answears_count = models.IntegerField(default=0, blank=True, null=True)
    is_public = models.BooleanField(default=True, blank=True, null=True)
    pic_1 = models.ImageField(blank=True, null=True)
    pic_2 = models.ImageField(blank=True, null=True)
    pic_3 = models.ImageField(blank=True, null=True)
    pic_4 = models.ImageField(blank=True, null=True)
    pic_5 = models.ImageField(blank=True, null=True)

    questions = models.ManyToManyField(Question, blank=True)
    users = models.ManyToManyField(UserPermission, blank=True)
    subject = models.ManyToManyField(Subject, blank=True, null=True)  
    comments = models.ManyToManyField(Commentary, blank=True, null=True)
    likes = models.ManyToManyField(Like, blank=True, null=True)
    deslikes = models.ManyToManyField(Deslike, blank=True, null=True)
    reports = models.ManyToManyField(Report, blank=True, null=True)









# OneToOne: Teacher, StandardUser; OneToMany: Question;
class Book(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    title = models.CharField(max_length=100)
    note = models.CharField(max_length=400, blank=True, null=True)
    like_count = models.IntegerField(default=0, blank=True, null=True)
    deslike_count = models.IntegerField(default=0, blank=True, null=True)
    is_public = models.BooleanField(default=True, blank=True, null=True)

    questions = models.ManyToManyField(Question, blank=True)
    subject = models.ManyToManyField(Subject, blank=True)
    users = models.ManyToManyField(UserPermission, blank=True)
    comments = models.ManyToManyField(Commentary, blank=True, null=True)
    likes = models.ManyToManyField(Like, blank=True, null=True)
    deslikes = models.ManyToManyField(Deslike, blank=True, null=True)
    reports = models.ManyToManyField(Report, blank=True, null=True)


    def __str__(self):
        return self.title






# ManyToOne: StandardUser, Question, Answear, Book, University, Report;
class Notification(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    not_pic = models.ImageField(default='notification.png', blank=True, null=True)
    message = models.CharField(max_length=1000, blank=True, null=True, default='Hi, see it')

    question = models.ForeignKey(Question, on_delete=models.CASCADE, blank=True, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null=True)
    answear = models.ForeignKey(Answear, on_delete=models.CASCADE, blank=True, null=True)
    university = models.ForeignKey(University, on_delete=models.CASCADE, blank=True, null=True)
    report = models.ForeignKey(Report, on_delete=models.CASCADE, blank=True, null=True)
    comments = models.ForeignKey(Commentary, on_delete=models.CASCADE, blank=True, null=True)




# ManyToOne: StandardUser;
class Requisition(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    title = models.CharField(max_length=200)
    about = models.CharField(max_length=200)
    text = models.TextField

    standard_user = models.ForeignKey(StandardUser, on_delete=models.CASCADE, blank=True)