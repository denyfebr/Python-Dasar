## Tutorial membaca file external

print(3*"="," Membaca file txt ",3*"=")
file = open("./63 Read External File/data.txt",mode="r")

print(f"status read : {file.readable()}")
print(f"status write : {file.writable()}")

# baca seluruh file
print(file.read())

# baca baris per-baris
# print(file.readline()) # baca baris pertama
# print(file.readline()) # baca baris kedua

## baca semua baris sebagai list
# print(file.readlines())

print(f"Apakah file sudah diclose : {file.closed}")
file.close()
print(f"Apakah file sudah diclose : {file.closed}")

## salah satu teknik membuka file di python

print("\n",3*"="," Membaca file txt dengan with",3*"=")

with open("./63 Read External File/data.txt",mode="r") as file:
    content = file.readline()
    print(content,end="")
    print(f"Apakah file sudah diclose : {file.closed}")

print(f"Apakah file sudah diclose : {file.closed}")