'''**kwargs'''

def fungsi(nama,tinggi,berat):
    '''Fungsi biasa'''
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("Ucup",183,79)

def fungsi(**kwargs):
    '''Fungsi kwargs'''
    print(kwargs)
    print(kwargs['nama'])
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

# fungsi("Ucup",183,79)
fungsi(nama="Ucup",tinggi=183,berat=79)

# studi kasus

def math(*args,**kwargs):
    
    hasil = 0
    if kwargs["option"] == "tambah":        
        for angka in args:
            hasil += angka
    elif kwargs["option"] == "kali":
        hasil = 1
        for angka in args:
            hasil *= angka
    else:
        print("tidak ada operasi")
    
    return hasil

hasil_math = math(1,2,3,4,option="tambah")
print(f"hasil jumlah = {hasil_math}")

hasil_math = math(1,2,3,4,option="kali")
print(f"hasil kali = {hasil_math}")