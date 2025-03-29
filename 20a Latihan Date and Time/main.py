import datetime as dt

print("Masukkan tanggal, bulan, dan tahun lahir")
tanggal = int(input("Tanggal \t: "))
bulan = int(input("Bulan \t\t: "))
tahun = int(input("Tahun \t\t: "))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"Tanggal lahir Anda {tanggal_lahir:%A},{tanggal_lahir}")

tanggal_skr = dt.date.today()
print(f"Tanggal sekarang {tanggal_skr:%A},{tanggal_skr}")

umur_hari = tanggal_skr-tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan = (umur_hari.days % 365) // 30
print(f"Umur Anda {umur_tahun} tahun, {umur_bulan} bulan")



