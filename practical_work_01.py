import random

# * 1) ¿Cuánto te sobró?

dinero_insertado = int(input("Insertar una cantidad de dinero que sea mayor a 3: "))

resto = dinero_insertado % 3

print("El resto es:", resto)



# * 2) Y el ganador es...

ganador_encontrado = random.randint(0, 300)

print("El número ganador es:", ganador_encontrado)


# * 3) Control de gastos

salario_mensual = float(input("Inserte su salario mensual: "))

salario_quincena = salario_mensual / 2
salario_semanal = salario_mensual / 4
salario_diario = salario_mensual / 20
salario_hora = salario_diario / 8

print("Salario por quincena:", round(salario_quincena, 2))
print("Salario semanal:", round(salario_semanal, 2))
print("Salario diario:", round(salario_diario, 2))
print("Salario por hora:", round(salario_hora, 2))


# * 4) Cuento los segundos

dias_insertados = int(input("Inserte cantidad de días: "))

segundos_obtenidos = dias_insertados* 24 * 60 * 60

print("La cantidad de segundos es:", segundos_obtenidos)



# * 5) Área de un círculo

radio_insertado = float(input("Inserte el radio del círculo: "))

area_circulo = 3.1416 * (radio_insertado ** 2)

print("El área del círculo es:", round(area_circulo, 2))



# * 6) A dónde me lleve la billetera


precio_litro_nafta = float(input("Ingrese el precio del litro de nafta súper: "))
distancia_kilometros = float(input("Inserte la distancia en kilómetros: "))

litros_necesarios = distancia_kilometros * 0.62
dinero_necesario = litros_necesarios * precio_litro_nafta

print("Litros necesarios para viajar:", round(litros_necesarios, 2))
print("Dinero necesario para gastar:", round(dinero_necesario, 2))




# * 7) Ni rápido ni furioso

tamano_archivo_mb = float(input("Inserte el tamaño del archivo en MB: "))
velocidad_descarga_kb = float(input("Ingrese la velocidad de descarga en KB/s: "))

tamano_kb = tamano_archivo_mb * 1024
segundos = tamano_kb / velocidad_descarga_kb
minutos = segundos / 60

print("Tiempo estimado de descarga en minutos:", round(minutos, 2))



# * 8) Mis mejores años marcianos


edad_terrestre = float(input("Inserte edad en años terrestres: "))

edad_marciana = edad_terrestre / 1.88

print("Su edad en años marcianos es:", round(edad_marciana, 2))


# * 9) Vivir de rentas


capital = float(input("Inserte el capital invertido: "))
tasa_anual = float(input("Inserte tasa anual de interés (%): "))
meses = int(input("Inserte la cantidad de meses de depósito: "))

interes_mensual = tasa_anual / 12
interes_total = capital * (interes_mensual / 100) * meses

print("El interés total que ganaste es:", round(interes_total, 2))


# * 10) A sus marcas

posicion_metros_iniciar = float(input("Inserta tu posición inicial en metros: "))
velocidad_iniciar = float(input("Inserta tu velocidad inicial en m/s: "))
tiempo = float(input("Inserta el tiempo transcurrido en segundos: "))
aceleracion = float(input("Inserta la aceleración en m/s²: "))

posicion_final = posicion_metros_iniciar + velocidad_iniciar * tiempo + 0.5 * aceleracion * (tiempo ** 2)

print("La posición final de tu  objeto es:", round(posicion_final, 2), "metros")

