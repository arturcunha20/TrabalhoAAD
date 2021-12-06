from django.shortcuts import render

def home(request):
    return render(request,"home.html")

def home_next(request):
    frase = request.POST.get('box')
    return render(request,"home_next.html",{"frase":frase})

def index(request):
    return render(request,"index.html")