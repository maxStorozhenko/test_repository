from flask import Flask, request
import requests
from functions import get_requirements, parse_count, get_users, get_mean_from_csv


app = Flask(__name__)


@app.route('/requirements/')
def requirements():
    return get_requirements('requirements.txt')


@app.route('/generate-users/')
def generate_users():
    count = parse_count(request.args.get('count', '100'))

    if type(count) is str:
        return count

    return get_users(count)


@app.route('/mean/')
def mean():
    return get_mean_from_csv()


@app.route('/space/')
def count_of_cosmonauts():
    r = requests.get('http://api.open-notify.org/astros.json')
    count = r.json()['number']
    return f'The number of astronauts currently = {count}'


if __name__ == '__main__':
    app.run()
