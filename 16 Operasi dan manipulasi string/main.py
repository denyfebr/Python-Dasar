# Operasi dan manipulasi string

# 1. menyambung string (concatenate)
nama_pertama = "Ucup"
nama_tengah = "D"
nama_akhir = "Fame"

nama_lengkap = nama_pertama + " " + nama_tengah + "'" + nama_akhir

print(nama_lengkap)

# 2. Menghitung panjang string
panjang = len(nama_lengkap)
print("panjang dari " + nama_lengkap + " = " + str(panjang))

# 3. Operator untuk string

# mengecek apakah ada komponen char atau string di string

cari = "Ucup"
status = cari in nama_lengkap
print(cari + " ada di "+ nama_lengkap + " = " + str(status))

carikecil = "ucup"
status = carikecil in nama_lengkap
print(carikecil + " ada di "+ nama_lengkap + " = " + str(status))

carikecil1 = "ucup"
status = carikecil1 not in nama_lengkap
print(carikecil1 + " tidak ada di "+ nama_lengkap + " = " + str(status))