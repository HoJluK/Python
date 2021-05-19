import re  
file=open('lab2_4.txt','r') 
text=file.read() 
file.close() 
line=text.split("\n") 
p = re.compile('(\b?[0-1][0-9]-[0-5][0-9]-[0-5][0-9][0-5][0-9]\b?)|(\b?[0-1][0-9]:[0-5][0-9]:[0-5][0-9][0-5][0-9]\b?)')
for i in range(len(line)):
    a=re.search(p,line[i]) 
    if a!=None: 
        print('Строка:',i+1,'Позиция:',a.span()[0]+1)