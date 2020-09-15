from django.urls import path
from . import views

urlpatterns = [
    path('', views.questions, name='questions'),
    path('exams/', views.exams, name='exams'),
    path('postquestion/', views.postquestion, name='postquestion'),
    path('postexam/', views.postexam, name='postexam'),
    path('universities/', views.universities, name='universities'),
    path('support/', views.support, name='support'),
    path('aboutus/', views.aboutus, name='aboutus'),
]

# customer settings
# login pages