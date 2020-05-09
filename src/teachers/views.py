from django.http import HttpResponse
from django.shortcuts import redirect, render

from forms import TeacherCreateForm

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


def create_teacher(request):
    if request.method == 'POST':
        form = TeacherCreateForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    elif request.method == 'GET':
        form = TeacherCreateForm()

    context = {'form_name': 'CREATE_TEACHER',
               'create_form': form}
    return render(request, 'create.html', context=context)
