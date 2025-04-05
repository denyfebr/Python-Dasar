# copy & pop dictionary

teman_teman = {
    "cup":"ucup surucup",
    "tong":"otong surotong",
    "dung":"dudung surudung",
    "sep":"asep si kasyep",
    "cuy":"ucuy surucuy"
}

print("==Mengcopy pass by reference==")
friends = teman_teman

print(f"teman_teman: {teman_teman}")
print(f"friends: {friends}")

teman_teman["cup"] = "ucup si kweren"
print(f"teman_teman: {teman_teman}")
print(f"friends: {friends}")

print("\n==Mengcopy copy()==")
friends = teman_teman.copy()
teman_teman["cup"] = "ucup si kintull"
print(f"teman_teman: {teman_teman}")
print(f"friends: {friends}")

print("\n==Pop Dictionary==")
dataAsep = friends.pop("sep")
print(f"data asep = {dataAsep}")
print(f"friends: {friends}")

print("\n==Pop Items Dictionary==")
dataTerakhir = friends.popitem()
print(f"data terakhir = {dataTerakhir}")
print(f"friends: {friends}")
