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
from .filters import *


# from django.views import generic
# ListView; DetailView; FormView; DeleteView; UpdateView...@unauthenticated_user


@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            group = Group.objects.get(name="student")
            user.groups.add(group)
            StandardUser.objects.create(user=user)
            messages.success(request, "Account was created for " + username)

            return redirect("login")

    context = {"form": form}
    return render(request, "accounts/register.html", context)


@unauthenticated_user
def loginPage(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("questions")
        else:
            messages.info(request, "Username OR password is incorrect")

    context = {}
    return render(request, "base/login.html", context)


def logoutUser(request):
    logout(request)
    return redirect("login")


@login_required(login_url="login")
def questions(request):
    filter = QuestionFilter(
        request.GET, queryset=Question.objects.filter(is_public=True)
    )
    paginator = Paginator(filter.qs, 5)
    page = request.GET.get("page")
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)
    questions_num = len(questions)
    context = {
        "page": page,
        "questions": questions,
        "filter": filter,
        "questions_num": questions_num,
    }

    return render(request, "base/questions.html", context)


@login_required(login_url="login")
def questionPost(request):
    form = QuestionForm()
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {
        "form": form,
    }
    return render(request, "base/question-post.html", context)


@login_required(login_url="login")
def questionsUser(request):
    questions = set()
    for (
        permission_question
    ) in request.user.standarduser.userpermissionquestion_set.all():
        if permission_question.permission == "P":
            if permission_question.question != None:
                questions.add(permission_question.question)
    context = {
        "questions": questions,
    }
    return render(request, "base/my_questions.html", context)


@login_required(login_url="login")
def exams(request):
    exams = Exam.objects.filter(is_public=True)
    paginator = Paginator(exams, 6)
    page = request.GET.get("page")
    try:
        exams = paginator.page(page)
    except PageNotAnInteger:
        exams = paginator.page(1)
    except EmptyPage:
        exams = paginator.page(paginator.num_pages)
    context = {
        "page": page,
        "exams": exams,
    }
    return render(request, "base/exams.html", context)


@login_required(login_url="login")
def examPost(request):
    form = ExamForm()
    if request.method == "POST":
        form = ExamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {
        "form": form,
    }
    return render(request, "base/postexam.html", context)


@login_required(login_url="login")
def examsUser(request):
    exams = set()
    for permission_exam in request.user.standarduser.userpermissionexam_set.all():
        if permission_exam.permission == "P":
            if permission_exam.exam != None:
                exams.add(permission_exam.exam)
    context = {
        "exams": exams,
    }
    return render(request, "base/myexams.html", context)


# I should require that only teachers apply exams
@login_required(login_url="login")
def examApply(request):
    form = TimeToApplyExamForm
    context = {
        "form": form,
    }
    return render(request, "base/postexam.html", context)


@admin_only
def reports(request):
    context = {}
    return render(request, "base/reports.html", context)


@login_required(login_url="login")
def reportPost(request):
    form = ReportForm()
    if request.method == "POST":
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {
        "form": form,
    }
    return render(request, "base/postreport.html", context)


@login_required(login_url="login")
def notifications(request):
    notifications = Notification.objects.all()
    paginator = Paginator(notifications, 10)
    page = request.GET.get("page")
    try:
        notifications = paginator.page(page)
    except PageNotAnInteger:
        notifications = paginator.page(1)
    except EmptyPage:
        notifications = paginator.page(paginator.num_pages)

    context = {
        "page": page,
        "notifications": notifications,
    }
    return render(request, "base/notifications.html", context)


@login_required(login_url="login")
def account_settings(request):
    return render(request, "base/account_settings.html")


def support(request):
    return render(request, "base/support.html")


def info(request):
    return render(request, "base/info.html")


# Um professor posta uma prova e ganha créditos
# créditos para baixar as provas de outros professores
