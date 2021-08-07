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
    lotte_theater_info = []
    lotte_movie_schedules = []
    Lcinema = LotteCinema()
    location = Location(LOCATION_API_KEY)

    movie_name = request.POST.get('selected_movie')
    date = request.POST.get('date')
    if request.POST.get('moviePlace'):
        movie_place = request.POST.get('moviePlace')
        findLoc = location.get_place_location(movie_place)
        lat = findLoc['lat']
        lng = findLoc['lng']
    else:
        movie_place = 'here'
        myloc = location.get_location()
        lat = myloc['lat']
        lng = myloc['lng']

    lotte_theater_lists = Lcinema.filter_nearest_theater(Lcinema.get_theater_list(), lat, lng)

    for lotte_theater in lotte_theater_lists:
        theaterID = lotte_theater.get('TheaterID')
        theaterName = lotte_theater.get('TheaterName')
        theaterLng = lotte_theater.get('Longitude')
        theaterLat = lotte_theater.get('Latitude')
        movie_lists = Lcinema.get_movie_list(theaterID, date)
        # print(f"theaterID: {theaterID}, theaterName: {theaterName}, theaterLng: {theaterLng}, movie_lists: {movie_lists}")

        for key, value in movie_lists.items():
            if value.get('Name') == movie_name:
                schedules = value.get('Schedules')[0]
                lotte_movie_schedules.append(schedules)
            else:
                continue

        lotte_theater_info.append({
            'TheaterID': theaterID,
            'TheaterName': theaterName,
            'Longitude': theaterLng,
            'Latitude': theaterLat,
            'MoiveLists': lotte_movie_schedules
        })

    datas = {
        'movie_name': movie_name,
        'movie_place': movie_place,
        'lotte_theater_info': lotte_theater_info
    }

    return render(request, 'movie/findTheater.html', {'datas': datas})