from django.db.models.signals import pre_save
from django.dispatch import receiver

from students.models import Student

from teachers.models import Teacher


@receiver(pre_save)
def save_profile(sender, instance, **kwargs):
    if sender is Student or sender is Teacher:
        instance.first_name = instance.first_name.capitalize()
        instance.last_name = instance.last_name.capitalize()
