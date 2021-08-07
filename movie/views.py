import os
import json
from pathlib import Path
from django.shortcuts import render
from django.core.exceptions import ImproperlyConfigured
from django.views.decorators.csrf import csrf_exempt

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


@csrf_exempt
def index(request):
    data = 'index page'
    return render(request, 'movie/index.html', {'data': data})


@csrf_exempt
def rank(request):
    response_data = {}

    box = BoxOffice(BOXOFFICE_API_KEY)
    movies = box.get_movies()
    movie_lists = box.simplify(movies)

    for movie_list in movie_lists:
        rank = movie_list['rank']
        response_data[rank] = movie_list

    return render(request, 'movie/rank.html', {'datas': response_data})


@csrf_exempt
def nearCGV(request):
    cinema = LotteCinema()
    location = Location(LOCATION_API_KEY)
    myloc = location.get_location()
    lat = myloc['lat']
    lng = myloc['lng']

    theater_lists = cinema.filter_nearest_theater(cinema.get_theater_list(), lat, lng)

    return render(request, 'movie/nearCGV.html', {'datas': theater_lists})


@csrf_exempt
def findTheater(request):
    # LOTTE
    cinema = LotteCinema()
    location = Location(LOCATION_API_KEY)
    movie_info = request.body
    movie_info = movie_info.decode('utf-8')
    movie_code = movie_info.split('&')[0]
    movie_code = movie_code.split('=')[1]
    movie_place = movie_info.split('&')[1]
    if movie_place.split('=')[1]:
        movie_place = movie_place.split('=')[1]
        findLoc = location.get_place_location(movie_place)
        lat = findLoc['lat']
        lng = findLoc['lng']
    else:
        myloc = location.get_location()
        lat = myloc['lat']
        lng = myloc['lng']

    lotte_theater_lists = cinema.filter_nearest_theater(cinema.get_theater_list(), lat, lng)

    return render(request, 'movie/findTheater.html', {'lotte_theater_lists': lotte_theater_lists})