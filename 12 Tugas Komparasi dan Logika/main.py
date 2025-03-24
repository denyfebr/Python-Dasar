# episode latihan logika dan komparasi

# membuat gabungan area rentang dari angka

# ----0++++5----8++++11----

inputUser = float(input("Masukkan angka yang bernilai:\n1.lebih dari 0\ndan\n2.kurang dari 5\ndan\n3.lebih dari 8\ndan\n4.kurang dari 11\n:"))
isLebihNol = inputUser>0
isKurangLima = inputUser<5
isLebihDelapan = inputUser>8
isKurangSebelas = inputUser<11
isCorrect = (isLebihNol and isKurangLima) or (isLebihDelapan and isKurangSebelas)
print(isCorrect)