print("*****************************************************")
print("*                                                   *")
print("*                   DERET GEOMETRI                  *") 
print("*                                                   *")
print("*****************************************************")


print("mau ngitung apa nih?")

def pilihan():
  print("1. Menghitung Un")
  print("2. Menghitung Sn")
pilihan()
pilih = input("Masukkan pilihan: ")

r = int(input("Masukkan rasio deret: "))
a1= int(input("Masukkan suku pertama: "))
n = int(input("Masukkan jumlah suku yang ingin dicari: "))

if pilih =="1":
  pangkat = n-1
  Un = a1 * (r**pangkat)
  print("Nilai U ke", n, "adalah: ", Un)

else:
  penyebut = r - 1
  pembilang = a1 * ((r ** n)-1)  
  Sn = pembilang / penyebut
  print("Nilai S ke", n, "adalah: ", Sn)
