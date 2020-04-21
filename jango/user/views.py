from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'user/home.html',{"title":"Home Page"})

def about(request):
    return render(request,'user/about.html')
