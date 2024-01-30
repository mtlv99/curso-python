# importaciones (los archivos .py no deben tener el mismo
# nombre que las librerias, o causara dependencias circulares (se estaría importando el mismo módulo
# que se está escribiendo (case sensitive). Si se utiliza Random.py, no causaría problema por ejemplo.

from random import *  # para importar toda la librería
# from random import randint  # para importar un solo método

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

print("Random:\n")

# Random
colores = ['azul', 'rojo', 'verde', 'amarillo']
numeros_rand = list(range(5, 50, 5))

aleatorio = randint(1,50)  # genera un int entre el rango seleccionado
aleatorio_uniform = uniform(1,5)  # genera un float entre el rango seleccionado
aleatorio_rand = random()  # genera un float entre 0 y 1, similar a como funcionan los otros lenguajes de programación.
aleatorio_choice = choice(colores)  # selecciona un elemento random de una lista

# random values
print(aleatorio)
print(aleatorio_uniform)
print(aleatorio_rand)
print(aleatorio_choice)

# shuffle method
shuffle(numeros_rand)  # randomiza una lista de valores
print(numeros_rand)

# Comprensión de listas

palabra = 'python'

# Esto se puede simplificar:
# lista = []
#
# for letra in palabra:
#     lista.append(letra)

# Es lo mismo de arriba. La variable tiene que tener el mismo nombre
lista = [letra for letra in palabra]
print(lista)

# nums
lista_num = [n for n in range(0, 21, 2)]
print(lista_num)

# también se puede manipular el resultado de n
lista_num2 = [n / 2 for n in range(0, 21, 2)]
print(lista_num2)

# también con condiciones
lista_if = [n for n in range(0, 21, 2) if n * 2 > 10]
print(lista_if)

# también con condicion alternativa
# (hay que cambiar un por el orden para meter el else)
lista_if2 = [n if n * 2 > 10 else 'no' for n in range(0, 21, 2)]
print(lista_if2)

# Ejemplo
pies = [10, 20, 30, 40, 50]
metros = [p/3.281 for p in pies]

print(metros)