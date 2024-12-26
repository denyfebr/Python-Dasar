# a = 10, a adalah variable dengan nilai 10

#tipe data:Integer
data_integer = 10
print("data : ", data_integer, ", bertipe : ", type(data_integer))

#tipe data: Float (angka dengan koma)
data_float = 1.5
print("data : ", data_float, ", bertipe : ", type(data_float))

#tipe data: String (kumpulan karakter)
data_string = "ucup"
print("data : ", data_string, ", bertipe : ", type(data_string))

#tipe data: Boolean (biner true/false)
data_bool = False
print("data : ", data_bool, ", bertipe : ", type(data_bool))

##tipe data khusus

#bilangan kompleks
data_complex = complex(5,6)
print("data : ", data_complex, ", bertipe : ", type(data_complex))

#tipe data dari bahasa C
from ctypes import c_double, c_char, c_long

data_c_double = c_double(10.5)
print("data : ", data_c_double, ", bertipe : ", type(data_c_double))