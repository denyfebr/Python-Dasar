# Standar library

import datetime

data_waktu = datetime.datetime.now()
print(f"datetime now : {data_waktu}")
print(f"tahun : {data_waktu.year}")
print(f"hari : {data_waktu.strftime('%A')}")
print(f"datetime now with format: {data_waktu.strftime('%A, %d/%m/%Y')}")

from collections import Counter

data = ["a","b","c","d","a","d","a"]
data_count = Counter(data)
print(f"data count = {data_count}")
print(f"jumlah 'a' = {data_count['a']}")
print(f"jumlah 'd' = {data_count['d']}")

# kalau manual tanpa std lib collection
# count = 0
# for i in data:
#     if i == "a":
#         count += 1

# print(f"Jumlah 'a' = {count}")

import io

file = io.open("D:/Latihan/Python/Kelas_terbuka/Python-Dasar/58 Standar Library/file_text.txt","r")
print(file.read())

