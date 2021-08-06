import requests
import json

class Location(object):
    def __init__(self, LOCATION_API_KEY):
        self.LOCATION_API_KEY = LOCATION_API_KEY
        # https://velog.io/@yvvyoon/python-current-location-coordinate

    def get_location(self):
        url = f'https://www.googleapis.com/geolocation/v1/geolocate?key={self.LOCATION_API_KEY}'
        data = {
            'considerIp': True,
        }

        result = requests.post(url, data).text
        location = json.loads(result)
        location = location['location']

        return location