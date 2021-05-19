file = open("TextSamples/rus_text.txt", 'r',encoding = 'utf-8')
text=file.read()
file.close()
kolsym=0
freq=[]
symb=[]
sym=''
text1=''
for i in range(len(text)):
    if text[i].isalpha():
        if text[i].isupper():
            sym=text[i].lower()
            sym.lower()
            text1+=sym
            sym=''
        else:
            text1+=text[i]            
text=text1
for i in range(len(text)):
    if symb.count(text[i])==0:       
        kolsym=text.count(text[i])
        freq.append(kolsym)
        symb.append(text[i])
size=len(symb)
for i in range(size):
    k=freq.index(max(freq))
    print('Символ: ',symb[k],' встречается ',max(freq),' раз(а)')
    symb.remove(symb[k])
    freq.remove(freq[k])