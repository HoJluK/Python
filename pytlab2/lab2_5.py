import re
#text=input('Введите текст: ')
text='Getr12 Hfadvjde Remont8452 nauxnikov124 Hggre2 Gghjkl964891 Huawei9'
result=re.findall(r'[A-Z][a-z]+[0-9]{2,4}\b',text)
print(result)