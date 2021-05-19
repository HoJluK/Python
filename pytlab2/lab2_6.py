import os, datetime, shutil
def reorgonize(source,days,size):
    if os.path.exists(source+'\\Archive'):
        shutil.rmtree(source+'\\Archive')        
    if os.path.exists(source+'\\Small'):
        shutil.rmtree(source+'\\Small')
    listfiles=[]
    now=datetime.datetime.now()
    folders=os.walk(source)
    for way,dirs,files in folders:
        for f in files:
            listfiles.append(way+'\\'+f)        
    for i in range(len(listfiles)):
        stat=datetime.datetime.fromtimestamp(os.stat(listfiles[i]).st_mtime)
        if ((now-stat).days)>days:
            if os.path.exists(source+'\\Archive')==False:
                os.mkdir(source+'\\Archive')
            shutil.copy(listfiles[i],source+'\\Archive')
        if os.stat(listfiles[i]).st_size<size:
            if os.path.exists(source+'\\Small')==False:
                os.mkdir(source+'\\Small')
            shutil.copy(listfiles[i],source+'\\Small')
    print(listfiles)
    delete=input("Удалить отсортированные файлы? y/n: ")
    if delete=='y':
        for i in listfiles:
            os.remove(i)
        print("Отсортированные файлы удалены!")
    else:
        print("Отсортированные файлы не удалены!")
reorgonize(r'D:\Laboratory_pr\питон',14,15000)