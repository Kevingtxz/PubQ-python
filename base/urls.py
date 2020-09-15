from django.urls import path
from . import views

urlpatterns = [
    path('', views.questions, name='questions'),
    path('support/', views.support, name='support'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('universities/', views.universities, name='universities'),
]



# search view universities

# suport

# about us

# customer settings

# login pages
