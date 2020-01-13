from bs4 import BeautifulSoup
import requests
import re

file1 = open("myfile.txt","w") 
def get_all (page):
  period = 7
  area = 3
  querry = 'Java'
  url = 'https://hh.ru/search/resume?text='+querry +'&clusters=true&order_by=publication_time&no_magic=false&st=resumeSearch&logic=normal&pos=keywords&specialization=1&order_by=publication_time&exp_period=all_time&area=' + str(area) + '&search_period='+str(period)+'&page='+str(page)
  headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
  res = requests.get(url, headers=headers)
  soup_all = BeautifulSoup(res.content, 'html.parser')
  data_all = soup_all.find_all('div', {'data-qa':"resume-serp__resume"})  
  # print(res.status_code)
  return data_all

def get_one(id):
  url = 'https://hh.ru'+id
  headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
  res = requests.get(url, headers=headers)
  return res

# soup_all = BeautifulSoup(get_all(1).content, 'html.parser')
# data_all = soup_all.find_all('div', {'data-qa':"resume-serp__resume"})
# print(len(data_all))
# for item in data_all:
  # print(item.find('a', href=True)['href'])


i=0
while len(get_all(i)) > 0:
  result_all = get_all(i)
  # soup_all = BeautifulSoup(result_all.content, 'html.parser')
  # data_all = soup_all.find_all('div', {'data-qa':"resume-serp__resume"})
  i = i + 1
  # print(result_all)
  for item in result_all:
    print(item.find('a', href=True)['href'])
    # file1.write(item.find('a', href=True)['href'] + '\n') 
# file1.close()  
  #   id = item.find('a', href=True)['href']
  #   result_one = get_one(id)
  #   soup_one = BeautifulSoup(result_one.content, 'html.parser')
  #   title = soup_one.find('span',class_='resume-block__title-text resume-block__title-text_position').find("span").get_text()
  #   salary_tag = soup_one.find('span',class_='resume-block__salary resume-block__title-text_salary')
  #   if salary_tag:
  #     salary = salary_tag.get_text()

    # print(title + ' ' + salary)
    # print(id)



