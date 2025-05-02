approved_list = list(range(51, 101))  # Creamos una lista de aprobados
not_approved_list = list(range(0, 51))  # Creamos una lista de no aprobados

# Validar calificación única
while True:  # Bucle infinito que permite reintentar cuando se ingresan datos inválidos
    try:  # Capturamos errores para evitar que el programa se caiga
        score = int(input("Ingresa una calificación numérica (0-100): "))  # Pedimos explícitamente números del 0 al 100
        if score < 0:  # No se acepta número negativos
            print("No se permiten números negativos.")
            continue  # Si los datos no son correctos, vuelve al inicio del while True

        if score in approved_list:  # Si la calificación está en la lista
            print("Aprobaste")  # Aprobamos
        elif score in not_approved_list:  # Si la calificación está en la lista de no aprobados
            print("No aprobaste")
        else:
            print("Estas calificaciones no están dentro del rango")  # Si no están dentro del rango
        break
    except ValueError:
        print("Ingresa datos válidos por favor")  # Datos no válidos

# Validar entrada de lista de calificaciones
while True:
    try:
        input_scores = input("Ingresa las calificaciones separadas por comas (ejemplo: 80,65,35): ")  # Ingresamos las calificaciones desde la terminal
        grades = [int(value.strip()) for value in input_scores.split(",")]  # Creamos una lista donde vamos a castear los números que están como str, con el método .strip logramos borrar los espacios, con el método .split logramos separar por aparte, en este caso las comas
        if any(n < 0 for n in grades):  # Verificamos que no haya números negativos, con ayuda de la función any, y recorremos con ayuda del for
            print("No se permiten calificaciones negativas.")
            continue

        average = sum(grades) / len(grades)  # Sumamos las calificaciones y las dividimos por la cantidad, para sacar el promedio
        print("El promedio es:", average)  # Imprimimos el promedio
        break
    except ValueError:
        print("Ingresa datos válidos por favor")

# Comparar valor para contar calificaciones mayores
while True:
    try:
        compare_value = int(input("Ingresa un valor para contar cuántas calificaciones son mayores: "))
        if compare_value < 0:
            print("No se permiten números negativos.")
            continue

        counter = 0  # Inicializamos una variable en cero
        for grade in grades:  # Vamos a buscar en grades
            if grade > compare_value:  # Cada vez que encontramos un número mayor que el valor ingresado, va a sumar 1 en el contador
                counter += 1

        print("Cantidad de calificaciones mayores a", compare_value, "es:", counter)  # Imprimimos la cantidad de números que son mayores
        break
    except ValueError:
        print("Ingresa datos válidos por favor")

# Verificar y contar calificación específica
while True:
    try:
        count_specific = 0
        val = int(input(f"Escoge una calificación específica de esta lista {grades}: "))  # Escoge una calificación de la lista de calificaciones
        if val < 0:
            print("No se permiten números negativos.")
            continue

        for i in grades:  # Buscamos en grades
            if i == val:  # Si los datos que recorrimos son iguales a lo que ingresamos
                count_specific += 1  # Le sumamos 1 por cada dato que veamos igual

        if count_specific > 0:  # Si count_specific es mayor a cero
            print(f"La calificación sí está, aparece {count_specific} veces.")  # Imprimimos lo que tenemos en el contador
        else:
            print("La calificación no está.")  # Si no encontramos la calificación
        break
    except ValueError:
        print("Ingresa datos válidos")
