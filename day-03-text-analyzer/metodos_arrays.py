# LISTAS
# a.k.a arrays
print("Probando Listas:")

mi_lista = ['a', 'b', 'c']
mi_lista2 = ['d', 'e', 'f']

# recordar que el ultimo valor no es inclusivo, por lo que si se pone [0:1] solo incluirá ['a']
resultado = mi_lista[0:2]
mi_lista3 = mi_lista + mi_lista2  # combinar 2 arrays

print(resultado)
print(type(resultado))  # type : <class 'list'>

mi_lista3.append('g')
print(mi_lista3)


# pop() devuelve el elemento eliminado por lo que se puede guardar en una variable
eliminado = mi_lista3.pop(0)  # sin argumento elimina el ultimo elemento, pero se le puede pasar un index

print("Sort() lista:")
lista = ['g', 'o', 'b', 'm', 'c']

# sort()
print(lista)
nueva_lista = lista.sort()  # sort() es un metodo MUTABLE, por lo que cambiará el array original
print(lista)  # se está imprimiendo 'lista' por lo que el array original cambió
print(type(nueva_lista))  # y sort() tampoco devuelve ningun dato, por lo que queda en estado NoneType (null)

# reverse()
lista2 = ['a', 'b', 'c', 'd']
print(lista2)
lista2.reverse()  # reverse() es un metodo MUTABLE, por lo que cambiará el array original
print(lista2)
print('a' in lista2)
