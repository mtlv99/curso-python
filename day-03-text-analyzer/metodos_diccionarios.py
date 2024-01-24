# DICCIONARIOS

diccionario = {'c1': 'valor1', 'c2': 'valor2'}
print(diccionario)
print(type(diccionario))  # type : <class 'dict'>

resultado = diccionario['c1']
print(resultado)

dic = {
    'c1': 55,
    'c2': [10, 20, 30],
    'c3': {  # dicts dentro de dicts
        's1': 100,
        's2': 200
    }
}

print(dic['c2'][1])
print(dic['c3']['s1'])

dic2 = {'c1': ['a', 'b', 'c'], 'c2': ['d', 'e', 'f']}
print(dic2['c2'][1].upper())

dic2['c3'] = 'Soy nuevo'  # para agregar elementos nuevos, similar a JS

# metodos key/value
print(dic2.keys())
print(dic2.values())
print(dic.items())  # tuples
print('c1' in dic2)
