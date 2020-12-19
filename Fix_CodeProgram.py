#Class
class pendataan_lahan():
    daerah = ""
    lahan = ""
    judul = ""

    def __init__ (self, judul):
        self.judul = judul

    def get_lahan (self, daerah):
        self.daerah = daerah
    
    def get_daerah (self, lahan):
        self.lahan = lahan
       
    def get_output(self):
        print ("\n\n",self.judul)
        print ("Daerah : ",self.daerah)
        print ("Tipe Lahan : ", self.lahan)
#PROGRAM UTAMA
obj = pendataan_lahan("DATA DAERAH DAN TIPE LAHAN")
i=0
daerah=[]
lahan=[]
while True:
    print('masukkan data ke-',i+1)
    daerah.append(input('Nama Daerah : '))
    lahan.append(input('Tipe lahan : '))
    lagi=''
    while lagi!='y' and lagi!='t':
        lagi=input('INPUT LAGI [Y/T]:')
        i+=1
    if lagi=='t':
        break
print("            DATA DAERAH DAN TIPE LAHAN")
print("===================================================")
print("no ||      Nama Daerah      ||      Tipe Lahan   ||")
print("===================================================")
for n in range (i):
    print(n+1,' ', daerah[n],'                       ',lahan[n],'')
    print()
    print()
choice = 0
while True:
    ing=input('ingin melihat hasil [y/t]?')
    if ing=='y':
        cari=input('cari berdasarkan lahan/daerah:')
        for n in range(i):
            if cari == lahan[n]:
                print()
                obj.get_daerah(daerah[n])
                obj.get_lahan(lahan[n])
                obj.get_output()
                print()
                i+1
            elif cari==daerah[n]:
                print()
                obj.get_daerah(daerah[n])
                obj.get_lahan(lahan[n])
                obj.get_output()
                print()
        continue 
    elif ing=='t':
        print('')
        print("============== EXIT ==============")
        print('')
        break
