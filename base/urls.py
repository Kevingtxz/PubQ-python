from django.urls import path
from . import views

# use include;      model_detail;           app_name = 'public_exam;

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('', views.questions, name='questions'),
    path('question-post/', views.questionPost, name='question-post'),
    path('exams/', views.exams, name='exams'),
    path('exam-apply/', views.examApply, name='exam-apply'),
    path('exam-post/', views.examPost, name='exam-post'),
    path('notifications/', views.notifications, name='notifications'),
    path('account-settings/', views.account_settings, name='account-settings'),
    path('support/', views.support, name='support'),
    path('info/', views.info, name='info'),
    path('report-post/', views.reportPost, name='report-post'),
    path('questions-user/', views.questionsUser, name='questions-user'),
    path('exams-user/', views.examsUser, name='exams-user'),
]

# customer settings
# login pages
