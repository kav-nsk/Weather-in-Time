# Программа запроса текущей погоды с использованием API Yandex и методов GET/POST.
# Данные выводятся с заданной периодичностью в консоль и пишутся в архивный .csv файл.
# Настройки содержатся в файле params.json

import json
import requests
import time
import csv
from pprint import pprint


class WeatherInformer:

    def __init__(self, fileParams):
        # Считываем необходимые для работы параметры из файла params.json
        with open(fileParams) as pfile:
            self.params = json.load(pfile)

        self.nameArhFile = self.params['outputFile']
        open(self.nameArhFile, 'w')
        self.questParams = {'lat': self.params['lat'], 'lon': self.params['lon'], 'hours': 'false', 'limit': '2'}
        self.periodCall = self.params['timer']
        self.firstCall = True

    def weather_info(self):
        # Делаем запрос в Yandex
        url = 'https://api.weather.yandex.ru/v1/forecast'
        timeRequest = time.ctime()
        req = requests.get(url, self.questParams, headers={'X-Yandex-API-Key': self.params['key']})
        self.statusCode = req.status_code
        response = req.json()
        response = [
                    {'param': 'время запроса', 'value': timeRequest[4:-5]},
                    {'param': 'время замера', 'value': time.ctime(response['fact']['obs_time'])[4:-5]},
                    {'param': 't сейчас', 'value': response['fact']['temp'], 'unit': 'C'},
                    {'param': 'давление', 'value': response['fact']['pressure_mm'], 'unit': 'мм рт. ст.'},
                    {'param': 'влажность', 'value': response['fact']['humidity'], 'unit': '%'},
                    {'param': 'скорость ветра', 'value': response['fact']['wind_speed'], 'unit': 'м/с'},
                    {'param': 'направление ветра', 'value': response['fact']['wind_dir']}
                    ]

        # Формирование шапки для csv
        columnName = [response[i]['param'] + ', ' + response[i]['unit'] for i in range(2, len(response) - 1)]
        columnName.insert(0, response[0]['param'])
        columnName.insert(1, response[1]['param'])
        columnName.append(response[-1]['param'])

        # Запись в архивный файл
        with open(self.nameArhFile, 'a') as arhFile:
            toArhFile = csv.writer(arhFile)
            writer = csv.DictWriter(arhFile, fieldnames=columnName)
            if self.firstCall:
                writer.writeheader()
            writer.writerow({columnName[i]: response[i]['value'] for i in range(len(response))})

        self.firstCall = False
        return




# ========= MAIN SECTION =============

location = WeatherInformer('params.json')
while True:
    location.weather_info()
    print('Код ответа:', location.statusCode)
    time.sleep(location.periodCall)