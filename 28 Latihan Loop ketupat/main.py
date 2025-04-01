panjang = int(input("Masukkan jumlah ukuran: "))  # Ukuran setengah tinggi ketupat

# Bagian atas ketupat
for i in range(1, panjang + 1):
    print(("+" * (2 * i - 1)).center(panjang * 2 - 1))

# Bagian bawah ketupat
for i in range(panjang - 1, 0, -1):
    print(("+" * (2 * i - 1)).center(panjang * 2 - 1))
