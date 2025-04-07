## Global and Local Scope

nama_global = 'otong' # <- variable global

# akses variable global dalam fungsi
def fungsi():
    print(f"fungsi menampilkan {nama_global}")

fungsi()

# akses variable global dalam loop
for i in range(0,5):
    print(f"loop {i} - {nama_global}")

# akses variable global dalam percabangan
if True:
    print(f"if menampilkan {nama_global}")

## Variable Local Scope

def fungsi2():
    nama_local = "Ucup" # <- variable local scope

fungsi2()
# print(nama_local) # nama_local tidak bisa dikenal

## Contoh 1: penggunaan akses variable
def say_otong():
    print(f"Hello {nama}")

nama = "Otong"
say_otong()

## Contoh 2: merubah variable global
angka = 0
namanya = "Ucup"

def ubah(nilai_baru, nama_baru):
    global angka # angka global akan dipanggil
    global namanya
    angka = nilai_baru
    namanya = nama_baru

print(f"Sebelum {angka,namanya}")
ubah(10,"Otong")
print(f"Sesudah {angka,namanya}")

## Contoh 3:
angka = 0

for i in range(0,5):
    angka += i
    angka_dummy = 0

print(angka)
print(angka_dummy)

if True:
    angka = 10
    angka_dummy = 10

print(angka)
print(angka_dummy)