# Lambda function

def f_kuadrat(angka):
    return angka**2

print(f"hasil fungsi kuadrat = {f_kuadrat(3)}")

# kita coba dengan lambda
# output = lambda argument: expression
kuadrat = lambda angka:angka**2
print(f"hasil lambda kuadrat = {f_kuadrat(5)}")

pangkat = lambda num,pow : num**pow
print(f"hasil lambda pangkat = {pangkat(9,2)}")

## kegunaanya apa lambda ini?

# sorting berdasarkan alphabet untuk list
data_list = ["Otong","Ucup","Dudung"]
print(f"data list = {data_list}")
data_list.sort()
print(f"sorted list = {data_list}")

# sorting berdasarkan panjang karakter untuk list
def panjang_nama(nama):
    return len(nama)

data_list.sort(key=panjang_nama)
print(f"sorted list panjang karakter dengan fungsi = {data_list}")

data_list.sort(key=len)
print(f"sorted list panjang karakter = {data_list}")

# sort pakai lambda
data_list = ["Otong","Ucup","Dudung"]

data_list.sort(key=lambda nama:len(nama))

print(f"sorted list panjang karakter by lambda = {data_list}")

# filter pakai fungsi
data_angka = [1,2,3,4,5,6,7,8,9,10,11,12]

def kurang_dari_lima(angka):
    return angka < 5

data_angka_baru = list(filter(kurang_dari_lima,data_angka))
print(data_angka_baru)

data_angka = [1,2,3,4,5,6,7,8,9,10,11,12]
data_angka_baru = list(filter(lambda x:x < 7,data_angka))
print(data_angka_baru)

# kasus genap
data_angka = [1,2,3,4,5,6,7,8,9,10,11,12]
data_angka_genap = list(filter(lambda x:x % 2 == 0,data_angka))
print(data_angka_genap)

# kasus ganjil
data_angka = [1,2,3,4,5,6,7,8,9,10,11,12]
data_angka_ganjil = list(filter(lambda x:x % 2 != 0,data_angka))
print(data_angka_ganjil)

# kasus kelipatan 3
data_angka = [1,2,3,4,5,6,7,8,9,10,11,12]
data_angka_tiga = list(filter(lambda x:x % 3 == 0,data_angka))
print(data_angka_tiga)

# anonymous function
# currying <- Haskell Curry

# Fungsi biasa
def pangkat(angka,pow):
    hasil = angka**pow
    return hasil

data_hasil = pangkat(5,2)
print(f"hasil dari fungsi biasa = {data_hasil}")

# dengan currying/anonymous function

def pangkat(n):
    return lambda angka:angka**n

pangkat_dua = pangkat(2)
print(f"pangkat 2 menggunakan anonymous = {pangkat_dua(5)}")

pangkat_tiga = pangkat(3)
print(f"pangkat 3 menggunakan anonymous = {pangkat_tiga(5)}")

print(f"pangkat bebas menggunakan anonymous = {pangkat(4)(5)}")
