import statistics as stats

idades = []
maior = 0
menor = 0
espacocalculo = 0

confirmacao = input("deseja digitar a nota do primeiro aluno (s/n) ")

if confirmacao == "n":
 exit()

while confirmacao != "n":
   idade = int(input('idade: '))
   idades.append(idade)
   confirmacao = input("deseja digitar a nota do primeiro aluno? (s/n) ")

for i in idades:
    if i > 18:
       maior +=1
    if i <= 18:
         menor +=1
         espacocalculo=espacocalculo + i
print("\nmais novo: ", min(idades), "\nmais velho", max(idade), "\nmaiores de 18 anos :",maior, "\nate 18",menor,"\nmedia ariitimetica", espacocalculo  / len(idades), "\nmediana:", stats.median(idades))