nombre = "Ana"
edad = 30
print("Hola,", nombre)  # Salida: Hola, Ana
print("Nombre:", nombre, "Edad:", edad, sep="-")  # Salida: Nombre:-Ana-Edad:-30
print("Esta línea termina sin salto de línea.", end="")
print(" Esta continúa en la misma línea.")  # Salida: Esta línea termina sin salto de línea. Esta continúa en la misma línea.

###############

nombre_usuario = input("Por favor, ingresa tu nombre: ")
print(f"Hola, {nombre_usuario}!")

edad_str = input("Ingresa tu edad: ")  # La entrada siempre es una cadena
edad = int(edad_str)  # Necesitamos convertirla a entero si queremos trabajar con ella como número
print(f"Tienes {edad} años.")


###############

numero_str = "123"
numero_int = int(numero_str)
print(f"La cadena '{numero_str}' convertida a entero es: {numero_int}, y su tipo es: {type(numero_int)}")

numero_binario_str = "1011"
numero_decimal = int(numero_binario_str, 2)  # Convertir desde base 2
print(f"El binario '{numero_binario_str}' en decimal es: {numero_decimal}")

numero_float = 3.14159
numero_entero_truncado = int(numero_float)  # Trunca la parte decimal
print(f"El float {numero_float} truncado a entero es: {numero_entero_truncado}")

#########################################

cadena_decimal = "3.14159"
numero_flotante = float(cadena_decimal)
print(f"La cadena '{cadena_decimal}' convertida a float es: {numero_flotante}, y su tipo es: {type(numero_flotante)}")

numero_entero = 10
numero_flotante_desde_entero = float(numero_entero)
print(f"El entero {numero_entero} convertido a float es: {numero_flotante_desde_entero}")


#####################################

numero = 123
cadena_numero = str(numero)
print(f"El número {numero} convertido a cadena es: '{cadena_numero}', y su tipo es: {type(cadena_numero)}")

lista = [1, 2, 3]
cadena_lista = str(lista)
print(f"La lista {lista} convertida a cadena es: '{cadena_lista}'")

booleano = True
cadena_booleano = str(booleano)
print(f"El booleano {booleano} convertido a cadena es: '{cadena_booleano}'")


##################################

print(f"bool(0): {bool(0)}")
print(f"bool(1): {bool(1)}")
print(f"bool(-1): {bool(-1)}")
print(f"bool([]): {bool([])}")
print(f"bool([1, 2]): {bool([1, 2])}")
print(f"bool(''): {bool('')}")
print(f"bool('hola'): {bool('hola')}")
print(f"bool(None): {bool(None)}")


####################################

numero = 10
cadena = "hola"
lista = [1, 2]
diccionario = {"a": 1}

print(f"El tipo de {numero} es: {type(numero)}")
print(f"El tipo de '{cadena}' es: {type(cadena)}")
print(f"El tipo de {lista} es: {type(lista)}")
print(f"El tipo de {diccionario} es: {type(diccionario)}")

#####################################

print(f"abs(-5): {abs(-5)}")
print(f"abs(5): {abs(5)}")
print(f"abs(-3.14): {abs(-3.14)}")

#######################################

print(f"pow(2, 3): {pow(2, 3)}")  # 2 elevado a 3 es 8
print(f"pow(5, 2): {pow(5, 2)}")  # 5 elevado a 2 es 25
print(f"pow(2, 3, 5): {pow(2, 3, 5)}")  # (2 ** 3) % 5 = 8 % 5 = 3

####################################


print(f"round(3.14159): {round(3.14159)}")  # Redondea al entero más cercano: 3
print(f"round(3.14159, 2): {round(3.14159, 2)}")  # Redondea a 2 decimales: 3.14
print(f"round(3.7): {round(3.7)}")  # Redondea a 4
print(f"round(3.5): {round(3.5)}")  # Redondea a 4 (redondeo al par en Python 3)
print(f"round(12345, -3): {round(12345, -3)}")  # Redondea a las miles: 12000.0

#######################################

lista_numeros = [10, 5, 20, 15]
print(f"max(lista_numeros): {max(lista_numeros)}")  # Salida: 20

print(f"max(1, 5, 2, 8): {max(1, 5, 2, 8)}")  # Salida: 8

