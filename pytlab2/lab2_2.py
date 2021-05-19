import os 
import hashlib 
 
ellist=os.walk(r'D:\Laboratory_pr\питон') 
filelist=[] 
filecount=[] 
for el in ellist: 
    if el[1]!=0: 
        for e in el[2]: 
            filelist.append(el[0]+'\\'+e) 
 
for file in filelist: 
    with open(file, 'rb') as f: 
        content = f.read() 
        f.close() 
        filecount.append(hashlib.md5(content).hexdigest()) 
 
for i in range(0,len(filelist)-1): 
    for j in range(i+1,len(filelist)): 
        if filecount[i]==filecount[j]: 
            print(filelist[i],'=',filelist[j])