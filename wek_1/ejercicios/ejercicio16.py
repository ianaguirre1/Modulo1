lista = list(range(1,11))

while True:
    try:
        numero = int(input("ingresa un numero valido"))
        for i in lista:
            if i == numero:
                print("encontre el numero")
                break
        else:
            print("no encontre el numero")
            continue
        break
    except ValueError:
        print("ingresa un caracter valido")
        
                
    
        
                
            