cadena = "zebra"
print(f"max(cadena): {max(cadena)}")  # Salida: 'z' (basado en el orden alfabético)

###########################################

lista_numeros = [10, 5, 20, 15]
print(f"min(lista_numeros): {min(lista_numeros)}")  # Salida: 5

print(f"min(1, 5, 2, 8): {min(1, 5, 2, 8)}")  # Salida: 1

cadena = "zebra"
print(f"min(cadena): {min(cadena)}")  # Salida: 'b'

############################################

lista_numeros = [1, 2, 3, 4, 5]
print(f"sum(lista_numeros): {sum(lista_numeros)}")  # Salida: 15

print(f"sum(lista_numeros, 10): {sum(lista_numeros, 10)}")  # Salida: 25 (10 + 1 + 2 + 3 + 4 + 5)

######################################


cadena = "hola"
print(f"len('{cadena}'): {len(cadena)}")  # Salida: 4

lista = [1, 2, 3, 4]
print(f"len({lista}): {len(lista)}")  # Salida: 4

diccionario = {"a": 1, "b": 2}
print(f"len({diccionario}): {len(diccionario)}")  # Salida: 2 (número de claves)


#########################################

for i in range(5):  # Genera 0, 1, 2, 3, 4
    print(i, end=" ")  # Salida: 0 1 2 3 4

print()

for i in range(2, 10, 2):  # Genera 2, 4, 6, 8
    print(i, end=" ")  # Salida: 2 4 6 8

print()

for i in range(5, 0, -1):  # Genera 5, 4, 3, 2, 1
    print(i, end=" ")  # Salida: 5 4 3 2 1
    
    
######################################

tupla = (1, 2, 3)
lista_desde_tupla = list(tupla)
print(f"Tupla: {tupla}, Lista desde tupla: {lista_desde_tupla}")

cadena = "hola"
lista_desde_cadena = list(cadena)
print(f"Cadena: '{cadena}', Lista desde cadena: {lista_desde_cadena}")

generador = (x**2 for x in range(3))
lista_desde_generador = list(generador)
print(f"Lista desde generador: {lista_desde_generador}")

######################################


lista = [1, 2, 3]
tupla_desde_lista = tuple(lista)
print(f"Lista: {lista}, Tupla desde lista: {tupla_desde_lista}")

cadena = "mundo"
tupla_desde_cadena = tuple(cadena)
print(f"Cadena: '{cadena}', Tupla desde cadena: {tupla_desde_cadena}")


#################################

lista_con_duplicados = [1, 2, 2,]


######################

mi_tupla = (10, 20, 30)
a, b, c = mi_tupla

print(f"a: {a}")  # Salida: a: 10
print(f"b: {b}")  # Salida: b: 20
print(f"c: {c}")  # Salida: c: 30


###########################

datos = ("Juan", 25, "Ingeniero", "Medellín")
nombre, edad, profesion, _ = datos  # Ignoramos la ciudad

print(f"Nombre: {nombre}")    # Salida: Nombre: Juan
print(f"Edad: {edad}")      # Salida: Edad: 25
print(f"Profesión: {profesion}") # Salida: Profesión: Ingeniero
# La variable _ existe pero no la usamos

#########################

numeros = (1, 2, 3, 4, 5)
primero, segundo, *resto = numeros

print(f"Primero: {primero}")  # Salida: Primero: 1
print(f"Segundo: {segundo}")  # Salida: Segundo: 2
print(f"Resto: {resto}")    # Salida: Resto: [3, 4, 5]

otros_numeros = (10, 20, 30, 40)
*inicio, ultimo = otros_numeros

print(f"Inicio: {inicio}")   # Salida: Inicio: [10, 20, 30]
print(f"Último: {ultimo}")   # Salida: Último: 40

mezclados = (True, "Hola", 3.14, "Mundo", False)
booleano1, *mensajes, booleano2 = mezclados

print(f"Booleano 1: {booleano1}")  # Salida: Booleano 1: True
print(f"Mensajes: {mensajes}")    # Salida: Mensajes: ['Hola', 3.14, 'Mundo']
print(f"Booleano 2: {booleano2}")  # Salida: Booleano 2: False

#################################
mi_diccionario = {"a": 1, "b": 2, "c": 3}
for clave, valor in mi_diccionario.items():
    print(f"Clave: {clave}, Valor: {valor}") 
    
