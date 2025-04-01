sisi = int(input("Masukkan ukuran ketupat (harus ganjil) = "))
if sisi % 2 == 0:
    print("Ukuran ketupat harus ganjil!")
else:
    print("=" * 10)
    print("awal while ketupat")

    # Bagian atas ketupat
    count = 1
    spasi = sisi // 2
    while count <= sisi:
        print(" " * spasi + "+" * count)
        count += 2
        spasi -= 1

    # Bagian bawah ketupat
    count -= 4  # Mengurangi count agar mulai dari baris bawah yang benar
    spasi += 2  # Menyesuaikan spasi agar seimbang
    while count > 0:
        print(" " * spasi + "+" * count)
        count -= 2
        spasi += 1

    print("akhir while ketupat")
    print("=" * 10)
