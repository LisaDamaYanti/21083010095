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

print("mau ngitung apa nih?")

def pilihan():
  print("1. Menghitung Un")
  print("2. Menghitung Sn")
pilihan()
pilih = input("Masukkan pilihan: ")

r = int(input("Masukkan rasio deret: "))
a1 = int(input("Masukkan suku pertama: "))
n = int(input("Masukkan jumlah suku yang ingin dicari: "))


if pilih == 1:
  Un = a1 * r**(n-1)
  print("Suku ke-n deret geometri adalah:", Un)
else:
  Sn = a1 * (r**n - 1) / (r - 1)
  print("Jumlah deret geometri adalah:", Sn)
