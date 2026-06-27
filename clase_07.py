
# *Tipos de Datos compuestos
lista= ["hola",1, True, [1,2,3,4] ]

tupla= (1,3,(1,2), ["g", 0], "chau")

textos= "hola mundo cruel"

# *Diccionarios

alumno= ["valentina", 19, "TSCDIA", "Resistencia"] # *cuesta acceder a un valor cuando hay muchos datos
diccionario_alumno= {"nombre": "valentina","edad": 20} # *se accede mas rapido por su llave key

# TODO: print(diccionario_alumno["nombre"])# *accede a un elemento del diccionario
# TODO: print(tupla[1]) # *accede a un elemento de una lista
# TODO: print(diccionario_alumno.get("nombre", "no tiene nombre"))
# TODO: print(diccionario_alumno.get("casa", "no existe casa"))
# TODO: print(diccionario_alumno.get("nombres", "no existe nombres"))

# *agreagar datos

# *para listas

lista.append("hola")

# *para diccionarios

diccionario_alumno["edad"]= "luis"


# *acceder a keys (ubicacion del dato)
key_diccionario= diccionario_alumno.keys

# TODO: print(key_diccionario)

# *acceder a los valores 
value_diccionario= diccionario_alumno.values
# TODO: print(value_diccionario)


# *en listas los valores pueden repetirse 
lista_nueva=[1,1,1,2,2]

# *en diccionarios no puede repetirse las claves pero si el valor
diccionario_nuevo= {"arbol": "algarrobo"}
diccionario_nuevo["arbol": "paraiso"] # *reemplaza el valor de la antigua clave

diccionario_nuevo["arbol": "urunday"] # *agrega nuevo  valor sin problema

eliminado= diccionario_nuevo.pop("arbol") # *manera de eliminar
del diccionario_nuevo["arbol"] # *manera de eliminar

eliminar_ultimo= diccionario_nuevo.popitem # *elimina el ultimo

# *unir diccionarios

diccionario_alumno.update(diccionario_nuevo)

