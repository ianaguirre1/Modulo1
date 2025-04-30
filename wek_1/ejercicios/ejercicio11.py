# numero1_int = input("digita un numero")
# numero2_int = input("digita un numero")
# numero3_int = input("digita un numero")
<<<<<<< HEAD
while (True):

    try:
        numero1_int = input("digita el primer numero")
        numero1 = int(numero1_int)
        print(f"numero elegido: {numero1}")
        
        numero2_int = input("digita el segundo numero")
        numero2 = int(numero2_int)
        print(f"numero elegido: {numero2}")
        
        numero3_int = input("digita el tercer numero")
        numero3 = int(numero3_int)
        print(f"numero elegido: {numero3}")
        
        if numero1_int > numero2_int and numero1_int > numero3_int:
            print("el primer numero es mayor")
        elif numero2_int > numero1_int and numero2_int > numero3_int :
            print("el segungo numero es mayor")
            
        else:
            ("el tercer numero es mayor")
            
            continue
            
        break

    except ValueError:
            print("Ingresa un número entero valido")
=======
# Validar el primer número
while True:
    try:
        numero1_int = input("Digita el primer número: ")
        numero1 = int(numero1_int)
        print(f"Número elegido: {numero1}")
        break  # Sale del while solo si todo va bien
    except ValueError:
        print("Ingresa un número entero válido")

# Validar el segundo número
while True:
    try:
        numero2_int = input("Digita el segundo número: ")
        numero2 = int(numero2_int)
        print(f"Número elegido: {numero2}")
        break
    except ValueError:
        print("Ingresa un número entero válido")

# Validar el tercer número
while True:
    try:
        numero3_int = input("Digita el tercer número: ")
        numero3 = int(numero3_int)
        print(f"Número elegido: {numero3}")
        break
    except ValueError:
        print("Ingresa un número entero válido")

    # Comparar los números
    if numero1 > numero2 and numero1 > numero3:
        print("El primer número es el mayor")
    elif numero2 > numero1 and numero2 > numero3:
        print("El segundo número es el mayor")
    else:
        print("El tercer número es el mayor")


>>>>>>> c993df9 (se)

   