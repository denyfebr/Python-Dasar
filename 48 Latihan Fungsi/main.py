'''Latihan Fungsi'''
import os

# program menghitung luas dan keliling persegi panjang

# membuat header program

# os.system("cls")
# print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
# print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
# print(f"{"-"*40:^40}")

# # Mengambil input user
# panjang = float(input("Masukkan Panjang : "))
# lebar = float(input("Masukkan Lebar : "))

# # Program menghitung luas
# luas = panjang*lebar
# keliling = 2*(panjang+lebar)

# # Tampilkan hasilnya
# print(f"hasil perhitungan luas = {luas}")
# print(f"hasil perhitungan keliling = {keliling}")

def header():
    '''Header'''
    os.system("cls")
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{"-"*40:^40}")

def input_user():
    panjang = float(input("Masukkan Panjang : "))
    lebar = float(input("Masukkan Lebar : "))
    return panjang,lebar
    
def hitung_luas(panjang,lebar):
    luas = panjang*lebar
    return luas

def hitung_keliling(panjang,lebar):
    keliling = 2*(panjang+lebar)
    return keliling

def menampilkan_hasil(opsi,luas,keliling):
    if opsi == 1:
        print(f"hasil perhitungan luas = {luas}")
    elif opsi == 2:
        print(f"hasil perhitungan keliling = {keliling}")
    elif opsi == 3:
        print(f"hasil perhitungan luas = {luas}")
        print(f"hasil perhitungan keliling = {keliling}")
    else:
        print("Udaaah kaga ada")

# program utama
while True:
    header()
    opsi = int(input("Pilih hitung:\n1. luas\n2. keliling\n3. keduanya\n(ketik angka sesuai pilihan): "))

    panjang,lebar = input_user()
    luas = hitung_luas(panjang,lebar)
    keliling = hitung_keliling(panjang,lebar)

    menampilkan_hasil(opsi,luas,keliling)

    isContinue = input("Apakah lanjut (y/n)? ")
    if isContinue == "n":
        break

print("Program selesai terima kasih")