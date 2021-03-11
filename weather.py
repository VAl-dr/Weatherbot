import datetime
import requests
from pprint import pprint


class Weather():
    def __init__(self, city):
        self.city = city

    def three_days_result(city):

        cnt = 24
        app_id = "5bf55858fa1b823d743d2b165c8131ad"
        result = ''

        resp = requests.get(
            f'https://api.openweathermap.org/data/2.5/forecast?q={city}&cnt={cnt}&units=metric&appid={app_id}')
        resp = resp.json()

        #pprint(resp)

        if int(resp['cod']) == 404:
            result = f'Города {city} не существует!'

        else:
            today = datetime.date.today().strftime('%d.%m')

            result += resp['city']['name'] + ', ' + resp['city']['country'] + '\n' + '\n'

            for i in range(0, cnt, 8):

                date_ = str(int(today[:2]) + i / 8) + today[4:]
                #temp = str(resp['list'][i]['main']['temp'])
                weather = resp['list'][i]['weather'][0]['main']

                weather_dict = {
                    'Clear': 'Ясно',
                    'Clouds': 'Облачно',
                    'Rain': 'Дождь',
                    'Snow': 'Снег',
                }

                if weather_dict.get(weather) is not None:
                    weather = weather_dict.get(weather)

                #'''
                temp = float(resp['list'][i]['main']['temp'])
                if temp % 1 >= 0.5:
                    temp = str(int(temp // 1 + 1))
                else:
                    temp = str(int(temp // 1))
                #'''

                if float(temp) > 0:
                    temp = '+' + temp

                result += str(date_ + '    ' + temp + u" \u2103" + '    ' + weather + '\n')
        return result


    def daily(city, day):

        cnt = 24
        app_id = "5bf55858fa1b823d743d2b165c8131ad"
        result = ''
        day_ = ''

        resp = requests.get(
            f'https://api.openweathermap.org/data/2.5/forecast?q={city}&cnt={cnt}&units=metric&appid={app_id}')
        resp = resp.json()

        #pprint(resp)

        today = datetime.date.today().strftime('%d.%m.%Y')

        if day < 10:
            day_ = '0' + str(day)
        else:
            day_ = str(day)

        result += 'Weather for ' + str(day_) + today[2:] + '\n'
        result += resp['city']['name'] + ', ' + resp['city']['country'] + '\n' + '\n'

        for i in range(cnt):
            if day_ == str(resp['list'][i]['dt_txt'])[8:10]:
                time_ = str(resp['list'][i]['dt_txt'])[11:16]
                # temp = str(resp['list'][i]['main']['temp'])
                weather = resp['list'][i]['weather'][0]['main']

                weather_dict = {
                    'Clear': 'Ясно',
                    'Clouds': 'Облачно',
                    'Rain': 'Дождь',
                    'Snow': 'Снег',
                }

                if weather_dict.get(weather) is not None:
                    weather = weather_dict.get(weather)

                # '''
                temp = float(resp['list'][i]['main']['temp'])
                if temp % 1 >= 0.5:
                    temp = str(int(temp // 1 + 1))
                else:
                    temp = str(int(temp // 1))
                # '''

                if float(temp) > 0:
                    temp = '+' + temp
                elif int(temp) == 0:
                    temp = ' ' + temp

                result += str(time_ + '    ' + temp + u" \u2103" + '    ' + weather + '\n')
        return result


'''
d3 = Weather.three_days_result('Kulusuk')
d1 = Weather.daily('Zaporizhzhia', 6)
print(d3)
#print(d1)
'''
