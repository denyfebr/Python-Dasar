# Latihan kalkulator sederhana

print(10*"=")
print("Kalkulator Sederhana")
print(10*"=")

angka_1 = float(input("Masukkan angka 1 = "))
operator = input("Pilih operator (+,-,x,/) : ")
angka_2 = float(input("Masukkan angka 2 = "))

if operator == '+':
    print(f"{angka_1} {operator} {angka_2} = {angka_1+angka_2}")
elif operator == '-':
    print(f"{angka_1} {operator} {angka_2} = {angka_1-angka_2}")
elif operator == 'x' or operator == '*':
    print(f"{angka_1} {operator} {angka_2} = {angka_1*angka_2}")
elif operator == '/' or operator == ':':
    print(f"{angka_1} {operator} {angka_2} = {angka_1/angka_2}")
else:
    print("Simbol tidak ada")

