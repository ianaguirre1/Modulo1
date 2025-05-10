biblioteca = {
    '001': {'titulo': 'Cien años de soledad', 'autor': 'Gabriel García Márquez', 'año': 1967},
    '002': {'titulo': '1984', 'autor': 'George Orwell', 'año': 1949}
}
nuevo_libro = {
    '003': {'titulo': 'El principito', 'autor': 'Antoine de Saint-Exupéry', 'año': 1943},
    '004':{'titulo': 'la cuadra', 'auto': 'Gilmer Messa', 'año': 2016}
}

biblioteca.update(nuevo_libro)
print(biblioteca)

for libro in biblioteca.values():
    print(libro['titulo'])
    
biblioteca.update({'001':{'titulo': 'tomas'}})
print(biblioteca['001']['titulo'])

biblioteca.pop('001')
print(biblioteca)

codigo = (input("ingresa un código"))
libro = (input("ingresa un libro"))
autor = (input("ingresa un autor"))
fecha = int(input("ingesa una fecha"))

nuevo_libro1 = {
    codigo:{
    'titulo': libro,
    'autor': autor,
    'año': fecha}
}
biblioteca.update(nuevo_libro1)

print("\nBiblioteca actualizada:")
for clave, datos in biblioteca.items():
    print(f"{clave}: {datos}")
    
    
diccionario = {
    '001': 'hola'}
    


numero = (input("ingrese un numero"))
contador = {}

for letra in contador:
    if letra in contador:
        contador[letra] = contador[letra] +1
    else:
        contador[letra] = 1

print(contador)

diccionario = {
    '001':{'nombre': 'tomas'},
    '002':{'nombre':'luis'},
    '003':{'nombre':'jose'}
}

for libro in diccionario.values():
    print(libro['nombre'])
   







