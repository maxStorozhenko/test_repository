from django.contrib import admin

from teachers.models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    list_per_page = 19
    list_display = ('id', 'first_name', 'last_name', 'age', 'specification', 'active_groups')
    fields = ('first_name', 'last_name', 'age', 'specification', 'active_groups')


admin.site.register(Teacher, TeacherAdmin)
