# looping dictionary

teman_teman = {
    "cup":"ucup surucup",
    "tong":"otong surotong",
    "dung":"dudung surudung",
    "sep":"asep si kasyep",
    "cuy":"ucuy surucuy"
}

# looping first try menggunakan list
for teman in teman_teman:
    print(teman) #yg keluar key nya

# operator utk mengambil item/iterables
print("\n==Iterrables keys==")
keys = teman_teman.keys()
print(keys)

print("\n==Mengambil keys==")
for key in teman_teman.keys():
    print(key)

print("\n==Mengambil value==")
for key in teman_teman.keys():
    print(teman_teman.get(key))

print("\n==Iterrables value==")
values = teman_teman.values()
print(values)

print("\n==Mengambil value==")
for val in values:
    print(val)

print("\n==Iterrables items==")
items = teman_teman.items()
print(items)

print("\n==Mengambil items==")
for item in items:
    print(item)

for key,value in teman_teman.items():
    print(f"key = {key}, value = {value}")