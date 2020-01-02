# -*- coding: UTF-8 -*-
import requests
import json
import pandas as pd
from pandas.io.json import json_normalize

import sys

def get_request (page):
  q = str(sys.argv[1])
  area = str(sys.argv[2])
  url = 'https://api.hh.ru/vacancies?area='+str(area)+'&page='+str(page)+'&per_page=10&text='+q
  res = requests.get(url)
  return res

i=1
df = pd.DataFrame()
while get_request(i).status_code == 200 and len(get_request(i).json()['items']) > 0:
  json_data = get_request(i).json()
  norm = json_normalize(json_data['items'])
  dfi = pd.DataFrame(norm)
  # print('page :' + str(i) + ' length :' + str(len(get_request(i).json()['items'])))
  df = pd.concat([df,dfi],sort=False)
  i = i + 1
# print(df[(df['salary.from'] > 0) & (df['salary.to'] > 0)][['name','employer.name','salary.from','salary.to','published_at','alternate_url']])
# print(df[df['salary.from'] > 0][['name','employer.name','salary.from','salary.to','published_at','alternate_url']])
# print(df[['name','employer.name','salary.from','salary.to','published_at','alternate_url']])
print(df.agg({'salary.from':['mean','median','count']}))
#df[df['salary.from'] > 0][['name','employer.name','salary.from','salary.to','published_at','alternate_url','snippet.requirement','snippet.responsibility']].to_csv('file.csv',encoding='utf-8-sig',sep=';')


