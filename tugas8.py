# import library
from os import getpid
from time import time, sleep
from multiprocessing import cpu_count, Pool, Process

# inisialisasi fungsi
def tetapkan(i):
   if i % 2 == 0:
      print(i+1, "Genap - ID proses", getpid())
   else:
      print(i+1, "Ganjil - ID proses", getpid())
   sleep(1)

# input
a = int(input("Input:\n"))

print("\nOutput:")

print("\nSekuensial")
sekuensial_awal = time()

for i in range (a):
  tetapkan(i)

sekuensial_akhir = time()


print("\nmultiprocessing.Process")
kumpulan_proses = []

process_awal = time()

for i in range (a):
   p = Process(target=tetapkan, args=(i,))
   kumpulan_proses.append(p)
   p.start()

for i in kumpulan_proses:
   p.join()

process_akhir = time()


print("\nmultiprocessing.Pool")
pool_awal = time()

pool = Pool()
pool.map(tetapkan, range(a))
pool.close

pool_akhir = time()


#perbandingan waktu
print("\nWaktu eksekusi sekuensial :", sekuensial_akhir - sekuensial_awal, "detik")
print("Waktu eksekusi multiprocessing.Process:", process_akhir - process_awal, "detik")
print("Waktu eksekusi multiprocessing.Pool:", pool_akhir - pool_awal, "detik")


