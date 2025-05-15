# objetos = {
# '001':{'objetos':'televisor', 'color':'amarillo', 'precio':12515},
# '002':{'objetos':'ventilador', 'color':'azul', 'precio':151851},
# '003':{'objetos':'nevera', 'color':'morado', 'precio':515118}
# }


# codigo = str(input("ingrese un codigo"))
# objeto = str(input("ingrese un objeto"))
# color = str(input("ingrese un color"))
# while True:
#     try:
#         precio = int(input("ingrese un nuevo precio"))
#         if precio < 0:
#             print("ingrese numeros positivos")
#             continue
#         break
#     except ValueError:
#         print ("ingrese datos valuido por favor")

# nuevos_datos = {
#     codigo: {
#         'objetos':objeto,
#         'color': color,
#         'precio': precio
#     }
# }

# objetos.update(nuevos_datos)

# print("\nnuevos objetos acttulizados")

# for clave, i in objetos.items():
#     print(f"{clave}:{i}")
    
# for t in objetos.values():
#     print(t['objetos'])

    
# objetos.update({'002':{'objetos':1488}})
# print(objetos['001']['objetos'])

# print(objetos)
lista_aprovados = list(range(51,101))
lista_desaprovados = list (range(0,51))

while True:
    try:
        calificacion = int(input("ingrese un calificacion"))
        if 100 < calificacion < 0:    
            print("no se permiten numeros negativos")
            continue
        if calificacion in lista_aprovados:
            print("aprovaste")
        elif calificacion in lista_desaprovados:
            print("desaprovaste")
        else:
            print("estas calificaciones no estan dentro del rango")
            break
    except ValueError:
        print("ingrese datos validos por favor")
        
while True:
    try:
        entrada_calificacion = input("ingresa las calificaciones separadas por comas (ejemplo : 80,65,35)")
        gua = [int(value.strip())for value in entrada_calificacion.split(",")]
        if any(n < 0 for n in gua):
            print("no se permiten numeros negativos")
            continue
        promedio  = sum(gua) / len(gua)
        print("el promedio es", promedio)
        break
    except ValueError:
        print("ingrese datos validos por favor")

while True:
    try:
        comparar_valor = int(input("ingrese un valor para contar cuantas calificaciones son mayores: "))
        if comparar_valor < 0:
            print("no se permiten numeros negativos")
            continue
        contador = 0
        for g in gua:
            if g > comparar_valor:
                contador += 1
        print("cantidad de calificaciones mayores a", comparar_valor, "es:", contador)
        break
    except ValueError:
        print("ingrese datos validos por favor")
        
while True:
    try:
        contador_especifico = 0
        val = int(input(f"escoje una calificacion especifica de esta lista: {gua}: "))
        if val < 0:
            print("no se permite numeros negativos")
            continue
        for i in gua:
            if i == val:
                contador_especifico +=1
                
        if contador > 0:
            print(f"la calificacion si esta, aparece {contador_especifico} veces")
        else:
            print("la calificacion no esta")
        break
    except ValueError:
        print("ingrese datos validos por favor")
        