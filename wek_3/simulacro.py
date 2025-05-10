Escuela = {
    '001':{'nombre': 'Mateo', 'edad': 16, 'nota':4.5},
    '002':{'nombre': 'Luis', 'edad': 18, 'nota':5.0},
    '003':{'nombre': 'Albeiro', 'edad': 19, 'nota':3.5},
    '004':{'nombre': 'Jose', 'edad': 15, 'nota':4.5},
    '005':{'nombre': 'Sebastian', 'edad': 14, 'nota':4.8}
}

contra = "escuela"

def mostrar_menu():
    """Muestra el menú principal del inventario."""
    print("\nMENU")
    print("1. Añadir estudiante")
    print("2. Buscar estudiante")
    print("2. Buscar estudiante")
    print("3. Actualizar edad del estudiante")
    print("4. Actualizar nota del estudiante")
    print("5. Eliminar estudiantes")
    print("6. Salir")
    
def autenticar():
    """Autenticacion"""
    while True:
        contraseña_ingresada = input("Ingrese la contraseña de acceso: ")
        if contraseña_ingresada == contra:
            print("Autenticación exitosa")
            return True
        else:
            print("Contraseña incorrecta.")
            
def añadir_estudiante():
    """Permite al usuario ingresar nuevos estudiantes."""
    id_nuevo = input("Ingrese una ID unica para el estudiante: ")
    if id_nuevo in Escuela:
        print("El estudiante ya está registrado")
    else: 
        
        nombre_nuevo = input("Ingrese el nombre del produ: ")
        edad_nueva = input("Ingrese el precio del producto: ")
        nota_nueva = input("Ingrese la cantidad del producto: ")

        nuevo_estudiantes = {
            id_nuevo: {
                'nombre': nombre_nuevo,
                'edad': int(edad_nueva),
                'nota': int(nota_nueva)
            }
        }
        Escuela.update(nuevo_estudiantes)
        print(f"Estudiante con ID: '{id_nuevo}' añadido a la Escula.")

def buscar_estudiante_nombre():
    nombre = input("ingrese el nombre del estudiante")
    if Escuela[nombre]['nombre'] == nombre:
        print(f"El estudiante {nombre} está en la lista")
    else:
        print("El estudiante no está registrado")
    
def buscar_Estudiante_id():
    """Permite al usuario ingresar estudiantes a la base de datos."""
    id = input("Ingrese el código del producto para ver el precio: ")#pen

    if id in Escuela:
        print(f"Estudiante: {Escuela[id]['nombre']}")
    else:
        print("No se encontró el estudiante")

    
def actualizar_edad_estudiante():
    """Permite actualizar la información del estudiante"""
    estudiantes_actualizar = input("ingrese la ID del estudiante que desea actualizar: ")
    if estudiantes_actualizar in Escuela:
        nuevo_edad_str = input(f"Ingrese un nueva edad para {Escuela[estudiantes_actualizar]['nombre']}: ")
        try:
            if int(nuevo_edad_str) < 0:
                print("no se permiten numeros negativos")
                return
            nuevo_edad = int(nuevo_edad_str)
            Escuela[estudiantes_actualizar]['edad'] = nuevo_edad
            print(f"La edad de {Escuela[estudiantes_actualizar]['nombre']} ha sido actualizado a {nuevo_edad}.")
        except ValueError:
            print("La nota ingresada no es un número válido.")
    else:
        print("Código de producto inválido.")
        
def actualizar_nota_estudiante():
    """Permite actualizar la información del estudiante"""
    estudiantes_actualizar = input("ingrese la ID del estudiante que desea actualizar: ")
    if estudiantes_actualizar in Escuela:
        nuevo_nota_str = input(f"Ingrese un nueva nota para {Escuela[estudiantes_actualizar]['nombre']}: ")
        try:
            if float(nuevo_nota_str) < 0.0 or float(nuevo_nota_str) > 5.0:
                print("No es posible insertar la nota. El rango es entre 0.0 y 5.0")
                return
            nuevo_nota = float(nuevo_nota_str)
            Escuela[estudiantes_actualizar]['nota'] = nuevo_nota
            print(f"La nota de {Escuela[estudiantes_actualizar]['nombre']} ha sido actualizado a {nuevo_nota}.")
        except ValueError:
            print("La nota ingresada no es un número válido.")
    else:
        print("Código de producto inválido.")     
        
def Eliminar_estudiantes():
    """permite borrar el estudiante"""
    Eliminar= input("Ingrese la ID del estudiante que desea Eliminar: ")
    if Eliminar in Escuela:
        Escuela.pop(Eliminar)
        

if autenticar():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            añadir_estudiante()
        elif opcion == '2':
            buscar_estudiante_nombre()
        elif opcion == '3':
            buscar_Estudiante_id()
        elif opcion == '4':
            actualizar_edad_estudiante()
        elif opcion == "5":
            actualizar_nota_estudiante()
        elif opcion == '6':
            Eliminar_estudiantes() 
        elif opcion == '7':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")
else:
    print("El programa finalizó debido a un error de autenticación.")






"""Actualizar información de un estudiante:

Deben poder actualizar la nota o la edad de un estudiante.
La nota debe estar entre 0.0 y 5.0.
La edad debe ser un número entero positivo.    
            """

        