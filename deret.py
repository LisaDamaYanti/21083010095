print("*****************************************************")
print("*                                                   *")
print("*                   DERET GEOMETRI                  *") 
print("*                                                   *")
print("*****************************************************") 

print("mau ngitung apanih?")

def pilihan():
   print("1.Menghitung Un")
   print("2.Menghitung Sn")

pilihan()
pilih = input("Masukkan pilihan: ")

a = print(int(input("Masukkan suku pertama: "))) 
r = print(int(input("Masukkan rasio deret: "))) 
n = print(int(input("Masukkan jumlah suku: "))) 

if pilih == 1:
  pangkat = n-1
  Un = a * (r**pangkat)
  print("Nilai U ke", n, "adalah: ", Un)
else:
  penyebut = r-1
  pembilang = a * ((r ** n)-1)
  Sn = pembilang / penyebut
  print("Nilai S ke", n, "adalah: ", Sn)
