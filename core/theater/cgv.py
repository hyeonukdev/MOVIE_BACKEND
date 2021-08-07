import json
import math
from datetime import datetime
from urllib.request import urlopen
from urllib.parse import urlencode


class CGV():
    base_url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx'

    def get_region_list(self, areaName):
        '''
        To get Region list

        ---
        :parameter:
        areaName='서울'
        :return:
        01
        '''

        with open('./data/AreaCodes.json') as json_file:
            data = json.load(json_file)

        data = data.get('areaCode')

        if areaName:
            areaCode = data.get(areaName)
        else:
            areaCode = '999'
        return areaCode

    def get_theater_list(self, areaCode):
        '''
        To get theater list

        ---
        :parameter:
        areaCode = 01
        :return:
        [{'TheaterCode': '0056', 'TheaterName': 'CGV강남'}, {'TheaterCode': '0001', 'TheaterName': 'CGV강변'}, {'TheaterCode': '0229', 'TheaterName': 'CGV건대입구'}, {'TheaterCode': '0010', 'TheaterName': 'CGV구로'}, {'TheaterCode': '0063',ame': 'CGV대학로'}, {'TheaterCode': '0252', 'TheaterName': 'CGV동대문'}, {'TheaterCode': '0230', 'TheaterName': 'CGV등촌'}, {'TheaterCode': '0009', 'TheaterName': 'CGV명동'}, {'TheaterCode': '0105', 'TheaterName': 'CGV명동역 씨네라이Code': '0011', 'TheaterName': 'CGV목동'}, {'TheaterCode': '0057', 'TheaterName': 'CGV미아'}, {'TheaterCode': '0030', 'TheaterName': 'CGV불광'}, {'TheaterCode': '0046', 'TheaterName': 'CGV상봉'}, {'TheaterCode': '0300', 'TheaterName'여대입구'}, {'TheaterCode': '0088', 'TheaterName': 'CGV송파'}, {'TheaterCode': '0276', 'TheaterName': 'CGV수유'}, {'TheaterCode': '0150', 'TheaterName': 'CGV신촌아트레온'}, {'TheaterCode': '0040', 'TheaterName': 'CGV압구정'}, {'TheaterCode': '0112', 'TheaterName': 'CGV여의도'}, {'TheaterCode': '0292', 'TheaterName': 'CGV연남'}, {'TheaterCode': '0059', 'TheaterName': 'CGV영등포'}, {'TheaterCode': '0074', 'TheaterName': 'CGV왕십리'}, {'TheaterCode': '0013', 'The'CGV용산아이파크몰'}, {'TheaterCode': '0131', 'TheaterName': 'CGV중계'}, {'TheaterCode': '0199', 'TheaterName': 'CGV천호'}, {'TheaterCode': '0107', 'TheaterName': 'CGV청담씨네시티'}, {'TheaterCode': '0223', 'TheaterName': 'CGV피카디de': '0164', 'TheaterName': 'CGV하계'}, {'TheaterCode': '0191', 'TheaterName': 'CGV홍대'}, {'TheaterCode': 'P001', 'TheaterName': 'CINE de CHEF 압구정'}, {'TheaterCode': 'P013', 'TheaterName': 'CINE de CHEF 용산아이파크몰'}]
        '''
        with open('./data/TheaterCodes.json') as json_file:
            data = json.load(json_file)

        if areaCode:
            theaterLists = data.get(areaCode)
        else:
            theaterLists = ['null']
        return theaterLists

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

cgv = CGV()
areaName = '서울'
print(cgv.get_region_list(areaName))
# areaCode = cgv.get_region_list(areaName)
# print(cgv.get_theater_list(areaCode))