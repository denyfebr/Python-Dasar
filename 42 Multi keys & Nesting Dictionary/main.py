# Multi keys & Nesting Dictionary

import datetime

mahasiswa1 = {
    "nama":"Ucup Surucup",
    "nim":"19022001",
    "sks_lulus":130,
    "beasiswa":False,
    "lahir":datetime.date(2001,3,11)
}

mahasiswa2 = {
    "nama":"Otong Surotong",
    "nim":"19022002",
    "sks_lulus":140,
    "beasiswa":True,
    "lahir":datetime.date(2002,2,18)
}

mahasiswa3 = {
    "nama":"Asep Si Kasyep",
    "nim":"19022003",
    "sks_lulus":100,
    "beasiswa":False,
    "lahir":datetime.date(1999,8,17)
}

data_mahasiswa = {
    'MAH001':mahasiswa1,
    'MAH002':mahasiswa2,
    'MAH003':mahasiswa3
}

print(f"{'KEY':<6} {'NIM':<8} {'Nama':<17} {'SKS':<3} {'Beasiswa':<9} {'Lahir':<10}")
print("-"*50)

for mahasiswa in data_mahasiswa:
    key = mahasiswa
    nama = data_mahasiswa[key]['nama']
    nim = data_mahasiswa[key]['nim']
    sks = data_mahasiswa[key]['sks_lulus']
    beasiswa = data_mahasiswa[key]['beasiswa']
    lahir = data_mahasiswa[key]['lahir'].strftime("%d/%m/%Y")

    print(f"{key:<6} {nim:<8} {nama:<17} {sks:<3} {beasiswa:^9} {lahir:<10}")