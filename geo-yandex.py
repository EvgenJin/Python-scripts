import requests
import json
# url = 'http://geocode-maps.yandex.ru/1.x/?key=AMsJFVIBAAAA6b1EZgIARt3xxKvqDXFSuzYNLrfjJlyduEsAAAAAAAAAAABtEHh2MEhJiiNct5e0zKVyv2ggKA==&geocode=Екатеринбург Уральская 3 225&format=json'
url = 'http://geocode-maps.yandex.ru/1.x/?'
key='AMsJFVIBAAAA6b1EZgIARt3xxKvqDXFSuzYNLrfjJlyduEsAAAAAAAAAAABtEHh2MEhJiiNct5e0zKVyv2ggKA=='
geocode='Екатеринбург Уральская 3 225'
frmat='json'
url_complete = url+'key='+key+'&'+'geocode='+geocode+'&'+'format='+frmat
# print(url_complete)
answer = requests.get(url_complete)
response = answer.json()

print(response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['Address']['Components'])
# response = answer.json()
    # print(querry)
    # answer = requests.get(url)
    # answer = requests.post(url, data=json.dumps(data), headers=headers)
    # response = answer.json()

