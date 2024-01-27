#  Loop For
lista = ['a', 'b', 'c', 'd']

for letra in lista:
    # para obtener index del valor iterado
    index_letra = lista.index(letra) + 1
    print(f"Letra {index_letra}: {letra}")

palabra = 'python'

for letra in palabra:
    print(letra)

#  la 2da variable accede al 2do nivel de iteracion
for i, j in [[1, 2], [3, 4], [5, 6]]:
    print(i)
    print(j)

dic = {'clave1': 'a', 'clave2': 'b', 'clave3': 'c'}

# imprime solo key
for item in dic:
    print(item)


# imprime key/value
for item in dic.items():
    print(item)

# imprime key/value en variables separadas (por el unpacking, es como destructuracion)
for a, b in dic.items():
    print(a, b)

# break
nombre_loop = input("Tu nombre es: ")
for letra in nombre_loop:
    if letra == 'r':
        break  # rompe el ciclo del loop y se sale
    print(letra)

# continue
for letra in nombre_loop:
    if letra == 'r':
        continue  # se salta la iteracion actual y continua con las otras
    print(letra)


# Loop While

monedas = 5

# control definido
while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas -= 1
else:
    print("No tengo más dinero")

# input de usuario
respuesta = 's'
while respuesta == 's':
    respuesta = input("Quieres seguir? (s/n): ")
else:
    print("Cerrando...")

# pass
while respuesta == 's':
    # es un placeholder que se asigna para cuando el loop está vacio. Basicamente previene el error de bloque vacio
    pass
