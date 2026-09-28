#* Lista de diccionarios

productos= [ {"nombre": "alfajor", "cantidad": 12, "precio": 3500},
              {"nombre": "agua", "cantidad": 3, "precio": 350},
               {"nombre": "naranja", "cantidad": 18, "precio": 3240},
                {"nombre": "silla", "cantidad": 8, "precio": 30},
            ]

# Contadores y acumuladores
valor_total= 0

for producto in productos:
  nombre= producto["nombre"]
  cantidad= producto["cantidad"]
  precio= producto["precio"]
  valor_total = valor_total + ( cantidad * precio)

  if cantidad == 0:
     print(f"{nombre}: agotado")
  elif cantidad < 5:
     print(f"{nombre}: necesita reposicion")
  else:
     print(f"{nombre} disponible {cantidad} unidades")


# Anidamiento While

registro = {}

while True:
   alumno = input("Nombre alumon ingreso o escribir salir para terminar")
   if alumno.lower() == "salir":
      break
 
   registro[alumno] = []

   while True:
      materia = input(f"Materia a la que asistió {alumno} (fin para terminar): ")
      if materia.lower()!= "fin":
         registro[alumno].append(materia)
      else:
         if registro[alumno]== []:
            registro[alumno].append("Ausente")
         break

for alumno in registro:
   cantidad =len(registro[alumno])
   if registro[alumno]== ["Ausente"]:
      print(f"{alumno}: Ausente")
   else:
      print(f"{alumno}: asistio a {cantidad} materias")


#Match case

alumnos = [
    {"nombre": "Luis", "nota": 8},
    {"nombre": "David", "nota": 6},
    {"nombre": "Mariel", "nota": 9}
]


for alumno in alumnos:

    match alumno["nota"]:

        case 7 | 8 | 9 | 10:
            print(f"{alumno['nombre']}: Aprobado")

        case 4 | 5 | 6:
            print(f"{alumno['nombre']}: Recuperatorio")

        case 1 | 2 | 3:
            print(f"{alumno['nombre']}: Desaprobado")

        case _:
            print(f"{alumno['nombre']}: Nota inválida")