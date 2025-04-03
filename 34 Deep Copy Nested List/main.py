# Deep Copy Nested list

data_0 = [1,2]
data_1 = [3,4]

data_2D = [data_0,data_1,10]
data_2D_copy = data_2D.copy()

print(f"Data 2D = {data_2D}")
print(f"Data 2D copy = {data_2D_copy}")

# mengambil data

data = data_2D[0][0]
print(f"data = {data}")

data = data_2D[1][0]
print(f"data = {data}")

# address semuanya

print(f"address asli = {hex(id(data_2D))}")
print(f"address copy = {hex(id(data_2D_copy))}")

print(f"address dari member ke-1")
print(f"address asli = {hex(id(data_2D[0]))}")
print(f"address copy = {hex(id(data_2D_copy[0]))}")

data_2D[1][0] = 5
data_2D[2] = 9
print(f"Data 2D = {data_2D}")
print(f"Data 2D copy = {data_2D_copy}")

# kita gunakan deepcopy

from copy import deepcopy

data_2D = [data_0,data_1,10]
data_2D_deepcopy = deepcopy(data_2D)

print(f"address asli = {hex(id(data_2D))}")
print(f"address deepcopy = {hex(id(data_2D_deepcopy))}")

print(f"address dari member ke-1 deepcopy")
print(f"address asli = {hex(id(data_2D[0]))}")
print(f"address deepcopy = {hex(id(data_2D_deepcopy[0]))}")

data_2D[1][0] = 30
print(f"Data 2D = {data_2D}")
print(f"Data 2D copy = {data_2D_copy}")
print(f"Data 2D deepcopy = {data_2D_deepcopy}")