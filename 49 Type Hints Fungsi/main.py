'''Type hints untuk fungsi'''

# menjadi masalaha apabila inputan yg diterima typenya 
# tidak diterima oleh operasi dalam fungsi
'''
Study kasus
def fungsi(parameter):
    hasil = parameter**2
    print(hasil)

fungsi(1) ga ada masalah
fungsi("Ucup") error! kok string dikuadratkan
fungsi(True) error! kok boolean dikuadratkan
'''
import string
import os

# Penggunaan type hints
def fungsi_type_hints(argument:int) -> int:
    '''Fungsi dengan hint'''
    hasil = 10**argument
    return hasil

hasil = fungsi_type_hints(2)
print(hasil)

def display(argument:string):
    print(argument)

display("Si Ucup")
