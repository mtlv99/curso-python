texto_original = input("Ingresa un texto a analizar: ")
cleaned_text = texto_original.lower()

usuario_letras_array = input("Ingresa tres letras, separadas por comas y sin espacios: ").split(",")

texto_array = cleaned_text.split(" ")
letras_array = list(cleaned_text)

# step 1
count_letra1 = letras_array.count(usuario_letras_array[0])
count_letra2 = letras_array.count(usuario_letras_array[1])
count_letra3 = letras_array.count(usuario_letras_array[2])

# step 2
total_palabras = len(texto_array)

# step 3
primera_letra = cleaned_text[0]
ultima_letra = cleaned_text[-1]

# step 4
texto_array.reverse()
texto_invertido = ' '.join(texto_array)

# step 5
existe_python = ('python' in cleaned_text)
dic_respuestas = {True: "La palabra Python si aparece en el texto.", False: "La palabra Python NO aparece en el texto."}

print("\nResultados\n")

print("Cuantas veces aparecen las letras?")
print(f"La cantidad de ocurrencias de la letra '{usuario_letras_array[0]}' es: {count_letra1}")
print(f"La cantidad de ocurrencias de la letra '{usuario_letras_array[1]}' es: {count_letra2}")
print(f"La cantidad de ocurrencias de la letra '{usuario_letras_array[2]}' es: {count_letra3}\n")

print(f"El total de palabras que tiene el texto es de {total_palabras} palabras")
print(f"La primera letra es '{primera_letra}' y la última letra es '{ultima_letra}'\n")
print(f"El texto al revés se leería como: {texto_invertido}\n")

print(dic_respuestas[existe_python])
