from django.shortcuts import render
from django.http import HttpResponse
from teachers.models import Teacher


def show_teachers(request):
    teachers = Teacher.objects.all()
    response = ''

    for teacher in teachers:
        response += teacher.info + '<br/>'

    return HttpResponse(response)
