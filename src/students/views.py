import random
import string

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render, reverse

from faker import Faker

from forms import StudentCreateForm

from students.models import Student


def generate_password(length: int = 10) -> str:
    choices = string.ascii_letters + string.digits + string.punctuation

    password = ''
    for _ in range(length):
        password += random.choice(choices)

    return password


def generate_one_student() -> Student:
    fake = Faker()
    new_student = Student.objects.create(first_name=fake.first_name(),
                                         last_name=fake.last_name(),
                                         age=random.randint(0, 100))

    return new_student


def hello_world(request):
    return HttpResponse(
        generate_password(
            int(request.GET['length'])
        )
    )


def students(request):
    count = Student.objects.count()
    students_queryset = Student.objects.all()
    return render(request, 'students-list.html', context={'students': students_queryset,
                                                          'count': count})


def generate_student(request) -> HttpResponse:
    generate_one_student()
    return redirect(reverse('students:list'))


def generate_students(request, count) -> HttpResponse:
    for i in range(count):
        generate_one_student()
    return redirect(reverse('students:list'))


def index(request):
    return render(request, 'index.html')


def create_student(request):
    if request.method == 'POST':
        form = StudentCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('students:list'))

    elif request.method == 'GET':
        form = StudentCreateForm()

    context = {
        'form_name': 'CREATE STUDENT',
        'create_form': form,
    }

    return render(request, 'create.html', context=context)


def edit_student(request, pk=id):
    student = get_object_or_404(Student, id=pk)

    if request.method == 'POST':
        form = StudentCreateForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return redirect(reverse('students:list'))

    elif request.method == 'GET':
        form = StudentCreateForm(instance=student)

    context = {
        'edit_form': form,
        'student': student,
    }

    return render(request, 'edit-student.html', context=context)


def delete_student(request, pk):
    student = Student.objects.filter(id=pk)
    student.delete()
    return redirect(reverse('students:list'))
