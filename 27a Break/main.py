# Break

data_int  = int(input("Hitung sampai = "))

angka = 0

if(data_int > 0) :
    while True:
        angka += 1
        print(f"angka sekarang -> {angka}")

        if angka == data_int :
            print("nice!")
            break

        print("wassup!")

print("finish!!")