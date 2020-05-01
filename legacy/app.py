from flask import Flask, request
import requests
from functions import get_requirements, parse_count, get_users, get_mean_from_csv
from db_func import run_query, filter_and

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


@app.route('/names/')
def names():
    query = 'SELECT COUNT(DISTINCT FirstName) FROM customers'
    return f"Count of unique names - {str(run_query(query))}"


@app.route('/customers/')
def customers():
    result = 'SELECT * FROM customers'
    params = request.args.get('filter')

    if params:
        result += f' WHERE {filter_and(params)};'
        return str(run_query(result))

    return str(run_query(f'{result};'))


@app.route('/tracks/')
def tracks():
    query = 'SELECT COUNT(TrackId) FROM tracks'
    return f"Count of tracks - {str(run_query(query))}"


@app.route('/tracks-sec/')
def tracks_sec():
    query = 'SELECT Name, Milliseconds / 1000 FROM tracks'
    return str(run_query(query))


if __name__ == '__main__':
    app.run(debug=True)
