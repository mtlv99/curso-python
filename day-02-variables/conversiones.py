num1 = 5.8

print(num1)
print(type(num1))  # float

# convertir a int quitará los decimales
num2 = int(num1)
print(num2)
print(type(num2))  # int

edad = input("Dime tu edad: ")
edad = int(edad)
nueva_edad = 1 + edad

# Para imprimirlo hay que convertir el num de vuelta a string, pero mas adelante se verá como formatear strings
print("Tu nueva edad va a ser " + str(nueva_edad))

