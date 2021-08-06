import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from core.boxoffice import BoxOffice
import os
from pathlib import Path
from django.core.exceptions import ImproperlyConfigured

# Build paths inside the project like this: BASE_DIR / 'subdir'.
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


BOXOFFICE_API = get_boxOffice_api("boxoffice_api_key")


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
    response_data = {}
    response_data['api'] = 'POST Movie Rank'
    response_data['errorr_msg'] = 'you should request POST'
    response_data['response'] = '400'

    if request.method == 'POST':
        box = BoxOffice(BOXOFFICE_API)
        movies = box.get_movies()
        movie_lists = box.simplify(movies)
        response_data['response'] = '200'

        for movie_list in movie_lists:
            rank = movie_list['rank']
            response_data[rank] = movie_list

    return HttpResponse(json.dumps(response_data), content_type="application/json")
