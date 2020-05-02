from django.shortcuts import render
from django.http import HttpResponse

##
import random
import string

from students.models import Student


def generate_password(length: int = 10) -> str:
    choices = string.ascii_letters + string.digits + string.punctuation

    password = ''
    for _ in range(length):
        password += random.choice(choices)

    return password
##


def hello_world(request):
    return HttpResponse(
        generate_password(
            int(request.GET['length'])
        )
    )


def students(request):
    count = Student.objects.count()
    students_queryset = Student.objects.all()

    response = f'students: {count}<br/>'
    for student in students_queryset:
        response += student.info() + '<br/>'
    return HttpResponse(response)
