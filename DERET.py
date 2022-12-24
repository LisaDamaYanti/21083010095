print("*******************************************************")
print("*                                                     *")
print("*                   DERET MATEMATIKA                  *") 
print("*                                                     *")
print("*******************************************************") 

print("mau ngitung apanih?")

def pilihan():
   print("1.Menghitung Sn Deret Aritmatika")
   print("2.Menghitung Sn Deret Geometri  ")
   print("3.keluar                        ")
pilihan()
pilih = input("Masukkan pilihan: ")

print("**********Deret Aritmatika**********") 
a = int (input("suku pertama: "))
b = int (input("beda: "))
n = int (input("banyak suku: "))

print("**********Deret Geometri**********") 
r = int(input("Masukkan rasio deret: "))
a = int(input("Masukkan suku pertama: "))
n = int(input("Masukkan jumlah suku yang ingin dicari: "))

if pilih == "1":
Sn = (n / 2) * (2 * a + (n - 1) * b)
print("Nilai S ke", n  "adalah:", Sn)

else:
Sn = a1 * (r ** n - 1) / (r - 1)
print("Nilai S ke", n, "adalah: ", Sn)
