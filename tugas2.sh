#1/bin/bash

echo -n "Masukkan harga"
read harga

if [ $harga -gt 200000 ]
then
  echo "Kamu mendapatkan diskon 4%"
elif [ $harga -eq 50000 ]
then
  echo "Kamu mendapatkan kupon undian"
else 
  echo "Kamu membayar $harga ribu"
fi
