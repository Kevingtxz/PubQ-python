from django.shortcuts import render, redirect

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

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
			return redirect('questions')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'base/login.html', context)
    
def logoutUser(request):
	logout(request)
	return redirect('login')


def questions(request):
	questions = Question.objects.all()
	paginator = Paginator(questions, 2)
	questions = Question.objects.values_list('text', 'education_Level', 'teacher_name', 'university', 'subject', 'right_answear')
	page = request.GET.get('page')
	try:
		questions = paginator.page(page)
	except PageNotAnInteger:
		questions = paginator.page(1)
	except EmptyPage:
		questions = paginator.page(paginator.num_pages)

	context = {'page':page, 'questions':questions}
	return render(request, 'base/questions.html', context)

def universities(request):
	universities = University.objects.all()
	context = {'universities':universities, 'addresses':addresses}
	return render(request, 'base/universities.html', context)

def postquestion(request):
    return render(request, 'base/postquestion.html')

def support(request):
    return render(request, 'base/support.html')

def aboutus(request):
    return render(request, 'base/aboutus.html')


# Um professor posta uma prova e ganha créditos
# créditos para baixar as provas de outros professores