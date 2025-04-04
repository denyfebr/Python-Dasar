# operator dictionary

data_dict = {
    "cup":"ucup surucup",
    "tong":"otong surotong",
    "dung":"dudung surudung" 
}

print(data_dict)

# panjang dictionary
lendict = len(data_dict)
print(f"panjang dictionary: {lendict}")

# mengecek key exist atau tidak
key = "cup"
# key = "kis" -> False
checkkey = key in data_dict
print(f"apakah {key} ada di data_dict: {checkkey}")

# mengakses value (read) dengan get
print(data_dict["cup"])
print(data_dict.get("cup"))
# print(data_dict.get("cup"),"data tidak ditemukan")
print(data_dict.get("kis"),"data tidak ditemukan") # cek key dg message
# print(data_dict["kis"]) -> jika menggunakan list akan error

# mengupdate data
data_dict["cup"] = "ucup si ganteng"
print(data_dict)

# menambah data
data_dict["sep"] = "asep si kasep"
print(data_dict)

data_dict.update({"cup":"ucup cupubeud"})
print(data_dict)
data_dict.update({"den":"den suraden"}) # kalau ga ada diadd otomatis
print(data_dict)

# mendelete data pada dictionary
del data_dict["den"]
print(data_dict)
del data_dict["tong"]
print(data_dict)