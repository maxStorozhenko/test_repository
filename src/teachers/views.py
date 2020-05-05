from django.http import HttpResponse

from django.shortcuts import render  # noqa  Autoimported by django

from teachers.models import Teacher


def show_teachers(request):
    params = ['first_name',
              'last_name',
              'age',
              'age__gt',
              'age__lt',
              'age__lte',
              'age__gte',
              'specification',
              'active_groups'
              ]

    teachers = Teacher.objects.all()

    for param in params:
        value = request.GET.get(param)
        if value:
            teachers = teachers.filter(**{param: value})

    response = f'Count of teachers: {teachers.count()}<br/>'

    for teacher in teachers:
        response += teacher.info + '<br/>'

    return HttpResponse(response)
