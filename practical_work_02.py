
#* Instituto Paulo Freire "Paulo Freire"

#TODO: Participantes

programacion= {"Ana", "Luis", "Carlos", "María", "Lucía", "Pedro"}
datos= {"Lucía","Pedro", "Elena", "María", "Sofía", "Franco"}
web= {"Carlos", "Elena", "Tomás", "María","Sofía", "Luis"}

#* Conjunto con todos los participantes sin repeticiones


total_participantes= programacion | datos |  web

print(f"Total de participantes por carrera: {total_participantes}")


#* Participantes que participaron en en los tres talleres al mismo tiempo


participan_en_todas= programacion & datos & web

print(f"Participantes en todos los talleres: {participan_en_todas}")



#* Participantes que solo estan en programacion


participan_solo_programacion= programacion - (datos | web )

print(f"Solo participan en Programacion: {participan_solo_programacion}")



#* Participantes en comun entre datos y web mostrar true o false


#todo: verificar si los conjuntos datos y web tienen algun parti cipante en comun.Devolver true o false


tienen_participantes_comun= not datos.isdisjoint(web)

print(f"Tienen datos y web participantes en  comun ?: {tienen_participantes_comun}")


participantes_comun= datos & web 

print(f"Participantes en comun entre datos y web: {participantes_comun}")


#* Guardar listado definitivo como registro que no pueda modificarse



#TODO: Listado de participantes programacion, datos, web

listado_participantes= programacion | datos | web
print(f"listado participantes programacion, datos y web: {listado_participantes}")


#TODO: Lista definitiva sin posibilidad de modificacion

listado_frozen= frozenset(listado_participantes)

#TODO: Nuevo alumno
alumno_nuevo= "Marcos"

#TODO: agregando un alumno nuevo

listado_nuevo= listado_participantes.add(alumno_nuevo)
print(f"Listado con nuevo participante: {listado_nuevo}")