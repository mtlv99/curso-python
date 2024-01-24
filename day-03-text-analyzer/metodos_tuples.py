# TUPLES
# son immutables
# ocupan menos espacio en memoria
# utiles para estructuras que deben ser readonly

mi_tuple = (1, 2, 3, 4)  # también se puede declarar sin parentesis
print(type(mi_tuple))  # type : <class 'tuple'>
t = (1, 'hola', {"soyun": "diccionario"}, True, (3, 4))  # puede tener multiples tipos de datos, incluso otros tuples

# mi_tuple[0] = "Error, oops"  # son immutables por lo que esto dará un error

print(mi_tuple[0])  # se accede igual que una lista y diccionario

# se puede castear a lista
mi_tuple_lista = list(mi_tuple)
print(type(mi_tuple_lista))


# son utiles para asignar multiples variables, similar a la destructuración de javascript (acá se llama unpack)
# También funciona con listas y diccionarios, mientras haya la misma cantidad de elementos (ni más, ni menos)
tuple_example = (1, 2, 3)
x, y, z = tuple_example
print(x, y, z)

# Metodos de tuples
t_metodos = (1, 2, 3, 1)
print(len(t_metodos))
print(t_metodos.count(1))  # .count() permite saber la cantidad de repeticiones de un elemento
print(t_metodos.index(2))  # buscar el index de cierto valor
print(2 in t_metodos)
