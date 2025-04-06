'''*args'''

# memasukkan data/argument

def fungsi(nama,tinggi,berat):
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("Ucup",140,60)

def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi(["Otong",150,90])

# kenalan dengan *args

def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("Dudung",120,120)

# studi kasus

def tambah(*nilai):
    hasil = 0
    for angka in nilai:
        hasil += angka
    return hasil

hasil_tambah = tambah(1,2,3,4,5,6,7,8,9)
print(f"Hasil tambah = {hasil_tambah}")

hasil_tambah = tambah(10,5,15)
print(f"Hasil tambah = {hasil_tambah}")
