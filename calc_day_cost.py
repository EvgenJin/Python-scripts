from datetime import datetime
import numpy as np
import calendar
#посчитает цену выхода на работу в нерабочий день
uinpt = None
while uinpt != 'n':
  #расчет последнего дня в тек месяце
  m = datetime.today().strftime("%m")
  y = datetime.today().strftime("%Y")
  _, num_days = calendar.monthrange(int(y), int(m))
  oklad = int(input("Укажи оклад: "))
  hours = int(input("Сколько часов работать?: "))
  day1 = datetime.today().replace(day=1).strftime("%Y-%m-%d")
  day2 = datetime.today().replace(day=num_days).strftime("%Y-%m-%d")
  days = np.busday_count(day1, day2)
  hour_cost = oklad / (days * 8)
  summ = (hour_cost*2*hours).round()
  print("Цена выходного дня "+str(summ) + " руб. за " + str(hours) + " часов" + "; Рабочих дней в месяце: " + str(days))
  #print("Рабочих дней в месяце: " + days )
  uinpt = input("Повторить расчет y/n ?")
else:
    print("Хорошего дежурства!!")  
