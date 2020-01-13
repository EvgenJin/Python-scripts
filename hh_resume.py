from bs4 import BeautifulSoup
import requests
import re

def get_request (page):
  period = 5
  url = 'https://hh.ru/search/resume?text=Java&search_period=0&order_by=publication_time&search_period='+str(period)+'&page='+str(page)
  headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
  res = requests.get(url, headers=headers)
  return res

i=1
while get_request(i).status_code == 200:
  result = get_request (i)
  soup = BeautifulSoup(result.content, 'html.parser')
  data = soup.find_all('div', {'data-qa':"resume-serp__resume"})
  for item in data:
    print(item.find('a', href=True)['href'])