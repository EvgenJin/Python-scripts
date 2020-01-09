from datetime import date, timedelta, datetime
import numpy as np
import calendar
import requests
#посчитает цену выхода на работу в нерабочий день

def get_request (q):
  url = 'https://isdayoff.ru/'+q
  res = requests.get(url)
  return res.json()

def calc_days(day1,day2):
  delta = timedelta(days=1)
  days = 0
  while day1 <= day2:
    res = get_request(day1.strftime("%Y%m%d"))
    day1 += delta
    days = days + res
  return days  

uinpt = None
while uinpt != 'n':
  #расчет последнего дня в тек месяце
  m = datetime.today().strftime("%m")
  y = datetime.today().strftime("%Y")
  _, num_days = calendar.monthrange(int(y), int(m))
  oklad = int(input("Укажи оклад: "))
  hours = int(input("Сколько часов работать?: "))
  day1 = datetime.today().replace(day=1) #.strftime("%Y-%m-%d")
  day2 = datetime.today().replace(day=num_days) #.strftime("%Y-%m-%d")
  days = calc_days(day1,day2)
  hour_cost = oklad / (days * 8)
  summ = int(hour_cost*2*hours)#.round()
  print("Цена выходного дня "+str(summ) + " руб. за " + str(hours) + " часов" + "; Рабочих дней в месяце: " + str(days))
  #print("Рабочих дней в месяце: " + days )
  uinpt = input("Повторить расчет y/n ?")
else:
    print("Хорошего дежурства!!")  
