# -*- coding: UTF-8 -*-
import csv
import difflib

def similarity(s1, s2):
  normalized1 = s1.lower()
  normalized2 = s2.lower()
  matcher = difflib.SequenceMatcher(None, normalized1, normalized2)
  return matcher.ratio()

def compare_str(p_str,p_id):
  with open('table2.csv','r') as fp:
    i = 0
    reader_ikar = csv.DictReader(fp, delimiter=';', quotechar='"')
    data_ikar = [r for r in reader_ikar]
    for row in data_ikar:
      ikar = row['Region']+' '+row['Area']+' '+row['City']+' '+row['District']+' '+row['Complex']+' '+row['Street']+' '+row['Corpus']+' '+row['Corpus2']+' '+row['Home']
      if similarity(ikar,p_str) > 0.6:
        res_file.write(p_str + ';' + p_id + ';' + ikar+';'+row['id'] + ';' + str(similarity(ikar,p_str)) + '\n')
        
res_file = open('res.csv','w')
res_file.write('Адрес в инверсии;ид инверсии;Адрес икар;ид икар;% совпадения;\n')
with open('table1.csv','r') as fp:
  i = 0
  reader_inv = csv.DictReader(fp, delimiter=';', quotechar='"')  
  data_inv = [r for r in reader_inv]
  for r in data_inv:
    compare_str(r['ADDRESS_STR'],r['ID'])
    i += 1
    print(i)
res_file.close()
