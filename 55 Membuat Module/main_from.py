
# modul matematika dengan import

# from matematika import tambah,kali,pangkat
# from matematika import * <- pake bintang jadi ga tau yg mana modul yg dipake
from matematika import tambah as add # pake (as) alias
from matematika import kali
from matematika import pangkat

import matematika as math # <--- bisa dilakukan

hasil_tambah = add(1,2,3,4,5)
print(f"hasil tambah = {hasil_tambah}")

hasil_kali = math.kali(1,2,3,4)
print(f"hasil kali = {hasil_kali}")

pangkat_3 = pangkat(3)
print(f"hasil pangkat 3 = {pangkat_3(4)}")
