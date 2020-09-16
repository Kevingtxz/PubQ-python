from django.shortcuts import render
# from django.contrib import messages       use after

def questions(request):
    # questions = Question.objects.values('exam', 'text', 'answears')
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

# def logoutUser(request):
# 	logout(request)
# 	return redirect('login')

# def accountSettings(request):
#     return render(request, 'base/profilesettings.html')

# def loginPage(request):
#     return render(request, 'base/register.html')





# Um professor posta uma prova e ganha créditos
# créditos para baixar as provas de outros professores