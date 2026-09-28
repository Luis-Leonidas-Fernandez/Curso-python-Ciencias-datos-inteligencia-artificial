
#* Desafio 1: Tuning

lista_prestaciones = ["precision", "velocidad", "escalabilidad", "robustez", "interpretabilidad"]

nueva_prestacion = "adaptabilidad"

lista_prestaciones.append(nueva_prestacion)

lista_ordenada = sorted(lista_prestaciones)


#* Desafio 2: No necesito saber tanto

datos_empleado = {}

datos_empleado["nombre"]= "Pedro"
datos_empleado["edad"]= 40
datos_empleado["aspiraciones"]= ["escalar muy alto", "obtener mucho poder"]
datos_empleado["especializacion"]= "machine learning"


print(f"nombre del empleado: {datos_empleado['nombre']}")
print(f"edad: {datos_empleado['edad']}")
print(f"aspiraciones: {datos_empleado['aspiraciones']}")
print(f"especializacion: {datos_empleado['especializacion']}")

datos_empleado["aspiraciones"]= ""

print(f"nombre del empleado: {datos_empleado['nombre']}")
print(f"edad: {datos_empleado['edad']}")
print(f"aspiraciones: {datos_empleado['aspiraciones']}")
print(f"especializacion: {datos_empleado['especializacion']}")


#*Desafio 3: No me quemes

temperatura_sensor= int(input("agregar temperatura actual: "))

if temperatura_sensor >= 80:
  print("¡Alerta! Temperatura critica")
elif temperatura_sensor >= 35  and temperatura_sensor <= 79:
    print("Temperatura dentro de los limites")
else:
    print("El equipo esta frio")


#*Desafio 4: Menos es mas

bella = {"lunes": 12, "martes": 16, "miercoles": 15, "jueves": 10, "viernes": 13}

edward = {"lunes": 24, "martes": 13, "miercoles": 8, "jueves": 4, "viernes": 21}

total_acciones = 0

for accion in bella.values():
   total_acciones += accion
print("acciones totales de bella:", total_acciones)

total_acciones = 0

for accion in edward.values():
   total_acciones += accion
print("acciones totales de edward:", total_acciones)


#* Desafio 5: ¿En que numero estoy pensando?

import random

numero_desconocido = random.randint(1, 10)
numero_adivinado = int(input("ingrese su numero: "))


while numero_desconocido:
   if numero_desconocido == numero_adivinado:
      print("felicidades has adivinado el numero")
      break
   if numero_desconocido != numero_adivinado:
      es_mayor = numero_adivinado < numero_desconocido
      es_menor = numero_adivinado > numero_desconocido

      if es_mayor == True:  
       numero_adivinado = int(input("haz fallado ingresa un numero mayor: "))
       if es_menor == True:
          numero_adivinado = int(input("haz fallado ingresa un numero menor: "))


#* Desafio 6: Tirar canas al aire

Drone1 = ["CoquiCorp", 45, True]
Drone2 = ['CoquiCorp', 70, False]
Drone3 = ['CoquiCorp', 25, True]
Drone4 = ['CoquiCorp', 90, False]
Drone5 = ['CoquiCorp', 15, True]
Drone6 = ['CoquiCorp', 55, True]
Drone7 = ['CoquiCorp', 80, False]

lista_drones = []

lista_drones.append(Drone1)
lista_drones.append(Drone2)
lista_drones.append(Drone3)
lista_drones.append(Drone4)
lista_drones.append(Drone5)
lista_drones.append(Drone6)
lista_drones.append(Drone7)


bateria_optima = 41
disponibilidad_tecnica = True

drones_listo_para_patrullar = []
drones_fuera_de_servicio = []

for drone in lista_drones:
  
   if drone[1] > bateria_optima and drone[2] == disponibilidad_tecnica:
      
      drones_listo_para_patrullar.append(drone)
   else:
     
      drones_fuera_de_servicio.append(drone)


print("Drones aptos para patrullaje:", drones_listo_para_patrullar)
print("Drones fuera de servicio, recargar y reparar:", drones_fuera_de_servicio)













