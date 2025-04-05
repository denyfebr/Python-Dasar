'''Fungsi dengan return value'''

# template fungsi dengan kembalian
# def nama_fungsi(argument):
#       badan fungsi
#       return output

# fungsi kuadrat
def kuadrat(input_angka):
    '''Fungsi kuadrat'''
    hasil = input_angka**2
    return hasil

in_angka = int(input("Masukkan angka : "))

print(f"Hasil dikuadratkan = {kuadrat(in_angka)}")

z = 10 + kuadrat(in_angka)
print(z)

#  fungsi tambah
def tambah(angka_1,angka_2):
    '''Fungsi return dengan multi argument'''
    return angka_1+angka_2

a = tambah(10,8)
print(a)

# fungsi dengan return banyak
def operasi_matematika(angka_1,angka_2):
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2
    kali = angka_1 * angka_2
    bagi = angka_1 / angka_2

    return tambah,kurang,kali,bagi

k,l,m,n = operasi_matematika(9,5)

print(f"Hasil ditambah = {k}")
print(f"Hasil dikurang = {l}")
print(f"Hasil dikali = {m}")
print(f"Hasil dibagi = {n}")

