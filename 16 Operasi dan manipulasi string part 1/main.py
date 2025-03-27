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

# mengulang string
print("wk"*10)
print(15*"wk")

# indexing
print("index ke-0 : "+nama_lengkap[0])
print("index ke-1 : "+nama_lengkap[1])
print("index ke-6 : "+nama_lengkap[6])
print("index ke- -1 : "+nama_lengkap[-1])
print("index ke- -2 : "+nama_lengkap[-2])
print("index ke-[0:4] : "+nama_lengkap[0:4])
print("index ke-[3:8] : "+nama_lengkap[3:8])
print("index ke-[0,2,4,6,8,10] : "+nama_lengkap[0:11:2])

# item paling kecil
print("paling kecil : " + min(nama_lengkap))

# item paling besar
print("paling besar : " + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII code dari ",min(nama_lengkap),": ",str(ascii_code))

data_char = 117
print("Karakter dari ASCII code ",data_char,": ",chr(data_char))

# 4. operator dalam bentuk method

data = "otong surotong pararotong"
jumlah = data.count("o")
print("jumlah o pada "+ data + " = "+str(jumlah))
