# Программа запроса текущей погоды с использованием API Yandex и методов GET/POST.
# Данные выводятся с заднной периодичностью в консоль и пишутся в архивный .csv файл.

import json

class WeatherInformer:

    def __init__(self, fileParams):
        # Считываем необходимые для работы параметры из файла
        with open(fileParams) as pfile:
            self.params = json.load(pfile)
        print(self.params)

    def weather_info(self):

        return True




# ========= MAIN SECTION =============

leninskoe = WeatherInformer('params.json')