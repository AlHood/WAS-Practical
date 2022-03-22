from django.shortcuts import render
from WASapp.models import Course

from django.http import HttpResponse

def index(request):
    return HttpResponse("Please go to  <a href='/courses/'>COURSES</a> !")
# Create your views here.

def courses(request):
    course_list = Course.objects.order_by('name')

    context_dict = {}
    context_dict['courses'] = course_list
    return render(request, 'WASapp/index.html', context=context_dict)
