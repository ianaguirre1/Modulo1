approved_list = list(range(51, 101))  # Creamos una lista de aprobados
not_approved_list = list(range(0, 51))  # Creamos una lista de no aprobados

# Validar calificacion unica
while True:  # Bucle infinito que permite reintentar cuando se ingresan datos invalidos
    try:  # Capturamos errores para evitar que el programa se caiga
        score = int(input("Ingresa una calificacion numerica (0-100): "))  # Pedimos explicitamente numeros del 0 al 100
        if score < 0:  # No se acepta numero negativos
            print("No se permiten numeros negativos")
            continue  # Si los datos no son correctos, vuelve al inicio del while True

        if score in approved_list:  # Si la calificacion esta en la lista
            print("Aprobaste")  # Aprobamos
        elif score in not_approved_list:  # Si la calificacion esta en la lista de no aprobados
            print("No aprobaste")
        else:
            print("Estas calificaciones no estan dentro del rango")  # Si no estan dentro del rango
        break
    except ValueError:
        print("Ingresa datos validos por favor")  # Datos no validos

# Validar entrada de lista de calificaciones
while True:
    try:
        input_scores = input("Ingresa las calificaciones separadas por comas (ejemplo: 80,65,35): ")  # Ingresamos las calificaciones desde la terminal
        grades = [int(value.strip()) for value in input_scores.split(",")]  # Creamos una lista donde vamos a castear los numeros que estan como str, con el metodo .strip logramos borrar los espacios, con el metodo .split logramos separar por aparte, en este caso las comas
        if any(n < 0 for n in grades):  # Verificamos que no haya numeros negativos, con ayuda de la funcion any, y recorremos con ayuda del for
            print("No se permiten calificaciones negativas")
            continue

        average = sum(grades) / len(grades)  # Sumamos las calificaciones y las dividimos por la cantidad, para sacar el promedio
        print("El promedio es:", average)  # Imprimimos el promedio
        break
    except ValueError:
        print("Ingresa datos validos por favor")

# Comparar valor para contar calificaciones mayores
while True:
    try:
        compare_value = int(input("Ingresa un valor para contar cuantas calificaciones son mayores: "))
        if compare_value < 0:
            print("No se permiten numeros negativos")
            continue

        counter = 0  # Inicializamos una variable en cero
        for grade in grades:  # Vamos a buscar en grades
            if grade > compare_value:  # Cada vez que encontramos un numero mayor que el valor ingresado, va a sumar 1 en el contador
                counter += 1

        print("Cantidad de calificaciones mayores a", compare_value, "es:", counter)  # Imprimimos la cantidad de numeros que son mayores
        break
    except ValueError:
        print("Ingresa datos validos por favor")

# Verificar y contar calificacion especifica
while True:
    try:
        count_specific = 0
        val = int(input(f"Escoge una calificacion especifica de esta lista {grades}: "))  # Escoge una calificacion de la lista de calificaciones
        if val < 0:
            print("No se permiten numeros negativos")
            continue

        for i in grades:  # Buscamos en grades
            if i == val:  # Si los datos que recorrimos son iguales a lo que ingresamos
                count_specific += 1  # Le sumamos 1 por cada dato que veamos igual

        if count_specific > 0:  # Si count_specific es mayor a cero
            print(f"La calificacion si esta, aparece {count_specific} veces")  # Imprimimos lo que tenemos en el contador
        else:
            print("La calificacion no esta")  # Si no encontramos la calificacion
        break
    except ValueError:
        print("Ingresa datos validos")
