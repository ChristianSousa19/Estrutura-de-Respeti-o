num = int(input("numer: "))
espacosexof = 0
espacosexom = 0
espacoidadesexof = 0
espacoidadesexom = 0

for i in range(num):
  sexo = input("sexo (m/f: ")
  idade = int(input("idade: "))
  if sexo =="f":
    espacosexof += 1
    espacoidadesexof+= idade
  elif sexo == "m":
      espacosexom +=1
      espacoidadesexom +=idade

print("media homens:"),espacoidadesexom / espacosexom,"media mulheres", espacoidadesexof/espacosexof