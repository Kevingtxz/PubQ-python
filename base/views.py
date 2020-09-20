from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout       
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .decorators import unauthenticated_user
from .forms import *
from .models import *

# from django.views import generic
# ListView; DetailView; FormView; DeleteView; UpdateView...@unauthenticated_user

@unauthenticated_user
def registerPage(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, 'Account was created for ' + username)

			return redirect('login')

	context = {'form':form}
	return render(request, 'base/register.html', context)

@unauthenticated_user
def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'base/login.html', context)
    
def logoutUser(request):
	logout(request)
	return redirect('login')


def questions(request):
    # questions = Question.objects.values('text', 'answears')
    return render(request, 'base/questions.html')

def exams(request):
    return render(request, 'base/exams.html')

def postexam(request):
    return render(request, 'base/postexam.html')

def postquestion(request):
    return render(request, 'base/postquestion.html')

def support(request):
    return render(request, 'base/support.html')

def aboutus(request):
    return render(request, 'base/aboutus.html')

def universities(request):
    return render(request, 'base/universities.html')


# Um professor posta uma prova e ganha créditos
# créditos para baixar as provas de outros professores