from django.db import models


class Group(models.Model):
    teacher = models.CharField(max_length=64)
    specification = models.CharField(max_length=64)
    count_of_students = models.PositiveSmallIntegerField()
    length_of_course = models.PositiveSmallIntegerField()

    def info(self) -> str:
        return f'{self.id} {self.teacher} {self.specification} {self.count_of_students} students {self.length_of_course} month'

    def add_student(self) -> None:
        self.count_of_students += 1
        self.save()
