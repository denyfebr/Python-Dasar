'''Fungsi dengan default argument'''

# template fungsi dengan default argument
# def nama_fungsi(argument):
# def nama_fungsi(argument = nilai defaultnya):

# contoh 1
def say_hello(nama = "Ganteng"):
    '''Fungsi dengan default argument'''
    print(f"Hallo {nama}")

say_hello("Ucup")
say_hello()

# contoh 2
def sapa_dia(nama,pesan = "Air putih"):
    '''Fungsi dengan argument default dan non default'''
    print(f"Nama saya {nama}, {pesan}")

sapa_dia("Dudung","Tebs 2 botol dan es batu")
sapa_dia("Bagong")

# contoh 3
def hitung_pangkat(angka,pangkat):
    hasil = angka**pangkat
    return hasil

print(hitung_pangkat(2,4))

hasil_pangkat = hitung_pangkat(pangkat = 2, angka = 2)
print(hasil_pangkat)

# contoh 4
def fungsi_empat(input1=1,input2=2,input3=3,input4=4):
    hasil = input1+input2+input3+input4
    return hasil

print(fungsi_empat())
print(fungsi_empat(input3=10))

def fungsi_genk(input1="Kucluk",input2="Kentir",input3="Paok",input4="Bajigur"):
    hasil = input1+","+input2+","+input3+","+input4
    return hasil

print(fungsi_genk())
print(fungsi_genk(input3="Dalbo"))