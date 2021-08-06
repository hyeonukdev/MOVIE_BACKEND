import json
import math
from datetime import datetime
from urllib.request import urlopen
from urllib.parse import urlencode


class LotteCinema(object):
    base_url = 'https://www.lottecinema.co.kr'
    base_url_cinema_data = '{}/LCWS/Cinema/CinemaData.aspx'.format(base_url)
    base_url_movie_list = '{}/LCWS/Ticketing/TicketingData.aspx'.format(base_url)

    def make_payload(self, **kwargs):
        '''
        To make payload
        :param kwargs:
        :return:
        '''
        param_list = {'channelType': 'MW', 'osType': '', 'osVersion': '', **kwargs}
        data = {'ParamList': json.dumps(param_list)}
        payload = urlencode(data).encode('cp949')
        return payload

    def byte_to_json(self, fp):
        '''
        byte to json
        :param fp:
        :return:
        '''
        content = fp.read().decode('utf-8')
        return json.loads(content)

    def get_theater_list(self):
        '''
        To get theater list
        :return:
        '''
        url = self.base_url_cinema_data
        payload = self.make_payload(MethodName='GetCinemaItems')
        with urlopen(url, data=payload) as fin:
            json_content = self.byte_to_json(fin)
            return [
                {
                    'TheaterName': '{} 롯데시네마'.format(entry.get('CinemaNameKR')),
                    'TheaterID': '{}|{}|{}'.format(entry.get('DivisionCode'), entry.get('SortSequence'), entry.get('CinemaID')),
                    'Longitude': entry.get('Longitude'),
                    'Latitude': entry.get('Latitude')
                }
                for entry in json_content.get('Cinemas').get('Items')
            ]

    def distance(self, x1, x2, y1, y2):
        '''
        TO get distance (x1, x2) ~ (y1, y2)
        :param x1:
        :param x2:
        :param y1:
        :param y2:
        :return:
        '''
        dx = float(x1) - float(x2)
        dy = float(y1) - float(y2)
        distance = math.sqrt(dx**2 + dy**2)
        return distance

    def filter_nearest_theater(self, theater_list, pos_latitude, pos_longitude, n=3):
        '''
        To filter by location to get nearest theater count 3
        :param theater_list:
        :param pos_latitude:
        :param pos_longitude:
        :param n:
        :return:
        '''
        distance_to_theater = []
        for theater in theater_list:
            distance = self.distance(pos_latitude, theater.get('Latitude'), pos_longitude, theater.get('Longitude'))
            distance_to_theater.append((distance, theater))

        return [theater for distance, theater in sorted(distance_to_theater, key=lambda x: x[0])[:n]]

    def get_movie_list(self, theater_id):
        '''
        To get moive list by theater_id
        :param theater_id:
        :return:
        '''
        url = self.base_url_movie_list
        target_dt = datetime.now()
        target_dt_str = target_dt.strftime('%Y-%m-%d')
        payload = self.make_payload(MethodName='GetPlaySequence', playDate=target_dt_str, cinemaID=theater_id, representationMovieCode='')
        with urlopen(url, data=payload) as fin:
            json_content = self.byte_to_json(fin)
            movie_id_to_info = {}

            for entry in json_content.get('PlaySeqsHeader', {}).get('Items', []):
                movie_id_to_info.setdefault(entry.get('MovieCode'), {})['Name'] = entry.get('MovieNameKR')

            for order, entry in enumerate(json_content.get('PlaySeqs').get('Items')):
                schedules = movie_id_to_info[entry.get('MovieCode')].setdefault('Schedules', [])
                schedule = {
                    'StartTime': '{}'.format(entry.get('StartTime')),
                    'RemainingSeat': int(entry.get('TotalSeatCount')) - int(entry.get('BookingSeatCount'))
                }
                schedules.append(schedule)
            return movie_id_to_info

cinema = LotteCinema()

# print(cinema.filter_nearest_theater(cinema.get_theater_list(), 37.5, 126.844))
'''
[{'TheaterName': '광명(광명사거리) 롯데시네마', 'TheaterID': '1|2|3027', 'Longitude': '126.8556578', 'Latitude': '37.4794548'}, 
{'TheaterName': '신도림 롯데시네마', 'TheaterID': '1|14|1015', 'Longitude'titude': '37.5086097'}, 
{'TheaterName': '가산디지털 롯데시네마', 'TheaterID': '1|1|1013', 'Longitude': '126.8890717', 'Latitude': '37.4775952'}]
'''
# print('===')
print(cinema.get_movie_list('1|0003|4005'))
'''
{'17616': {'Name': '모가디슈', 'Schedules': [{'StartTime': '19:40', 'RemainingSeat': 120}]}, 
'17652': {'Name': '더 수어사이드 스쿼드', 'Schedules': [{'StartTime': '19:30', 'RemainingSeat': 75}]}, 
'17657피닉스', 'Schedules': [{'StartTime': '20:00', 'RemainingSeat': 22}]}}

'''