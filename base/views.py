from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# from django.forms import inlineformset_factory
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout       
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .decorators import unauthenticated_user, allowed_users, admin_only
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





@login_required(login_url='login')
def questions(request):
	questions = Question.objects.all()
	paginator = Paginator(questions, 5)
	page = request.GET.get('page')
	try:
		questions = paginator.page(page)
	except PageNotAnInteger:
		questions = paginator.page(1)
	except EmptyPage:
		questions = paginator.page(paginator.num_pages)
	context = {'page':page, 'questions':questions,}
	return render(request, 'base/questions.html', context)


@login_required(login_url='login')
def postquestion(request):
	form = QuestionForm()
	if request.method == 'POST':
		print('Printing POST:', request.POST)
		form = QuestionForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	context = {'form':form,}
	return render(request, 'base/postquestion.html', context)




@login_required(login_url='login')
def universities(request):
	universities = University.objects.all()
	paginator = Paginator(universities, 5)
	page = request.GET.get('page')
	try:
		universities = paginator.page(page)
	except PageNotAnInteger:
		universities = paginator.page(1)
	except EmptyPage:
		universities = paginator.page(paginator.num_pages)

	context = {'page':page, 'universities':universities,}
	return render(request, 'base/universities.html', context)









@login_required(login_url='login')
def books(request):
	books = Book.objects.all()
	paginator = Paginator(books, 5)
	page = request.GET.get('page')
	try:
		books = paginator.page(page)
	except PageNotAnInteger:
		books = paginator.page(1)
	except EmptyPage:
		books = paginator.page(paginator.num_pages)
		
	context = {'page':page, 'books':books,}
	return render(request, 'base/books.html', context)

@login_required(login_url='login')
def postbook(request):
	form = BookForm()
	if request.method == 'POST':
		print('Printing POST:', request.POST)
		form = BookForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	context = {'form':form,}
	return render(request, 'base/postbook.html', context)





@admin_only
def reports(request):
	context = {}
	return render(request, 'base/reports.html', context)	

@login_required(login_url='login')
def postreport(request):
	form = ReportForm()
	if request.method == 'POST':
		print('Printing POST:', request.POST)
		form = ReportForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	context = {'form':form,}
	return render(request, 'base/postreport.html', context)	





@login_required(login_url='login')
def notifications(request):
    return render(request, 'base/notifications.html')


@login_required(login_url='login')
def account_settings(request):
    return render(request, 'base/account_settings.html')


@login_required(login_url='login')
def support(request):
    return render(request, 'base/support.html')


@login_required(login_url='login')
def aboutus(request):
    return render(request, 'base/aboutus.html')


# Um professor posta uma prova e ganha créditos
# créditos para baixar as provas de outros professores