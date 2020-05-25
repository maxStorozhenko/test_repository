from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    age = models.PositiveSmallIntegerField()
    specification = models.CharField(max_length=32)
    active_groups = models.PositiveSmallIntegerField()

    @property
    def info(self) -> str:
        return f'{self.first_name} {self.last_name} {self.age} {self.specification} ' \
               f'{self.active_groups} groups'

    def __str__(self):
        return f'{self.id} {self.first_name} {self.last_name}'
