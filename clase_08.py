
# *CONJUNTOS

conjunto= {1,2,3,4}
print(type(conjunto))


lista= [1,2,3,4]
print(lista)

conjunto_vacio= set()
print(conjunto_vacio, type(conjunto_vacio))

a={1,2,3,4} # * esto es un conjunto
a.add(5) # * agrega un dato a un conjunto

print(a)
a.remove(2) # * elimina un elemento
print(a)
a.clear() # *limpia un conjunto en su totalidad
print(a)


print(4 in a) # * si existe dentro del conjunto


# * union de conjuntos
a= {8,9,10}
b= {5,8,9}

print(a.union(b))
print(a,"", b)

# * Interseccion (donde los datos coinciden o se repiten)
print(a.intersection(b))
print(a&b) # * es equivalente a: a.intersection


# * iferencia simetrica: es donde no se cruzan los datos de dos circulos

print(a.symmetric_difference(b))


# * Otro metodo

c={1,2}
d={1,2,3,4}

print(c.isdisjoint(d)) # * pregunta si comparte elementos ambos conjuntos

print(d.issubset(c)) # * esta dentro de que conjunto?

print(c.issuperset(d)) # * c contiene a d ?
print(d.issuperset(c)) # * d contiene a c? si


# * CREAR CONJUNTOS INMUTABLES

conjunto_inmutable= frozenset({1,2,3})
print(conjunto_inmutable, type(conjunto_inmutable))



ana= {"rock", "pop",  "jazz","metal", "blues"}
lucas={"pop", "reggae", "jazz", "electro", "cumbia"}
sofia={"pop", "jazz"}

# *gustos de los dos

print(lucas | ana)

# * Gustos en comun

print(ana&lucas)
print(ana&(lucas |  sofia)) # *gustos que coinciden entre ana ly lucas ...pero que coninicdan con sofia

print((ana&lucas) |  sofia ) # *gustos que coinciden entre ana y lucas (elimina)

# * Generos que sean exclusivos de ana, que ninguno de los otros  dos escuchan
print(ana-(lucas | sofia ))

todos= frozenset(ana| lucas | sofia)
print(todos, type(todos))