from django import forms

from group.models import Group

from students.models import Student

from teachers.models import Teacher


class StudentCreateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'age')


class TeacherCreateForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('first_name',
                  'last_name',
                  'age',
                  'specification',
                  'active_groups')


class GroupCreateForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('teacher',
                  'specification',
                  'count_of_students',
                  'length_of_course')
