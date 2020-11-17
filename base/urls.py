from django.urls import path
from . import views

# use include;      model_detail;           app_name = 'public_exam;

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('', views.questions, name='questions'),
    path('postquestion/', views.postquestion, name='postquestion'),
    path('exams/', views.exams, name='exams'),
    path('applyexam/', views.applyexam, name='applyexam'),
    path('postexam/', views.postexam, name='postexam'),
    path('notifications/', views.notifications, name='notifications'),
    path('account_settings', views.account_settings, name='account_settings'),
    path('support/', views.support, name='support'),
    path('info/', views.info, name='info'),
    path('postreport/', views.postreport, name='postreport'),
    path('myquestions/', views.myquestions, name='myquestions'),
    path('myexams/', views.myexams, name='myexams'),
]

# customer settings
# login pages
