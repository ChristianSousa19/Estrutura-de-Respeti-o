um = int(input("numero: "))
espaconome = "o"
espacoidade = 0

for i in range(num):
  nome = input("nome: ")
  idade = int(input("idade: "))
  if espacoidade < idade:
     espacoidade = idade
     espaconome = nome

print(espaconome, " e a pessoa mais velha")
