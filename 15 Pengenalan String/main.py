data = "ini adalah string"
print(data)
print(type(data))

# 1. cara membuat string

'''
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double quote "..."
'''

data = 'Menggunakan single quote'
print(data)

data = "Menggunakan double quote"
print(data)

print('"Halo, apa kabar?"')
print("'Halo, apa kabar?'")
print("ini adalah hari jum'at")

# 2. Menggunakan tanda \

# membuat tanda ' menjadi string
print('mari shalat jum\'at')
print('g\'day, isn\'t it?')

# backslash
print("C:\\user\\Ucup")

# tab
print("ucup\t\t\totong, jauhan")

# backspace
print("ucup \botong, jadi deketan")

# newline
print("baris pertama.\nbaris kedua.") #LF -> Line Feed -> unix, macos, linux
print("baris pertama.\rbaris kedua.") # CR -> Carriage Return -> commodore, acorn, lisp
print("baris pertama.\r\nbaris kedua.") # CRLG -> Line Feed Carriage Return -> windows

# 3.String literal atau raw

# hati-hati
print('C:\\new folder')

# menggunakan raw string
print(r'C:\new \t\r\bfolder')

# multiline literal string
print("""
Nama : Ucup
Kelas : 3 SD
""")

# multiline literal string dan RAW
print(r"""
      Nama : Ucup
      Kelas : 3 SD\new normal
      Website : www.ucup.com/newID
""")

