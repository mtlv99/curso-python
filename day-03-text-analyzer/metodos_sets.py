# Sets
# Solo admiten elementos ÚNICOS
# Python automaticamente descarta elementos repetidos si existiera alguno
# No están ordenados con indices, igual que los diccionarios
# al ser immutables, no se pueden incluir listas ni diccionarios, pero si tuples (porque también son immutables)

# se pueden declarar con set() o usando llaves { }

# con set debe pasar un solo argumento, puede ser con parentesis, corchetes o llaves
mi_set = set([1, 2, 3])

# ó declarando directamente
mi_set = {1, 2, 3}

print(type(mi_set))  # type : <class 'set'>
print(mi_set)  # {1, 2, 3}

print(len(mi_set))
print(2 in mi_set)  # para comprobar existencia de valores

s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.union(s2)  # Python quitará el 3 repetido a la hora de hacer la union, quedando solo con 5 elementos
print(s3)
s3.add(6)  # si se agregara un elemento repetido, simplemente lo ignora

# eliminar/descartar
s3.remove(1)  # elimina el elemento, pero si no existe tirará un error
s3.discard(1)  # elimina el elemento, pero si no existe simplemente ignora la instrucción
eliminado_random = s3.pop()  # elimina un elemento aleatorio al no haber indices
print(eliminado_random)

s3.clear()  # limpia el set por completo
