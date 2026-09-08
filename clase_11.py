
#* Bucle FOR - conocemos la catidad de veces que ejecutaremos el codigo


frutas=["manzana", "banana", "naranja"]
edades= [15, 12,18, 7, 20]
for fruta in frutas:
  print("fruta encontrada:", fruta)

for index, fruta in enumerate(frutas):
  print("fruta encontrada:", fruta, "index:", index)

for numero in range(10):
  print(numero)

for edad in edades:
  if edad >= 18:
    print(edad, "años es mayor")
  else:
    print(edad, "Es menor")

#* Acumulador simple
precios= [1000, 5000,10000, 40000]
total= 0
print(total)
for precio in precios:
  total+= precio
print("fin", total)

#* acumular pares
edades=[15, 12,18, 7, 20, 42, 88]
cantidad= 0
for edad in edades:
  if edad % 2 ==0:
    cantidad += 1
print(f"Hay {cantidad} edades pares")    

#* acumular con condicion
edades=[15, 12,18, 7, 20, 42, 88]

edad=0

for i in edades:
  if i > edad:
    edad= i
    print(f"edad ahora vale {edad}")

#* acumular buscando un item y reasignado True o False
nombres=["ana", "luis", "geremias", "jose"]
buscar= "luis"
encontrado= False

for nombre in nombres:
  if nombre == buscar:
    encontrado = True  

if encontrado == True:
  print(f" {buscar} esta en la lista")
