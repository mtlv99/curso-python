# index

mi_texto = "Esto es una prueba"
resultado = mi_texto.index("s", 5, 10)  # rindex() para buscar por index al reves
# index() y find() son casi iguales con la diferencia de que cuando no se encuentra el resultado,
# index() devuelve un error y find() devuelve un -1

print(resultado)


# slicing
texto = "ABCDEFGHIJKLM"
# [primera_posicion:ultima_posicion:salto_en_caracteres]
fragmento = texto[1:5]  # para hacer un substring del 2 al 5 (no incluyendo el 5)
fragmento2 = texto[1:10:2]  # para hacer substrings pero contando los caracteres de 2 en 2
# [::-1] para invertir el string

print(fragmento)
print(fragmento2)

# metodos
print(texto.upper())  # uppercase
print(texto.lower())  # lowercase
print(mi_texto.split(" "))  # divide el texto
print(" ".join(["A", "B", "C"]))  # une el texto por medio de un array
print(mi_texto.replace("prueba", "simulación"))

# Los strings son immutables: el siguiente codigo tirará un error
nombre = "Marco"
# nombre[3] = "k"
# print(nombre)

print(nombre * 10)  # los strings se pueden repetir varias veces usando *

# string con salto de linea
string_salto_linea = """Hola soy un mismo string
con un salto de linea"""
print(string_salto_linea)
print("soy" in string_salto_linea)  # valor booleano para determinar si existe el valor en el string
print("Adios" not in string_salto_linea)  # Mismo caso pero con doble negación
print(len(string_salto_linea))  # para obtener cantidad de caracteres
