import sains
from sains.matematika import scientific

hasil_tambah = sains.matematika.tambah(1,2,3,4,45)
print(f"hasil tambah = {hasil_tambah}")

hasil_fisika = sains.fisika.gaya(10,9.8)
print(f"hasil fisika = {hasil_fisika}")

hasil_kali = sains.matematika.kali(4,6,5,7)
print(f"hasil kali = {hasil_kali}")

hasil_pangkat_tiga = scientific.pangkat(3)
print(f"hasil pangkat tiga = {hasil_pangkat_tiga(4)}")

# from sains import *

# hasil_tambah = matematika.basic.tambah(1,2,3,4,45)
# print(f"hasil tambah = {hasil_tambah}")

# hasil_fisika = fisika.gaya(10,9.8)
# print(f"hasil fisika = {hasil_fisika}")

# hasil_kali = matematika.basic.kali(4,6,5,7)
# print(f"hasil kali = {hasil_kali}")