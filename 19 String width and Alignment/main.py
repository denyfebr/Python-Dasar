# Width and Multiline

# Data

data_nama = "Ucup Surucup"
data_umur = 17
data_tinggi = 177.1
data_nomor_sepatu = 44

# String standard
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, sepatu = {data_nomor_sepatu}"
judul = "DATA STRING".center(21,'=')
print("\n'"+judul+"'")
print(data_string)

# String multiline (dengan menggunakan enter, newline,\n)
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nsepatu = {data_nomor_sepatu}"
judul = "DATA STRING".center(21,'=')
print("\n'"+judul+"'")
print(data_string)

# String multiline (kutip triplets)
data_string = f"""nama = {data_nama}
umur = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_nomor_sepatu}
"""
print("\n'"+judul+"'")
print(data_string)

# Mengatur lebar
data_nama = "Ucup"
data_string = f"""
nama   = {data_nama:>5}
umur   = {data_umur:>5}
tinggi = {data_tinggi:>5}
sepatu = {data_nomor_sepatu:>5}
"""
print("\n'"+judul+"'")
print(data_string)