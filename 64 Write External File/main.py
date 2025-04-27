# 1. Mode write
# dia akan membuat file baru dan mereplace/overwrite file lama sehingga isinya yang terbaru

with open("./64 Write External File/data_1.txt",'w',encoding="utf-8") as file:
    file.write("ucup surucup")

with open("./64 Write External File/data_1.txt",'w',encoding="utf-8") as file:
    file.write("kontong sur kontong")

# 2. Mode append

with open("./64 Write External File/data_2.txt",'w',encoding="utf-8") as file:
    file.write("ucup surucup\n")

with open("./64 Write External File/data_2.txt",'a',encoding="utf-8") as file:
    file.write("kontong sur kontong\n")

with open("./64 Write External File/data_2.txt",'a',encoding="utf-8") as file:
    file.write("kintul sar kintul\n")

# 3. mode r+

with open("./64 Write External File/data_3.txt",'w',encoding="utf-8") as file:
    file.write("data ke-3\n")

with open("./64 Write External File/data_3.txt",'r+',encoding="utf-8") as file:   
    file.write("baris-1\n")    
    file.write("baris-2\n")
    file.write("baris-3\n")

with open("./64 Write External File/data_3.txt",'r+',encoding="utf-8") as file:   
    data = file.read()
    print(data)

with open("./64 Write External File/data_3.txt",'r+',encoding="utf-8") as file:   
    file.write("otong surotong") # akan menimpa sesuai dengan panjang data

