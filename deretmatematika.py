print('''
     ****************************************************
     *                     안녕하세요                   *
     *    Selamat Datang di Program Deret Matematika    *  
     ****************************************************
  ''')

def pilihan():
  print("Mau menghitung apa???")
  print("1. Deret Aritmatika")
  print("2. Deret Geometri")
  print("3. Exit")
pilihan()
print("+++++++++++")
pilih = int(input("Silahkan pilih menu deret: "))
print("+++++++++++")

while pilihan:
  if pilih == 1: 
    print("<<Deret Aritmatika>>")
    a = int(input("suku pertama: "))
    b = int(input("beda: "))
    n = int(input("jumlah suku: "))
    print("a => ", a)
    print("b => ", b)
    print("n => ", n)
    print("++++++++")
    Un = a + (n-1)*b
    Sn = n/2 * (2*a + (n-1)*b)
    print(">> Nilai Un adalah: ", Un)
    print(">> Nilai Sn adalah: ", Sn)
    break

  elif pilih == 2:
    print("<<Deret Geometri>>")
    a = int(input("suku pertama: "))
    r = int(input("rasio: "))
    n = int(input("jumlah suku: "))
    print("a => ", a)
    print("r => ", r)
    print("n => ", n)
    print("++++++++")
    Un = a * (r**(n-1))
    Sn = a * (1-r**n) / (1 - r)
    print(">> Nilai Un adalah: ", Un)
    print(">> Nilai Sn adalah: ", Sn)
    break

  elif pilih == 3:
    print("gomawo chinguya")
    break
