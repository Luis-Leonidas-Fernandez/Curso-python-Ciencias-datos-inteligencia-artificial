
#* Bucles while

frutas = ["manzana", "banana", "naranja"]

for fruta in frutas:
  print(fruta)

for numero in range(10): # se repite 10 veces
  print("cepillar diente derecha")
  print("cepíllar diente izquierda")



#* WHILE (mientras)

contador= 0

while True:
  print(contador)
  contador += 1
  if contador > 1000:
    print("se ejecuto")
    break

while True:
  respuesta = input("Escribi salir para terminar: ")
  if respuesta == "salir":
    break


stock = {"arroz": 45, "aceite": 8, "harina": 3, "azucar": 10}
#*diccionarios.values()
#*diccionario.keys()
#*diccionario.items()

cantidad = 0

for valor in stock.values():
  cantidad += valor
  print(cantidad)


for clave, valor in stock.items():
  cantidad += valor
  print(f"De {clave} traje {valor}")