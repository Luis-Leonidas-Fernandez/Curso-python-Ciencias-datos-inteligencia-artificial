
# * NUMEROS COMPUESTOS Y LISTAS

lista_nueva= ["uno", 2, "tres"]
peliculas= ["Inception","Interstellar", "Matrix", "Kun fu Panda"]
numeros=[1,8,3,5]

pelicula_tupla= ("Jim Carrey", "Los Simposons", "Batman") 
# TODO: print(type(",".join(peliculas)))

peliculas.append("Crepusculo") # *agrega un dato al final
peliculas.insert(2, "El conjuro") # *inserta un dato en una posicion determinada
# TODO: print(peliculas)
quitado= peliculas.pop() # *extrae el dsto en la ultima posicion
quitado_index= peliculas.pop(0) # *obtiene el dato de la primer posicion

# TODO: print(quitado)
# TODO: print(quitado_index)

# TODO: print(peliculas.index("Matrix")) # *para hallar un indice
# TODO: print(len(peliculas)) # *length de una lista

numeros.sort()# *ordena una lista
# TODO: print(numeros)
numeros.sort(reverse= True) # *Ordena una lista al revez del final al inicio
# TODO: print(numeros)
corte= peliculas[2:] # *trae los datos desde el index 2 hasta el final de la misma
# TODO: print(corte)

# TODO: En las tuplas no podes hacer remove, append, insert solo agregar tuplas a tuplas

nueva_tupla= pelicula_tupla + ("Casados con hijos")
# TODO: print(nueva_tupla)