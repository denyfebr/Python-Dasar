# operator dalam bentuk method

## merubah case dari string

# merubah semua ke upper case
salam = "bro!"
print("normal = "+salam)
salam = salam.upper()
print("upper = "+salam)

# merubah semua ke lower case
alay = "aKu KeCe AbieezZzZZZ"
print("normal = "+alay)
alay = alay.lower()
print("lower = "+alay)

# pengecekan dengan isX method
salam = "sist"
apakah_lower = salam.islower()
print(salam + " is lower = "+str(apakah_lower))
apakah_upper = salam.isupper()
print(salam + " is upper = "+str(apakah_upper))

# isalpha() <-- untuk mengecek apakah semuanya huruf
# isalnum() <-- untuk mengecek apakah string ada huruf dan angka
# isdecimal() <-- ngecek apa angka aja
# isspace() <-- spasi, tab, newline \n, 
# istitle() <-- semua kata dimulai dengan huruf besar

#judul = "It Is Okay Not To Be Orkay"
judul = "It's Okay Not To Be Orkay"
cek_judul = judul.istitle()
print(judul + " is title = "+str(cek_judul))

## ngecek komponen startswith() endswith()
cek_start = "Sangjangnim Oppa".startswith("sangjangnim")
print("start = "+str(cek_start))

cek_end = "Sangjangnim Oppak".endswith("Oppak")
print("end = "+str(cek_end))

## penggabungan komponen join() split()
pisah = ['aku','sayang','kamu']
gabung = ','.join(pisah)
print(pisah)
print(gabung)

gabung = ' '.join(pisah)
print(gabung)

gabung = ' ehm '.join(pisah)
print(gabung)

gabung = "akuehmsayangehmkamu"
print(gabung)
print(gabung.split('ehm'))

## alokasi karakter rjust, ljust, center()
# print(5*"=" + "data" + "="*5)
kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10,"*")
print("'"+kiri+"'")

tengah = "tengah".center(20,':')
print("'"+tengah+"'")

# kebalikannya -> strip()
tengah = tengah.strip(":") #menghilangkan tanda :
print("'"+tengah+"'")

kanan = kanan.strip()
print("'"+kanan+"'")
