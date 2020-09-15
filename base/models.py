from django.db import models


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=11, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default='profile1.png', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

# Create your models here.

#  I will create it in other place
#  User{
# 	nickname 						String
# 	password 						String
# 	date_created					Date	
# }



# State{
# 	Id								Integer
# 	name 							String
# }

# City{
# 	Id 								Integer
# 	name 							String

# 	State 							ManyToOne
# 	name 							String
# }

# Address{
# 	neighborhood 					String
	
# 	User 							OneToOne
# 	State							ManyToOne
# 	City							ManyToOne
# }

# Person{
# 	name 							String
# 	sex 							Char
# 	email 							String
# 	birth 							Date
# 	phone							String		null=True
# 	picture 						picture		null=True

# 	User 							OneToOne
# 	Address							ManyToOne
# }

# Student{
# 	Person 							OneToOne
# 	University						OneToOne	
# }

# Teacher{
# 	Person 							OneToOne
# 	University						OneToOne	
# }

# Performance{
# 	User 							OneToOne
# 	Question_wrong					OneToMany
# 	Question_right 					OneToMany
# }

# Exam{
# 	data created 					Date

# 	Dicipline 						OneToOne
# 	Subject 						OneToMany
# 	Question 						OneToMany
# 	University 						OneToMany
# 	Teacher 						OneToOne
# 	User - like 					ManyToMany
# 	User - deslike					ManyToMany
# }

# Question{
# 	description 					String
# 	aswears 						String
# 	right_aswear					Char

# 	Exam							ManyToOne
# 	User - poster					OneToOne 
# 	Commentary 						OneToMany
# 	User - like 					ManyToMany
# 	User - deslike					ManyToMany
# 	User - Wrong Answer 			ManyToMany
# 	User - Right Answer				ManyToMany
# }


# Book{	
# 	User							OneToOne
# 	Question						OneToMany
# 	Exams							ManyToMany
# 	Discipline						ManyToMany
# }

# Commentary{
# 	User 							OneToOne
# 	Question 			 			ManyToOne
# 	User - like 					ManyToMany
# 	User - deslike					ManyToMany
# }


# Subject{
# 	name 							String

# 	Discipline						ManyToOne
# }

# Discipline{
# 	name 							String

# 	Subject							OneToMany
# 	Exams 							OneToMany
# }

# University{ 
# 	name 							String
# 	initials 						String
# 	data created 					Date
	
# 	Students 						OneToMany
# 	Teachers 						OneToMany
# 	Address							OneToOne
# }
