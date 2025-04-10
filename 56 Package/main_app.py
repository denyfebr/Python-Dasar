import time

t_start = time.time()

import sains.matematika
# import sains.fisika
from sains import fisika
from sains.fisika import gaya as force

hasil_tambah = sains.matematika.tambah(1,2,3,4,5)
print(f"hasil tambah dari package adalah = {hasil_tambah}")

hasil_gaya = fisika.gaya(90,10)
print(f"gaya adalah = {hasil_gaya}")

gaya = force(90,10)
print(f"gaya as force adalah = {gaya}")


t_end = time.time()

print(f"waktu eksekusi = {t_end - t_start}")