# -*- coding: UTF-8 -*-
import requests
import json

def translate (text):
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    headers = {'Content-type': 'application/json',
            'Accept': 'application/json',
            'Content-Encoding': 'UTF-8'
            }
    data = {'lang':'en-ru'
            ,'key': 'trnsl.1.1.20190814T072216Z.1d484639e7b367bd.97e836b16a42bde09b118163f3afa6054de5429f'
            ,'format':'plain'
            ,'text':text
            }
    answer = requests.post(url, data=data)
    response = answer.json()
    for row in response['text']:
      return row

def my_function(sign):
    url = 'https://aztro.sameerkumar.website/?sign='+ sign + '&day=today'
    headers = {'Content-type': 'application/json',
            'Accept': 'application/json',
            'Content-Encoding': 'UTF-8'
            }
# aries, taurus, gemini, cancer, leo, virgo, libra, scorpio, sagittarius, capricorn, aquarius and pisces.
    data = {'sign':sign,'day':'today'}
    # print(querry)
    answer = requests.post(url, data=json.dumps(data), headers=headers)
    response = answer.json()
    #print(response)
    print(translate(sign))
    print(translate(response['current_date']))
    print('Совместимость: ' + translate(response['compatibility']))
    print('Настроение: ' + translate(response['mood']))
    print('Цвет: ' + translate(response['color']))
    print('Счасливый номер: ' + response['lucky_number'])
    print('Счасливое время: ' + response['lucky_time'])
    print(translate(response['description']))

def two_horo(sign):
    url = 'http://theastrologer-api.herokuapp.com/api/horoscope/'+sign+'/today'
    answer = requests.get(url)
    response = answer.json()
    print('Интенсивность: '+ response['meta']['intensity'])
    print('Ключевые слова: '+ translate(response['meta']['keywords']))
    print('Настроение: '+ translate(response['meta']['mood']))
    print(translate(response['horoscope']))
  
my_function('cancer')
two_horo('cancer')  
