from datetime import datetime
import numpy as np
#посчитает цену выхода на работу в нерабочий день
uinpt = None
while uinpt != 'n':
  oklad = int(input("Укажи оклад: "))
  hours = int(input("Сколько часов работать?: "))
  day1 = datetime.today().replace(day=1).strftime("%Y-%m-%d")
  day2 = datetime.today().replace(day=31).strftime("%Y-%m-%d")
  days = np.busday_count(day1, day2)
  hour_cost = oklad / (days * 8)
  summ = (hour_cost*2*hours).round()
  print("Цена выходного дня "+str(summ) + " руб. за " + str(hours) + " часов")
  uinpt = input("Повторить расчет y/n ?")
else:
    print("Хорошего дежурства!!")  
