from django.db.models.signals import pre_save
from django.dispatch import receiver

from students.models import Student

from teachers.models import Teacher


@receiver(pre_save, sender=Student)
def student_capitalize(sender, instance, **kwargs):
    instance.first_name = instance.first_name.capitalize()
    instance.last_name = instance.last_name.capitalize()


@receiver(pre_save, sender=Teacher)
def teacher_capitalize(sender, instance, **kwargs):
    instance.first_name = instance.first_name.capitalize()
    instance.last_name = instance.last_name.capitalize()
