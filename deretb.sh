echo "=============Program Deret=============="
echo "Silahkan pilih menu : "
echo ""
echo "1. Deret Aritmatika "
echo "2. Deret Pangkat"
echo "3. Deret Ganjil/Genap"
echo "0. Keluar"
echo ""
echo "Input : "
read pilihan
clear

case $pilihan in

1)
echo "=============Program Deret=============="
echo "| Deret Aritmatika |"
echo "========================================"
echo ""
echo "Program yang akan dicari : "
echo "1. Suku ke-n"
echo ""
echo "Input : "
read metode
clear

case $metode in

1)
echo "=============Program Deret=============="
echo "| Deret Aritmatika |"
echo "========================================"
echo ""
echo "Masukkan suku pertama : "
read a
suku_a=1
echo "Masukkan suku kedua : "
read b
suku_b=2
echo "-----------------------------"
echo "Berapa suku ke-n yang dicari : "
read suku_n
clear
pertama=$a
let beda=$(($a-$b))/$((suku_a-$suku_b))
let n=$(($pertama+$(($suku_n-1))*beda))
let sn=$(($suku_n/2))*$(($pertama+$n))
echo "=============Program Deret=============="
echo "| Deret Aritmatika |"
echo "========================================"
echo ""
echo "U$suku_a = $a"
echo "U$suku_b = $b"
echo ""
echo "Suku Pertama = $pertama"
echo "Beda : $beda"
echo "U$suku_n = $n"
echo ""
echo "Jumlah $suku_n suku pertama = $sn"
echo ""
echo "-------------------------------------"
tampilkan_deret $pertama $beda $suku_n
echo ""
echo "Tekan Enter untuk kembali..."
read
;;
*)
;;
esac
;;
