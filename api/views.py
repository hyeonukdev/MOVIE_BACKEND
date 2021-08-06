import os
import json
from pathlib import Path
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ImproperlyConfigured
from core.boxoffice import BoxOffice
from core.location import Location
from core.theater.lottecinema import LotteCinema


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
def test(request):
    if request.method == 'POST':
        response_data = {}
        response_data['result'] = 'POST test'
        response_data['message'] = 'Some test message'

        return HttpResponse(json.dumps(response_data), content_type="application/json")

    elif request.method == 'GET':
        response_data = {}
        response_data['result'] = 'GET test'
        response_data['message'] = 'Some test message'

        return HttpResponse(json.dumps(response_data), content_type="application/json")


@csrf_exempt
def movieRank(request):
    '''
    To get movie rank
    :param request:
    :return:
    {
        "api": "POST Movie Rank",
        "response": "200",
        "1": {
            "rank": "1",
            "name": "모가디슈",
            "code": "20204117"
        },
        "2": {
            "rank": "2",
            "name": "더 수어사이드 스쿼드",
            "code": "20217845"
        },
        "3": {
            "rank": "3",
            "name": "보스 베이비 2",
            "code": "20218391"
        },
        ...
    }
    '''
    response_data = {}
    response_data['api'] = 'POST Movie Rank'

    if request.method == 'POST':
        box = BoxOffice(BOXOFFICE_API_KEY)
        movies = box.get_movies()
        movie_lists = box.simplify(movies)
        response_data['response'] = '200'

        for movie_list in movie_lists:
            rank = movie_list['rank']
            response_data[rank] = movie_list
    else:
        response_data['errorr_msg'] = 'you should request POST'
        response_data['response'] = '400'

    return HttpResponse(json.dumps(response_data), content_type="application/json")


@csrf_exempt
def location(request):
    '''
    To get my location
    :param request:
    :return:
    {
        "api": "POST my location",
        "response": "200",
        "location": {
            "lat": 37.5160832,
            "lng": 126.9071872
        }
    }
    '''
    response_data = {}
    response_data['api'] = 'POST my location'

    if request.method == 'POST':
        location = Location(LOCATION_API_KEY)
        myloc = location.get_location()
        response_data['response'] = '200'
        response_data['location'] = myloc
    else:
        response_data['errorr_msg'] = 'you should request POST'
        response_data['response'] = '400'

    return HttpResponse(json.dumps(response_data), content_type="application/json")


@csrf_exempt
def filter_nearest_lottecinema(request):
    '''
    TO get filtered nearest 3 lottecinema
    :param request:
    :return:
    {
        "api": "POST lottecinema fileter by location",
        "response": "200",
        "near_theater_lists": [
            {
                "TheaterName": "영등포 롯데시네마",
                "TheaterID": "1|17|1002",
                "Longitude": "126.907755",
                "Latitude": "37.516369"
            },
            {
                "TheaterName": "신도림 롯데시네마",
                "TheaterID": "1|14|1015",
                "Longitude": "126.8889387",
                "Latitude": "37.5086097"
            },
            {
                "TheaterName": "합정 롯데시네마",
                "TheaterID": "1|24|1010",
                "Longitude": "126.9134333",
                "Latitude": "37.5504586"
            }
        ]
    }
    '''
    response_data = {}
    response_data['api'] = 'POST lottecinema fileter by location'

    if request.method == 'POST':
        cinema = LotteCinema()
        location = Location(LOCATION_API_KEY)
        myloc = location.get_location()
        lat = myloc['lat']
        lng = myloc['lng']

        theater_lists = cinema.filter_nearest_theater(cinema.get_theater_list(), lat, lng)

        response_data['response'] = '200'
        response_data['near_theater_lists'] = theater_lists
    else:
        response_data['errorr_msg'] = 'you should request POST'
        response_data['response'] = '400'

    return HttpResponse(json.dumps(response_data), content_type="application/json")


@csrf_exempt
def filtered_lottecinema_movie_list(request):
    '''
    To get movie list by filtered lottecinema
    :param request:
    {
        "TheaterID": "1|17|1002"
    }
    :return:
    {
    "api": "POST filetered lottecinema movie list",
    "response": "200",
    "movie_lists": {
            "17616": {
                "Name": "모가디슈",
                "Schedules": [
                    {
                        "StartTime": "14:10",
                        "RemainingSeat": 134
                    },
                    {
                        "StartTime": "16:35",
                        "RemainingSeat": 120
                    },
                    ...
                ]
            },
            "17652": {
                "Name": "더 수어사이드 스쿼드",
                "Schedules": [
                    {
                        "StartTime": "14:10",
                        "RemainingSeat": 91
                    },
                    {
                        "StartTime": "16:50",
                        "RemainingSeat": 86
                    },
                    ...
                ]
            },
            "17623": {
                "Name": "보스 베이비 2",
                "Schedules": [
                    {
                        "StartTime": "17:50",
                        "RemainingSeat": 57
                    }
                ]
            },
            ...
        }
    }
    '''
    response_data = {}
    response_data['api'] = 'POST filetered lottecinema movie list'

    if request.method == 'POST':
        data = json.loads(request.body)
        TheaterID = data.get('TheaterID')
        cinema = LotteCinema()
        movie_list = cinema.get_movie_list(TheaterID)

        response_data['response'] = '200'
        response_data['movie_lists'] = movie_list
    else:
        response_data['errorr_msg'] = 'you should request POST'
        response_data['response'] = '400'

    return HttpResponse(json.dumps(response_data), content_type="application/json")