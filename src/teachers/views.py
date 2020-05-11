from django.shortcuts import get_object_or_404, redirect, render, reverse

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

    count = teachers.count()
    return render(request, 'teachers-list.html', context={'teachers': teachers,
                                                          'count': count})


def create_teacher(request):
    if request.method == 'POST':
        form = TeacherCreateForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(reverse('teachers:list'))
    elif request.method == 'GET':
        form = TeacherCreateForm()

    context = {'form_name': 'CREATE TEACHER',
               'create_form': form}
    return render(request, 'create.html', context=context)


def edit_teacher(request, pk):
    teacher = get_object_or_404(Teacher, id=pk)

    if request.method == 'POST':
        form = TeacherCreateForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect(reverse('teachers:list'))
    elif request.method == 'GET':
        form = TeacherCreateForm(instance=teacher)

    context = {'edit_form': form,
               'teacher': teacher,
               }

    return render(request, 'edit-teacher.html', context=context)


def delete_teacher(request, pk):
    student = Teacher.objects.filter(id=pk)
    student.delete()
    return redirect(reverse('teachers:list'))
