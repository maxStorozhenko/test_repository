from django.contrib import admin

from group.models import Group


class GroupAdmin(admin.ModelAdmin):
    list_per_page = 19
    list_display = ('id', 'teacher', 'specification', 'count_of_students', 'length_of_course')
    fields = ('teacher', 'specification', 'count_of_students', 'length_of_course')


admin.site.register(Group, GroupAdmin)
