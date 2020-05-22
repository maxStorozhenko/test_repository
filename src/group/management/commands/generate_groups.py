from random import choice, randint

from django.core.management.base import BaseCommand

from faker import Faker

from group.models import Group

from students.models import Student

from teachers.models import Teacher


class Command(BaseCommand):
    help = 'Generates new groups (default = 100)'  # noqa  django requires 'help'

    def add_arguments(self, parser):
        parser.add_argument('number_of_groups', type=int, nargs='?', default=100)

    def handle(self, *args, **options):
        fake = Faker()
        specifications = ['Python', 'Javascript', 'Java', 'C++']
        count = options.get('number_of_groups')
        new_groups = []
        for _ in range(count):
            new_groups.append(Group(
                teacher=fake.name(),
                specification=choice(specifications),
                count_of_students=randint(10, 20),
                length_of_course=randint(1, 12),
                head=Student.objects.order_by('?').last(),
                curator=Teacher.objects.order_by('?').last()
            ))
        Group.objects.bulk_create(new_groups)
