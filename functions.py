import csv
from faker import Faker


def get_requirements(file_name):
    file = open(file_name)
    req = file.read()
    file.close()
    req = req.replace('\n', '<br>')
    return req


def parse_count(count):
    if not count.isdigit():
        return f'Incorrect parameter count: {count}'

    count = int(count)
    if count < 1 or count > 200:
        return f'Incorrect value of "count": {count}'

    return count


def get_users(count):
    fake = Faker()
    users = ''
    for i in range(int(count)):
        users += f'{i + 1}. {fake.name()} {fake.email()}\n'
    response = users.replace('\n', '<br>')
    return response


def inches_to_sm(inches):
    return round(inches * 2.54, 2)


def pounds_to_kg(pounds):
    return round(pounds * 0.453592, 2)


def get_mean_from_csv():
    total_height = 0
    total_weight = 0
    count = 0
    with open('hw.csv', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        for index, line in enumerate(csv_reader):
            if index == 0:
                continue
            height, weight = line[1], line[2]
            total_height += float(height.strip(', '))
            total_weight += float(weight.strip(', '))
            count += 1
    mean_height = total_height / count
    mean_weight = total_weight / count
    return f'Average height = {inches_to_sm(mean_height)} cm; Average weight = {pounds_to_kg(mean_weight)} kg'
