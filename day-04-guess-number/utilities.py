# Range:
# range crea un objeto con valores empezando desde 0 hasta el valor definido
# for numero in range(5):
#     print(numero)

# se le pasan dos valores para definir un rango de inicio. Tercer valor es el step (cuantos saltos entre numeros)
for numero in range(20, 31, 2):
    print(numero)

# crear una lista del 1 al 100
lista = list(range(1, 101))
print(lista)

# Enumerate:
# crea un tuple para recorrer las listas
lista_en = ['a', 'b', 'c']

for item in enumerate(lista_en):
    print(item)


# util para crear listas de tuples.
mis_tuples = list(enumerate(lista_en))
print(mis_tuples)
print(mis_tuples[1][0])

# con Strings
lista_indices = list(enumerate("Python"))
print(lista_indices)


# Zip
# combina dos listas en un tuple, segun el orden que sigan
nombres = ['Ana', 'Hugo', 'Valeria']
edades = [65, 29, 42, 100] # si no hay match con el resto, por ejemplo acá la posicion 4 la ignora.
ciudad = ['Lima', 'San José', 'Buenos Aires']

# sin el list, solo muestra una posicion en memoria
combinados = list(zip(nombres, edades, ciudad))
print(combinados)

for nombre, edad, ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")

# Min - max
menor = min(58, 35, 45, 23, 34)
mayor = max(58, 35, 45, 23, 34)

print(menor, mayor)

lista = [58, 35, 45, 23, 34]
print(f"El menor es {min(lista)} y el mayor es {max(lista)}")

# el primer nombre alfabeticamente
nombres_min = ['juan', 'pablo', 'alicia', 'carlos']
print(min(nombres_min))

# el primer caracter de un nombre (busca primero por mayusculas y luego minusculas, por eso sale 'C')
# para evitar confusiones, es mejor convertirlo a lowercase
nombre_min = "Carlos"
print(min(nombre_min))
print(min(nombre_min.lower()))  # resultado diferente

# para los diccionarios busca igual por el key con valor alfabetico mas bajo
dic_min = {'C1': 45, 'C2': 11}
print(min(dic_min))

# para conseguir el valor mas bajo se usaria .values()
print(min(dic_min.values()))
