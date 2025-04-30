lista = list(range(1,11))

while True:
    try:
        numero = int(input("ingrese un numero"))
        for i in lista:
            if numero == i:
                print("encontre el numero")
                break
        else:
                print("no encontre el numero")
        break
    except ValueError:
        print("estos caracateres no son validos")
        break
        
            

