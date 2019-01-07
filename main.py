# Программа запроса текущей погоды с использованием API Yandex и методов GET/POST.
# Данные выводятся с заднной периодичностью в консоль и пишутся в архивный .csv файл.

import json
import requests
from pprint import pprint

class WeatherInformer:

    def __init__(self, fileParams):
        # Считываем необходимые для работы параметры из файла
        with open(fileParams) as pfile:
            self.params = json.load(pfile)
        print(self.params)
        self.questParams = {'lat': self.params['lat'], 'lon': self.params['lon'], 'hourse': 'false', 'limit': '1'}
        print(self.questParams)

    def weather_info(self):
        url = 'https://api.weather.yandex.ru/v1/forecast?'
        response = requests.get(url, self.questParams, headers={'X-Yandex-API-Key': '4141b45c-ca49-4f38-9000-3da80ab71c38'})
        pprint(response.json())
        return




# ========= MAIN SECTION =============

leninskoe = WeatherInformer('params.json')
leninskoe.weather_info()