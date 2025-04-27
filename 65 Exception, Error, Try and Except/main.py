# exception akan terjadi saat program mengalami error saat run time

# file = open("./64 Write External File/data.txt",'r')

## contoh sederhana untuk menangkap exception

# input_user = int(input("masukkan angka : "))
# hasil = 0

# try:
#     hasil = 10/input_user
#     print(f"hasil = {hasil}")
# except:
#     print("input tidak boleh 0")

## contoh di aplikasi

# while True:
#     angka = int(input("masukkan angka pembagi: "))
#     try:
#         hasil = 10/angka
#         print(f"hasil = {hasil}")
#         is_done = input("lanjutkan (y/n)? ")
#         if is_done == "n":
#             break
#     except:
#         print("pembagi nol! silahkan masukkan input lagi")

# print("akhir dari program 1")

# implementasi exception untuk membuat file
try:
    with open("./65 Exception, Error, Try and Except/data.txt",'r') as file:
        print(file.read())    
except:
    print("file data.txt tidak ditemukan, membuat file baru")
    with open("./65 Exception, Error, Try and Except/data.txt",'w',encoding='utf-8') as file:
        file.write("new file")
        
print("akhir dari program 2")



