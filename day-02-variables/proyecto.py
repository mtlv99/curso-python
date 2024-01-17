nombre = input("Indique su nombre: ")
ventas = int(input("Indique sus ventas totales del mes: "))

# dos decimales
comision = round(ventas * 0.13, 2)

print(f"Hola {nombre}, tus comisiones de este mes son ${comision}")
