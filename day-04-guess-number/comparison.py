mi_bool = 100.0 == 100  # son lo mismo a pesar de que tengan diferentes tipos

print(mi_bool)

#  operadores de comparacion
operador_and = (4 < 5) and (5 == 2+3)
operador_or = 1 == 10 or 3 == 3

print(operador_and)
print(operador_or)

texto = "esta frase es breve"
mi_bool2 = ('frase' in texto) and ('breve' in texto)
print(mi_bool2)

#  negacion
mi_bool_negativo = not ('a' == 'a')
print(mi_bool_negativo)

# if
edad = 20
calificacion = 10

if edad > 18:
    print('Eres mayor de edad')
    if calificacion >= 7:
        print('Aprobado')
    else:
        print('Reprobado')
else:
    print('Eres menor de edad')
