#latihan konversi satuan temperature

#program konversi celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input("Masukkan suhu dalam celcius : "))
print("Suhu adalah ",celcius)

# reamur
reamur = (4/5)*celcius
print("Suhu dalam reamur adalah ",reamur," Reamur")
# fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam fahrenheit adalah ",fahrenheit," Fahrenheit")
#kelvin
kelvin = celcius+273
print("Suhu dalam kelvin adalah ",kelvin," Kelvin")