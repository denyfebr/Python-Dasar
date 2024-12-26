
import time
start_time = time.time()

print("Hello")
print("World")
print("Hello world")

print("Halo duniaaa")
#ini adalah comment

"""
ini adalah 
comment multiline
dan tidak akan diesksekusi
"""
a=10 #ini adalah commen juga
print(a)

for i in range(1,1000):
    a=10
    
print(time.time()-start_time, " detik")
#kita bisa mengcompile pyhon ke
#yang namanya bytecode
#cara mengcompile, buka terminal
#ketik python -m  py_compile Main.py