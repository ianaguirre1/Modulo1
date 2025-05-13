Escuela = {
    '001': {'nombre': 'Mateo', 'edad': 16, 'nota': 4.5},
    '002': {'nombre': 'Luis', 'edad': 18, 'nota': 5.0},
    '003': {'nombre': 'Albeiro', 'edad': 19, 'nota': 2.6},
    '004': {'nombre': 'Jose', 'edad': 15, 'nota': 2.5},
    '005': {'nombre': 'Sebastian', 'edad': 14, 'nota': 4.8}
}
# Diccionario 'Escuela' para almacenar datos de los estudiantes.

contrasena = "escuela"
# Contraseña para acceder al sistema.

def mostrar_menu():
    """Muestra el menú principal del inventario."""
    print("\nMENU")
    print("1. Añadir estudiante")
    print("2. Buscar estudiante por nombre")
    print("3. Buscar estudiante por id")
    print("4. Actualizar edad del estudiante")
    print("5. Actualizar nota del estudiante")
    print("6. Eliminar estudiantes")
    print("7. Calcular promedio de estudiantes")
    print("8. Umbral de estudiantes por debajo de 3.0")
    print("9. Salir")

def autenticar():
    """Autenticación"""
    while True:
        contrasena_ingresada = input("Ingrese la contraseña de acceso: ")
        if contrasena_ingresada == contrasena:
            print("Autenticación exitosa")
            return True # Inicio de sesión exitoso.
        else:
            print("Contraseña incorrecta.") # Contraseña incorrecta.

def añadir_estudiante():
    """Permite al usuario ingresar nuevos estudiantes."""
    nuevo_id = input("Ingrese una ID única para el estudiante: ")
    if nuevo_id in Escuela:
        print("El estudiante ya está registrado") # El estudiante ya existe.
    else:
        nuevo_nombre = input("Ingrese el nombre del estudiante: ")
        nueva_edad = input("Ingrese la edad del estudiante: ")
        nueva_nota = input("Ingrese la nota del estudiante: ")

        nuevo_estudiante = {
            nuevo_id: {
                'nombre': nuevo_nombre,
                'edad': int(nueva_edad),
                'nota': float(nueva_nota)
            }
        }
        Escuela.update(nuevo_estudiante) # Añadir nuevo estudiante a Escuela.
        print(f"Estudiante con ID: '{nuevo_id}' añadido a la Escuela.") # Confirmación.

def buscar_estudiante_por_nombre():
    nombre_a_buscar = input("Ingrese el nombre del estudiante a buscar: ")
    encontrado = False
    for estudiante_id, info_estudiante in Escuela.items():
        if info_estudiante['nombre'].lower() == nombre_a_buscar.lower():
            print(f"ID: {estudiante_id}, Nombre: {info_estudiante['nombre']}, Edad: {info_estudiante['edad']}, Nota: {info_estudiante['nota']}")
            encontrado = True
    if not encontrado:
        print(f"No se encontró ningún estudiante con el nombre '{nombre_a_buscar}'.")

def buscar_estudiante_por_id():
    """Permite al usuario buscar estudiantes por su ID."""
    id_a_buscar = input("Ingrese el ID del estudiante a buscar: ")

    if id_a_buscar in Escuela: # Verificar si el ID existe.
        info_estudiante = Escuela[id_a_buscar]
        print(f"ID: {id_a_buscar}, Nombre: {info_estudiante['nombre']}, Edad: {info_estudiante['edad']}, Nota: {info_estudiante['nota']}") # Mostrar nombre del estudiante.
    else:
        print("No se encontró el estudiante") # No se encontró el estudiante.

def actualizar_edad_estudiante():
    """Permite actualizar la información del estudiante"""
    estudiante_a_actualizar = input("Ingrese la ID del estudiante cuya edad desea actualizar: ")
    if estudiante_a_actualizar in Escuela:
        nueva_edad_str = input(f"Ingrese la nueva edad para {Escuela[estudiante_a_actualizar]['nombre']}: ")
        try:
            nueva_edad = int(nueva_edad_str)
            if nueva_edad >= 0:
                Escuela[estudiante_a_actualizar]['edad'] = nueva_edad # Actualizar edad.
                print(f"La edad de {Escuela[estudiante_a_actualizar]['nombre']} ha sido actualizada a {nueva_edad}.") # Confirmación.
            else:
                print("La edad no puede ser un número negativo.") # Edad negativa no permitida.
        except ValueError:
            print("La edad ingresada no es un número válido.") # Entrada de edad inválida.
    else:
        print(f"No se encontró ningún estudiante con el ID '{estudiante_a_actualizar}'.") # ID de estudiante inválido.

