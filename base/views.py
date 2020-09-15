from django.shortcuts import render

def questions(request):
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

# customer settings

# login pages



# Um professor posta uma prova e ganha créditos
# créditos para baixar as provas de outros professores