import requests
import json
uinpt = None

while uinpt != 'n':
  querry = input("Что переводить?: ")
  url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
  headers = {'Content-type': 'application/json',
          'Accept': 'application/json',
          'Content-Encoding': 'UTF-8'
          }
  data = {'lang':'en-ru'
          ,'key': 'trnsl.1.1.20190814T072216Z.1d484639e7b367bd.97e836b16a42bde09b118163f3afa6054de5429f'
          ,'format':'plain'
          ,'text':querry
          }
  answer = requests.post(url, data=data)
  response = answer.json()
  for row in response['text']:
    print(row)
  uinpt = input("Повторим y/n ?")  
else:
    print("Good luck!")