def actualizar_nota_estudiante():
    """Permite actualizar la información del estudiante"""
    estudiante_a_actualizar = input("Ingrese la ID del estudiante cuya nota desea actualizar: ")
    if estudiante_a_actualizar in Escuela:
        nueva_nota_str = input(f"Ingrese la nueva nota para {Escuela[estudiante_a_actualizar]['nombre']}: ")
        try:
            nueva_nota = float(nueva_nota_str)
            if 0.0 <= nueva_nota <= 5.0:
                Escuela[estudiante_a_actualizar]['nota'] = nueva_nota # Actualizar nota.
                print(f"La nota de {Escuela[estudiante_a_actualizar]['nombre']} ha sido actualizada a {nueva_nota}.") # Confirmación.
            else:
                print("La nota debe estar entre 0.0 y 5.0.") # Rango de nota debe ser 0.0 a 5.0.
        except ValueError:
            print("La nota ingresada no es un número válido.") # Entrada de nota inválida.
    else:
        print(f"No se encontró ningún estudiante con el ID '{estudiante_a_actualizar}'.") # ID de estudiante inválido.

def calcular_promedio_notas():
    """Permite calcular el promedio de las notas"""
    total_notas = 0
    cantidad_estudiantes = 0
    for info_estudiante in Escuela.values():
        total_notas += info_estudiante['nota']
        cantidad_estudiantes += 1

    if cantidad_estudiantes > 0:
        promedio = total_notas / cantidad_estudiantes
        print(f"El promedio de las notas de los estudiantes es: {promedio:.2f}") # Mostrar promedio de notas.
    else:
        print("No hay notas para calcular el promedio.") # No hay notas para calcular el promedio.

def umbral_notas_bajas():
    """Muestra la cantidad y nombres de estudiantes con notas por debajo de 3.0."""
    estudiantes_bajo_umbral = []
    cantidad_estudiantes = 0
    for estudiante_id, info_estudiante in Escuela.items():
        if info_estudiante['nota'] < 3.0:
            estudiantes_bajo_umbral.append(info_estudiante['nombre'])
            cantidad_estudiantes += 1

    if cantidad_estudiantes > 0:
        print(f"\nHay {cantidad_estudiantes} estudiantes con notas por debajo de 3.0:") # Mostrar cantidad de estudiantes bajo el umbral.
        for nombre in estudiantes_bajo_umbral:
            print(f"- {nombre}") # Mostrar nombres de estudiantes bajo el umbral.
    else:
        print("\nNo hay estudiantes con notas por debajo de 3.0.") # No hay estudiantes bajo el umbral.

def eliminar_estudiantes():
    """permite borrar el estudiante"""
    estudiante_a_eliminar = input("Ingrese la ID del estudiante que desea Eliminar: ")
    if estudiante_a_eliminar in Escuela:
        confirmacion = input(f"¿Está seguro de que desea eliminar a {Escuela[estudiante_a_eliminar]['nombre']}? (si/no): ")
        if confirmacion.lower() == "si":
            del Escuela[estudiante_a_eliminar] # Eliminar el estudiante.
            print(f"El estudiante con ID {estudiante_a_eliminar} ha sido eliminado.") # Confirmación.
        elif confirmacion.lower() == "no":
            print("La eliminación ha sido cancelada.") # Eliminación cancelada.
        else:
            print("Respuesta inválida. Por favor, ingrese 'si' o 'no'.") # Respuesta de confirmación inválida.
    else:
        print(f"No se encontró ningún estudiante con la ID {estudiante_a_eliminar}.") # No se encontró el ID del estudiante.


if autenticar(): # Iniciar programa principal si la autenticación es exitosa.
    while True: # Bucle principal del programa.
        mostrar_menu() # Mostrar menú.
        opcion = input("Seleccione una opción: ") # Obtener la opción del usuario.

        if opcion == '1':
            añadir_estudiante()
        elif opcion == '2':
            buscar_estudiante_por_nombre()
        elif opcion == '3':
            buscar_estudiante_por_id()
        elif opcion == '4':
            actualizar_edad_estudiante()
        elif opcion == "5":
            actualizar_nota_estudiante()
        elif opcion == '6':
            eliminar_estudiantes()
        elif opcion == '7':
            calcular_promedio_notas()
        elif opcion == '8':
            umbral_notas_bajas()
        elif opcion == '9':
            print("Saliendo del programa.") # Salir del programa.
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.") # Opción inválida.
else:

    print("El programa finalizó debido a un error de autenticación.") # Fallo de autenticación.

    print("El programa finalizó debido a un error de autenticación.") # Authentication failed.







        

