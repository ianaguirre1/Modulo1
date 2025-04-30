año_int = input("Ingresa un año: ")
try:
    año = int(año_int)
    print(f"Año elegido: {año}")

    if año % 4 == 0 and año % 100 != 0 or año % 400 == 0:
        print(f"{año} es un año bisiesto")
    else:
        print(f"{año} no es un año bisiesto")

except ValueError:
    print("Ingresa un número entero valido para el año")