################################

punto = (10, 5)
x, y = punto
print(f"Coordenada x: {x}, Coordenada y: {y}")

##########################
mi_lista = [100, 200, 300, 400, 500]
primero, *_, ultimo = mi_lista
print(f"Primer elemento: {primero}, Último elemento: {ultimo}")


###########################LISTASSSSSSSSSSSSSSS

mi_lista = [3, 1, 4, 1, 5, 9, 2, 6]

# len(): Obtener la longitud de la lista
print(f"Longitud de la lista: {len(mi_lista)}")  # Salida: Longitud de la lista: 8

# max(): Obtener el elemento más grande
print(f"Elemento máximo: {max(mi_lista)}")  # Salida: Elemento máximo: 9

# min(): Obtener el elemento más pequeño
print(f"Elemento mínimo: {min(mi_lista)}")  # Salida: Elemento mínimo: 1

# sum(): Sumar los elementos
print(f"Suma de los elementos: {sum(mi_lista)}")  # Salida: Suma de los elementos: 31

# sorted(): Obtener una nueva lista ordenada
lista_ordenada = sorted(mi_lista)
print(f"Lista ordenada: {lista_ordenada}")  # Salida: Lista ordenada: [1, 1, 2, 3, 4, 5, 6, 9]

# append(): Añadir al final
mi_lista.append(7)
print(f"Lista después de append(7): {mi_lista}")  # Salida: Lista después de append(7): [3, 1, 4, 1, 5, 9, 2, 6, 7]

# insert(): Insertar en un índice
mi_lista.insert(2, 10)
print(f"Lista después de insert(2, 10): {mi_lista}")  # Salida: Lista después de insert(2, 10): [3, 1, 10, 4, 1, 5, 9, 2, 6, 7]

# remove(): Eliminar la primera aparición
mi_lista.remove(1)
print(f"Lista después de remove(1): {mi_lista}")  # Salida: Lista después de remove(1): [3, 10, 4, 1, 5, 9, 2, 6, 7]

# pop(): Eliminar y devolver por índice (último por defecto)
elemento_eliminado = mi_lista.pop()
print(f"Elemento eliminado con pop(): {elemento_eliminado}, Lista restante: {mi_lista}")
# Salida: Elemento eliminado con pop(): 7, Lista restante: [3, 10, 4, 1, 5, 9, 2, 6]

elemento_eliminado_indice_2 = mi_lista.pop(2)
print(f"Elemento eliminado con pop(2): {elemento_eliminado_indice_2}, Lista restante: {mi_lista}")
# Salida: Elemento eliminado con pop(2): 4, Lista restante: [3, 10, 1, 5, 9, 2, 6]

# index(): Obtener el índice de un elemento
indice_del_5 = mi_lista.index(5)
print(f"Índice del elemento 5: {indice_del_5}")  # Salida: Índice del elemento 5: 3

# count(): Contar ocurrencias
conteo_del_1 = mi_lista.count(1)
print(f"Número de veces que aparece el 1: {conteo_del_1}")  # Salida: Número de veces que aparece el 1: 1

# sort(): Ordenar in-place
mi_lista_desordenada = [5, 1, 8, 2]
mi_lista_desordenada.sort()
print(f"Lista ordenada con sort(): {mi_lista_desordenada}")  # Salida: Lista ordenada con sort(): [1, 2, 5, 8]

# reverse(): Invertir in-place
# mi_lista_ordenada.reverse()
# print(f"Lista invertida con reverse(): {mi_lista_ordenada}")  # Salida: Lista invertida con reverse(): [8, 5, 2, 1]

# # clear(): Eliminar todos los elementos
# mi_lista_ordenada.clear()
# print(f"Lista después de clear(): {mi_lista_ordenada}")  # Salida: Lista después de clear(): []

##################DICCIONARIOSSSSSSSSSSSSSSSSSSSS

mi_diccionario = {"nombre": "Alice", "edad": 30, "ciudad": "Nueva York"}

# len(): Obtener el número de pares clave-valor
print(f"Número de elementos en el diccionario: {len(mi_diccionario)}")  # Salida: Número de elementos en el diccionario: 3

