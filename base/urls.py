from django.urls import path
from . import views

# use include;      model_detail;           app_name = 'public_exam;         

urlpatterns = [
	path('register/', views.registerPage, name='register'),
	path('login/', views.loginPage, name='login'),  
	path('logout/', views.logoutUser, name="logout"),  

    path('', views.questions, name='questions'),
    path('postquestion/', views.postquestion, name='postquestion'),
    path('universities/', views.universities, name='universities'),
    path('books', views.books, name='books'),
    path('notifications/', views.notifications, name='notifications'),
    path('account_settings', views.account_settings, name='account_settings'),
    path('support/', views.support, name='support'),
    path('aboutus/', views.aboutus, name='aboutus'),
]

# customer settings
# login pages