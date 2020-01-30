# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
url = 'https://receive-sms-online.com/r/+79653944057.php'
res = requests.get(url)
soup_one = BeautifulSoup(res.content, 'html.parser')
data = soup_one.findAll(['ttbody','tr'])
i = 0
for item in data:
    cols=item.find_all('td')
    cols=[x.text.strip().replace(u'\xa0', u' ').replace(u'\u200b', u' ') for x in cols]
    if len(cols) > 0 :
      print(cols)
      i += 1
      if i == 5:
        break
