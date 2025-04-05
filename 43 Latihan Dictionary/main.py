# Latihan Dictionary
import datetime
import os
import string
import random

os.system("cls")
mahasiswa_template = {
    "nama":"nama",
    "nim":"00000000",
    "sks_lulus":0,
    "lahir":datetime.date(1111,1,11)
}

data_mahasiswa = {}

while True:    
    print(f"{'SELAMAT DATANG':^20}")
    print(f"{'DATA MAHASISWA':^20}")
    print("-"*20)
    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    
    mahasiswa['nama'] = input("Nama : ")
    mahasiswa['nim'] = input("NIM : ")
    mahasiswa['sks_lulus'] = int(input("SKS : "))
    tanggal = int(input("Tanggal lahir (1-31): "))
    bulan = int(input("Bulan lahir (1-12): "))
    tahun = int(input("Tahun lahir (YYYY): "))
    mahasiswa['lahir'] = datetime.date(tahun,bulan,tanggal)

    key = ''.join(random.choice(string.ascii_uppercase) for i in range(6))
    data_mahasiswa.update({key:mahasiswa})
    print(f"\n{'KEY':<6} {'NIM':<8} {'Nama':<17} {'SKS':<3} {'Lahir':<10}")
    print("-"*50)
    for mahasiswa in data_mahasiswa:
        key = mahasiswa
        nama = data_mahasiswa[key]['nama']
        nim = data_mahasiswa[key]['nim']
        sks = data_mahasiswa[key]['sks_lulus']
        lahir = data_mahasiswa[key]['lahir'].strftime("%d/%m/%Y")

        print(f"{key:<6} {nim:<8} {nama:<17} {sks:<3} {lahir:<10}")

    pilih = input("Apakah akan mengisi data lagi (y/n): ")

    if pilih == "n":
        break

print("Selesai! Terima kasih")