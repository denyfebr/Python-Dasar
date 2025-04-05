'''Fungsi dengan argument (input)'''

'''
def nama_fungsi(argument):
    badan fungsi
'''

def hello_world(nama):
    print(f"Selamat datang di dunia wahai {nama} !!")

# hello_world("ucup")
in_nama = input("Masukkan nama Anda : ")
hello_world(in_nama)

# program tambah
def tambah(angka_1,angka_2):
    '''Fungsi tambah'''
    hasil = angka_1 + angka_2
    print(f"{angka_1} + {angka_2} = {angka_1+angka_2}")

in_angka_1 = int(input("Masukkan angka ke-1 : "))
in_angka_2 = int(input("Masukkan angka ke-2 : "))
tambah(in_angka_1,in_angka_2)

# Fungsi dengan argumen list

def say_hi(list_peserta):
    '''Iniadalah fungsi say hi'''
    # list_peserta[1] = "Ahsyep" pentingnya pake copy biar tidak merubah data di luar fungsi
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f"Yang terhormat {peserta}")


anggota_boyband = ["Ucup","Otong","Dudung"]
say_hi(anggota_boyband)
#print(anggota_boyband[1])