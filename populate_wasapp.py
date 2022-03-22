#asdf

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
        'GAprogram.settings')

import django
django.setup()
from WASapp.models import Course

def populate():

    new_courses = [{'name':"Web Application Systems",
                    'date': "Starting Date: April 1 2022",
                    'desc': "This is the most useful, most valuable and most inspiring course ever!"},
                   {'name':"Software Engineering",
                    'date': "Starting Date: June 1, 2022",
                    'desc': "This course is about good software engineering practices."}]

    for course in new_courses:
        add_course(course['name'], course['date'], course['desc'])


def add_course(name, date, desc):
    p = Course.objects.get_or_create(name=name, date=date, desc = desc)
    #p.save()
    return p

if __name__ == '__main__':
    print('Starting WASapp population script...')
    populate()


