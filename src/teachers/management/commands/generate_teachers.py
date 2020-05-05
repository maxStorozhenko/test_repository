from random import choice, randint

from django.core.management.base import BaseCommand

from faker import Faker

from teachers.models import Teacher


class Command(BaseCommand):
    help = 'Generates new teachers (default = 100)'  # noqa  django requires 'help'

    def add_arguments(self, parser):
        parser.add_argument('number_of_teachers', type=int, nargs='?', default=100)

    def handle(self, *args, **options):
        fake = Faker()
        specifications = ['Python', 'Javascript', 'Java', 'C++']
        count = options.get('number_of_teachers')
        for _ in range(count):
            Teacher.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                age=randint(25, 100),
                specification=choice(specifications),
                active_groups=randint(1, 5)
            )
