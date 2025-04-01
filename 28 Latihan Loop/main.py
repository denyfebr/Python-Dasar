# Latihan perulangan membuat segitiga

sisi = int(input("Masukkan jumlah sisi = "))
print("="*10)
# 1. Menggunakan for
count = 1
print("awal for")
for i in range(sisi):
    print ("*"*count)
    count += 1
print("akhir for")
print("="*10)
# 2. Menggunakan While
count = 1
print("awal while")
while True:
    print("*"*count)
    count += 1
    if count > sisi:
        break
print("akhir while")
print("="*10)
# 3. Hanya ganjil saja
count = 1
print("awal while ganjil")
while True:
    
    if count%2 != 0:
        print("*"*count)
        count += 1        
    else:
        count += 1
        continue

    if count > sisi:
        break
print("akhir while ganjil")
# 4. Segitiga sama kaki
count = 1
spasi = int(sisi/2)
print("awal while segitiga")
while True:    
    if count%2 != 0:
        print(" "*spasi+"+"*count)
        count += 1
        spasi -= 1       
    else:
        count += 1
        continue

    if count > sisi:
        break

while True:
    if count%2 != 0:  
        spasi += 1   
        print(" "*spasi+"+"*count)         
        count -= 1
    else:
        count -= 1
        continue

    if count == 0:
        break
print("akhir while segitiga")
