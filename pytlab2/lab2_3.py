import os
import path
files = [src + '\\' + file_ for src, dir_, files in os.walk(os.getcwd() + '\\music') for file_ in files if file_.endswith('.mp3')]
print(files, '\n')
f = open('music\\music.txt', 'r', encoding = 'utf-8')
txt = [line.rstrip('\n') for line in f]
index = 0
for line in txt:
    name = path.splitext(path.basename(files[index]))[0]
    if name in line:
        os.rename(f'music\\{name}.mp3', f'music\\{line}.mp3')
    index += 1
files = [src + '\\' + file_ for src, dir_, files in os.walk(os.getcwd() + '\\music') for file_ in files if file_.endswith('.mp3')]
print(files)
f.close()