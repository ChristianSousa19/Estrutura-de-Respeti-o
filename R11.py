num = int(input("numero: "))

nota = float(input("nota: "))
medianota = float(0)
medianota = medianota + nota

for i in range(1,num):
  nota = float(input("nota: "))
  medianota = medianota + nota

var = 4
print("media ", float(medianota/ num))