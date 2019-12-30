from bs4 import BeautifulSoup
import requests
import re 
tds = []
url = 'https://everymac.com/ultimate-mac-lookup/?search_keywords=md388'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
result = requests.get(url, headers=headers)
#print(result.content.decode())
# soup = BeautifulSoup(result.content.decode())
# film_list = soup.find('table', {'id': 'content6-title'})
# print(film_list)
soup = BeautifulSoup(result.content, 'html.parser')
main = soup.find('td',class_="detail_info")
date_start = main.select('td')[1]
date_end = main.select('td')[3]
model = main.select('td')[5] #main.select('td')[7]
gen = main.select('td')[9]
id = main.select('td')[11]
ram = main.select('td')[14]
hdd = main.select('td')[17]
url_details = 'https://everymac.com' + main.find('a', href=True)['href']

result_next = requests.get(url_details, headers=headers)
soup_next = BeautifulSoup(result_next.content, 'html.parser')
el_arr = soup_next.select('div > table > tr > td') 
count_cpu = el_arr[7].get_text()
gb2_sc = el_arr[12].get_text() + ' ' + el_arr[13].get_text() 
gb2_mc = el_arr[14].get_text() + ' ' + el_arr[15].get_text() 
gb3_32_sc = el_arr[18].get_text() + ' ' + el_arr[19].get_text()
gb3_32_mc = el_arr[20].get_text() + ' ' + el_arr[21].get_text() 
gb3_64_sc = el_arr[24].get_text() + ' ' + el_arr[25].get_text() 
gb3_64_mc = el_arr[26].get_text() + ' ' + el_arr[27].get_text() 
gb4_sc = el_arr[30].get_text() + ' ' + el_arr[31].get_text() 
gb4_mc = el_arr[32].get_text() + ' ' + el_arr[33].get_text() 
cpu_speed = el_arr[37].get_text() 
cpu_type = el_arr[39].get_text()
# print(gb4)

manufactory_date = el_arr[13].get_text()


# print(manufactory_date.get_text())
# soup.find_all('p', class_='outer-text')
# main = soup.find_all('div',id="contentcenter_specs_table")
# print(main)
# for row in main:
  # t1 = row.find_all('table',id="specs1-title")
  # print(t1.find('td'))
  # r = row.findall('div',id="contentcenter_specs_table_pairs")
  # print(r)
  # for rec in r:
    # date_man = re.findall(r'(?<=<td>)(.*)(?=</td>)',str(rec.find_all('td')[1]))
    # print(str(date_man))
# phone = str(tds[1][1])
# print(phone)
# for row in rows:          # Print all occurrences

    # print(row.get_text())
#print(soup.prettify())
# print(t)
