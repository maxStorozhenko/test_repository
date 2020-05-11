from django.urls import path

from teachers import views

app_name = 'teachers'

urlpatterns = [
    path('list/', views.show_teachers, name='list'),
    path('create/', views.create_teacher, name='create'),
    path('edit/<int:pk>', views.edit_teacher, name='edit'),
    path('delete/<int:pk>', views.delete_teacher, name='delete'),
]
