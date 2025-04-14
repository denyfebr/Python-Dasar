# Date and time (latihan)

import datetime as dt

hari_ini = dt.date.today()

print(hari_ini)
print(f"Hari ini adalah hari = {hari_ini:%A}")

tanggal = dt.date(1988,2,18)
print(tanggal)
print(f"Tanggal {tanggal} adalah hari = {tanggal:%A}")
print(f"Format tanggal (dd/mm/yyyy) = {tanggal.strftime("%d/%m/%Y")}")
