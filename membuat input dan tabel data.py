i=0
daerah=[]
lahan=[]
while True:
    print('masukkan data ke-',i+1)
    daerah.append(input('daerah:'))
    lahan.append(input('tipe lahan :'))
    lagi=''
    while lagi!='y' and lagi!='t':
        lagi=input('INPUT LAGI [y/t]:')
        i+=1
    if lagi=='t':
        break
print("             DAERAH DAN TIPE LAHAN")
print("===================================================")
print("no ||      nama daerah      ||      tipe lahan   ||")
print("===================================================")
for n in range (i):
    print(n+1,' ', daerah[n],'                       ',lahan[n],'')
    print()
    print()
