# Match
# A partir de la 3.10 se incluye match, similar a los switch de otros lenguajes de programación.

serie = "N-O2"

match serie:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:  # valor por default
        print("No existe ese producto")

# Ejemplo
cliente = {'nombre': 'Federico', 'edad': 45, 'ocupacion': 'instructor'}
pelicula = {'titulo': 'Matrix', 'ficha_tecnica': {'protagonista': 'Keanu Reeves', 'director': 'Lana y Lilly Wachowski'}}

elementos = [cliente, pelicula, 'libro']

# creo que no hay break entre opciones...
for e in elementos:
    match e:
        # se pueden hacer cases complejos (por ej. acá que siga cierta estructura)
        case {'nombre': nombre, 'edad': edad, 'ocupacion': ocupacion}:
            print("Es un cliente")
            print(nombre, edad, ocupacion)
        case {'titulo': titulo, 'ficha_tecnica': {'protagonista': protagonista, 'director': director}}:
            print("Es una película")
        case _:
            print("No match")
