# episode latihan logika dan komparasi

# membuat gabungan area rentang dari angka

# ++++0----5++++8----11++++

inputUser = float(input("Masukkan angka yang bernilai\nkurang dari 0\natau\nlebih besar dari 5 dan kurang dari 8\n:"))

isKurangNol = inputUser<0
isLebihLima = inputUser>5
isKurangDelapan = inputUser<8
isLebihSebelas = inputUser>11
isCorrect = isKurangNol or (isLebihLima and isKurangDelapan) or isLebihSebelas
print(isCorrect)