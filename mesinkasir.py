
def listMakanan():
    print('SELAMAT DATANG DI RUMAH MAKAN')
    print('====================')
    print('DAFTAR LIST MAKANAN')
    print('1.NASI AYAM GORENG --- Rp.15000')
    print('2.NASI RAMES --- Rp.12000')
    print('3.NASI IKAN BAKAR --- Rp.14000')
    print('4.NASI IKAN GORENG --- Rp.12000')
    print('5.NASI DAGING KAMBING --- Rp.20000')
    print('6.NASI KIKIL --- Rp.15000')
    print('====================')

listMakanan()

listMakanan1 = [
    'NASI AYAM GORENG',
    'NASI RAMES',
    'NASI IKAN BAKAR',
    'NASI IKAN GORENG',
    'NASI DAGING KAMBING',
    'NASI KIKIL'
]


def listMinuman():
    print('SILAHKAN PILIH MENU MINUMAN')
    print('====================')
    print('DAFTAR LIST MINUMAN')
    print('1.ES TEH --- Rp.5000')
    print('2.ES JERUK --- Rp.6000')
    print('3.ES COCACOLA --- Rp.5000')
    print('4.ES SODA GEMBIRA --- Rp.7000')
    print('5.ES KOPI --- Rp.5000')
    print('6.ES KELAPA --- Rp.8000')
    print('====================')

listMinuman()

listMinuman1 = [
    'ES TEH',
    'ES JERUK',
    'ES COCACOLA',
    'ES SODA GEMBIRA',
    'ES KOPI',
    'ES KELAPA'
]


def hargaMakanan():
    return int(input('MASUKKAN MAKANAN YANG DIBELI 1-6: '))


pilihanMakanan = hargaMakanan()

jumlahMakanan = int(input('MAU PESAN BERAPA PORSI: '))

if pilihanMakanan == 1:
    hargaMakananDipilih = 15000
elif pilihanMakanan == 2:
    hargaMakananDipilih = 12000
elif pilihanMakanan == 3:
    hargaMakananDipilih = 14000
elif pilihanMakanan == 4:
    hargaMakananDipilih = 12000
elif pilihanMakanan == 5:
    hargaMakananDipilih = 20000
elif pilihanMakanan == 6:
    hargaMakananDipilih = 15000
else:
    hargaMakananDipilih = 0
    print('HARGA TIDAK VALID')

totalMakanan = hargaMakananDipilih * jumlahMakanan

if hargaMakananDipilih > 0:
    print(f"KAMU MEMBELI MAKANAN {listMakanan1[pilihanMakanan-1]} SEBANYAK {jumlahMakanan} PORSI. TOTAL HARGA MAKANAN KAMU SEBESAR Rp{totalMakanan}")


def hargaMinuman():
    return int(input('MASUKKAN MINUMAN YANG DIBELI 1-6: '))


pilihanMinuman = hargaMinuman()

jumlahMinuman = int(input('MAU PESAN BERAPA GELAS: '))

if pilihanMinuman == 1:
    hargaMinumanDipilih = 5000
elif pilihanMinuman == 2:
    hargaMinumanDipilih = 6000
elif pilihanMinuman == 3:
    hargaMinumanDipilih = 5000
elif pilihanMinuman == 4:
    hargaMinumanDipilih = 7000
elif pilihanMinuman == 5:
    hargaMinumanDipilih = 5000
elif pilihanMinuman == 6:
    hargaMinumanDipilih = 8000
else:
    hargaMinumanDipilih = 0
    print('HARGA TIDAK VALID')

totalMinuman = hargaMinumanDipilih * jumlahMinuman

if hargaMinumanDipilih > 0:
    print(f"KAMU MEMBELI MINUMAN {listMinuman1[pilihanMinuman-1]} SEBANYAK {jumlahMinuman} GELAS. TOTAL HARGA MINUMAN KAMU SEBESAR Rp{totalMinuman}")


def total():
    return totalMinuman + totalMakanan

totalSemua = total()

print(f"TOTAL HARGA MINUMAN SEBESAR Rp{totalMinuman} DAN TOTAL HARGA MAKANAN SEBESAR Rp{totalMakanan}. DAN TOTAL SEMUA HARGA SEBESAR Rp{totalSemua}")

uang = int(input(f"TOLONG MASUKKAN UANG SEBESAR Rp{totalSemua}: "))

if uang == totalSemua:
    print(f"UANG KAMU SEBESAR Rp{uang} DAN TOTAL SEMUA SEBESAR Rp{totalSemua}. UANG KAMU PAS")
elif uang > totalSemua:
    print(f"UANG KAMU SEBESAR Rp{uang} DAN TOTAL SEMUA SEBESAR Rp{totalSemua}. UANG KEMBALIAN TERSISA Rp{uang - totalSemua}")
else:
    print(f"UANG KAMU SEBESAR Rp{uang} DAN TOTAL SEMUA SEBESAR Rp{totalSemua}. UANG KAMU KURANG SEBESAR Rp{totalSemua - uang}")
