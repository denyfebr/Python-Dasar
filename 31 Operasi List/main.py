## ----Operasi List----

data_angka = [1,5,1,4,3,2,4,3,2,3,7,8,9,0]

print(f"data angka = \n{data_angka}")

# count data spesifik

jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)

print(f"jumlah data berisi angka 4 = {jumlah_data_4}")
print(f"jumlah data berisi angka 3 = {jumlah_data_3}")

data_string = ["Ucup","Otong","Dudung","Ujang","Otong","Rozak","Dudung"]
jumlah_data_otong = data_string.count("Otong")

print(f"Jumlah otong = {jumlah_data_otong}")

data = ["Ucup","Otong","Dudung","Ujang"]
print(f"data = {data}")

# untuk mengetahui index mana data tersebut
index_dudung = data.index("Dudung")
index_ujang = data.index("Ujang")
print(f"index Dudung = {index_dudung}")
print(f"index Ujang = {index_ujang}")

# menurutkan list
print(f"data angka sebelum diurutkan = \n{data_angka}")
data_angka.sort()
print(f"data angka setelah diurutkan = \n{data_angka}")

print(f"data string sebelum diurutkan = \n{data_string}")
data_string.sort()
print(f"data angka setelah diurutkan = \n{data_string}")

# urutan dibalik
data_angka.reverse()
print(f"data angka setelah diurutkan lalu dibalik = \n{data_angka}")
data_string.reverse()
print(f"data string setelah diurutkan lalu dibalik = \n{data_string}")


