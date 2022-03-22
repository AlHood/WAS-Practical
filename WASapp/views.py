from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Please go to /courses/ !")
# Create your views here.

def courses(request):
    return HttpResponse("This is Courses!")
