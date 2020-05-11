from django.contrib import admin

from students.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_per_page = 19
    list_display = ('id', 'first_name', 'last_name', 'age')
    fields = ('first_name', 'last_name', 'age')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        if not request.user.is_superuser:
            queryset = queryset.filter(age__gte=18)

        return queryset


admin.site.register(Student, StudentAdmin)
