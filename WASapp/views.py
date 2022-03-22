from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Please go to  <a href='/courses/'>COURSES</a> !")
# Create your views here.

def courses(request):
    return HttpResponse("This is Courses!")
