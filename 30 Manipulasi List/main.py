## ----Manipulasi List----

#index  0(-3)     1(-2)   2(-1)
data = ["Ucup","Otong","Dudung"]

# mengambil data dari list ini
data_0 = data[0]
print(f"data pertama (index ke-0) = {data_0}")

data_terakhir = data[-1]
print(f"data terakhir adalah = {data_terakhir}")

data_ucup = data[-3]
print(f"data ucup = {data_ucup}")

# mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"panjang data = {panjang_data}")

## manipulasi data list

# menambahkan item pada list sesuai posisi
print(f"data sebelum ditambah = \n{data}")
#data.insert(posisi,item)
data.insert(1,"Asep")
print(f"data setelah ditambah 'Asep' di index-1 = \n{data}")

# menambahkan item di akhir list
data.append('Jajang')
print(f"data setelah ditambah 'Jajang' di akhir index = \n{data}")

# menggabungkan antar 2 buah list
data_baru = ["Kevin","Enrico","Felix","Denny"]
data.extend(data_baru)
print(f"Data setelah digabung data_baru = \n{data}")

# merubah data
data[2] = "Michael"
print(f"Data item ke-2 berubah menjadi 'Michael' = \n{data}")

# meremove data
data.remove("Kevin")
print(f"data remove 'Kevin' = {data}")
# data.remove("denny") akan error karena denny case sensitive

# meremove data paling belakang
data.pop()
print(f"data akhir = {data}")

data_terakhir_2 = data.pop()
print(f"data terakhir menggunakan pop adalah = {data_terakhir_2}")