# get(): Obtener un valor por clave (con valor por defecto)
nombre = mi_diccionario.get("nombre")
print(f"Nombre: {nombre}")  # Salida: Nombre: Alice
profesion = mi_diccionario.get("profesion", "Desconocida")
print(f"Profesión: {profesion}")  # Salida: Profesión: Desconocida

# keys(): Obtener las claves
claves = mi_diccionario.keys()
print(f"Claves del diccionario: {claves}")  # Salida: Claves del diccionario: dict_keys(['nombre', 'edad', 'ciudad'])
print(list(claves))  # Convertir a lista para mejor visualización: ['nombre', 'edad', 'ciudad']

# values(): Obtener los valores
valores = mi_diccionario.values()
print(f"Valores del diccionario: {valores}")  # Salida: Valores del diccionario: dict_values(['Alice', 30, 'Nueva York'])
print(list(valores))  # Convertir a lista: ['Alice', 30, 'Nueva York']

# items(): Obtener los pares clave-valor
items = mi_diccionario.items()
print(f"Pares clave-valor del diccionario: {items}")
# Salida: Pares clave-valor del diccionario: dict_items([('nombre', 'Alice'), ('edad', 30), ('ciudad', 'Nueva York')])
print(list(items))  # Convertir a lista de tuplas: [('nombre', 'Alice'), ('edad', 30), ('ciudad', 'Nueva York')]

# update(): Actualizar con otro diccionario
otro_diccionario = {"edad": 31, "profesion": "Ingeniera"}
mi_diccionario.update(otro_diccionario)
print(f"Diccionario después de update(): {mi_diccionario}")
# Salida: Diccionario después de update(): {'nombre': 'Alice', 'edad': 31, 'ciudad': 'Nueva York', 'profesion': 'Ingeniera'}

# pop(): Eliminar por clave y devolver valor
edad_eliminada = mi_diccionario.pop("edad")
print(f"Edad eliminada: {edad_eliminada}, Diccionario restante: {mi_diccionario}")
# Salida: Edad eliminada: 31, Diccionario restante: {'nombre': 'Alice', 'ciudad': 'Nueva York', 'profesion': 'Ingeniera'}

# popitem(): Eliminar y devolver un par arbitrario (último insertado en Python < 3.7)
item_eliminado = mi_diccionario.popitem()
print(f"Item eliminado con popitem(): {item_eliminado}, Diccionario restante: {mi_diccionario}")
# Salida (el orden puede variar): Item eliminado con popitem(): ('profesion', 'Ingeniera'), Diccionario restante: {'nombre': 'Alice', 'ciudad': 'Nueva York'}

# clear(): Eliminar todos los elementos
mi_diccionario.clear()
print(f"Diccionario después de clear(): {mi_diccionario}")  # Salida: Diccionario después de clear(): {}

#########################TUPLASSSSSSSSSSSSSSS


mi_tupla = (10, 20, 30, 20, 40)

# len(): Obtener la longitud
print(f"Longitud de la tupla: {len(mi_tupla)}")  # Salida: Longitud de la tupla: 5

# max(): Obtener el elemento más grande
print(f"Elemento máximo: {max(mi_tupla)}")  # Salida: Elemento máximo: 40

# min(): Obtener el elemento más pequeño
print(f"Elemento mínimo: {min(mi_tupla)}")  # Salida: Elemento mínimo: 10

# sum(): Sumar los elementos
print(f"Suma de los elementos: {sum(mi_tupla)}")  # Salida: Suma de los elementos: 120

# sorted(): Obtener una nueva lista ordenada
tupla_ordenada = sorted(mi_tupla)
print(f"Tupla ordenada (como lista): {tupla_ordenada}")  # Salida: Tupla ordenada (como lista): [10, 20, 20, 30, 40]

# count(): Contar ocurrencias
conteo_del_20 = mi_tupla.count(20)
print(f"Número de veces que aparece el 20: {conteo_del_20}")  # Salida: Número de veces que aparece el 20: 2

# index(): Obtener el índice de un elemento
indice_del_30 = mi_tupla.index(30)
print(f"Índice del elemento 30: {indice_del_30}")  # Salida: Índice del elemento 30: 2

# Las tuplas son inmutables, por lo que no tienen métodos como append, insert, remove, pop, clear, sort, reverse (que modificarían la tupla).


