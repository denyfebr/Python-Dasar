# Program list buku

list_buku = []
while True:
    print("\nMasukkan data buku")
    judul = input("Judul\t: ")
    penulis = input("Penulis\t: ")

    buku_baru = [judul,penulis]
    list_buku.append(buku_baru)

    print("\n\n","="*10,"Data Buku","="*10)

    for index,buku in enumerate(list_buku):
        print(f"Data buku ke-{index+1}")
        print(f"Judul\t: {buku[0]}")
        print(f"Penulis\t: {buku[1]}")
        print("-"*10)

    print("\n\n","="*20)
    is_lanjut = input("Input lagi (y/n) : ")

    if is_lanjut=="n":
        break

print("Input selesai terima kasih!!")