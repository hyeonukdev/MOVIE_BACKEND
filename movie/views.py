import os
import json
from pathlib import Path
from django.shortcuts import render
from django.core.exceptions import ImproperlyConfigured
from core.boxoffice import BoxOffice
from core.location import Location
from core.theater.lottecinema import LotteCinema
from core.theater.cgv import CGV


BASE_DIR = Path(__file__).resolve().parent.parent
secret_file = os.path.join(BASE_DIR, 'secrets.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())


def get_boxOffice_api(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} boxoffice api variable".format(setting)
        raise ImproperlyConfigured(error_msg)


def get_location_api(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} location api variable".format(setting)
        raise ImproperlyConfigured(error_msg)


BOXOFFICE_API_KEY = get_boxOffice_api("BOXOFFICE_API_KEY")
LOCATION_API_KEY = get_location_api("LOCATION_API_KEY")


def index(request):
    data = 'index page'
    return render(request, 'movie/index.html', {'data': data})


def rank(request):
    response_data = {}

    box = BoxOffice(BOXOFFICE_API_KEY)
    movies = box.get_movies()
    movie_lists = box.simplify(movies)

    for movie_list in movie_lists:
        rank = movie_list['rank']
        response_data[rank] = movie_list

    print(response_data)

    return render(request, 'movie/rank.html', {'datas': response_data})