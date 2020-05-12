from django.urls import path

from students import views

app_name = 'students'

urlpatterns = [
    path('hello-world/', views.hello_world, name='hello_world'),
    path('list/', views.students, name='list'),
    path('create/', views.create_student, name='create'),
    path('edit/<int:pk>', views.edit_student, name='edit'),
    path('generate-one/', views.generate_student, name='generate_one'),
    path('generate-some/<int:count>', views.generate_students, name='generate_some'),
    path('delete/<int:pk>/', views.delete_student, name='delete',)
]
