choice = 0
while True:
    ing=input('ingin melihat hasil [y/t]?')
    if ing=='y':
        cari=input('cari berdasarkan lahan/daerah:')
        for n in range(i):
            if cari==lahan[n]:
                print()
                print('daerah :',daerah[n])
                print('lahan  :',lahan[n])
                print()
                i+1
            elif cari==daerah[n]:
                print()
                print('daerah :',daerah[n])
                print('lahan  :',lahan[n])
                print()
        continue 
    elif ing=='t':
        break
