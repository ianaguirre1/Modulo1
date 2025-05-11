#Creamo un diccionario de diccionarios, este es el inventario
Inventario = {
    '001': {'producto': 'aceite', 'precio': 8000, 'cantidad': 50},
    '002': {'producto': 'arepas', 'precio': 2500, 'cantidad': 40},
    '003': {'producto': 'arroz', 'precio': 3000, 'cantidad': 35},
}
#creamos una contraseña de acceso al inventario
Contra = "skalibut"
#creamo un menu de opciones para mostrar al usuario
def mostrar_inventario():
    """Muestra el menu principal del inventario."""
    print("\nInventario")
    print("1. Mostrar inventario completo")
    print("2. Buscar precio de producto")
    print("3. Buscar cantidad de producto")
    print("4. Ingresar productos")
    print("5. Actualizar precio de producto")
    print("6. Eliminar productos")
    print("7. Calcular valor total del inventario")
    print("8. Salir")
#autenticamos el inicio de seccion en el inventario
def autenticar():
    """Autenticacion"""
    while True:
        contrasena_ingresada = input("Ingrese la contrasena de acceso: ")
        if contrasena_ingresada == Contra:
            print("Autenticacion exitosa")
            return True
        else:
            print("Contrasena incorrecta.")
#mostramos el inventario completo
def mostrar_inventario_completo():
    """Muestra todos los productos en el inventario."""
    print("\n--- Inventario Completo ---")
    for codigo, producto_info in Inventario.items():
        print(f"Codigo: {codigo}")
        for clave, valor in producto_info.items():
            print(f"  {clave.capitalize()}: {valor}")
        print("-" * 20)
#buscamos el precio mediante el acceso al inventario por medio de las claves del Diccionario principal
def buscar_precio():
    """Permite al usuario buscar el precio de un producto."""
    codigo_producto = input("Ingrese el codigo del producto para ver el precio: ")
    if codigo_producto in Inventario:
        print(f"El precio de {Inventario[codigo_producto]['producto']} es: {Inventario[codigo_producto]['precio']}")
    else:
        print("Codigo de producto invalido.")
#buscamos la  cantidad de productos que tenemos, mediante las claves del primer Diccionario principal
def buscar_cantidad():
    """Permite al usuario buscar la cantidad de un producto."""
    codigo_producto = input("Ingrese el codigo del producto para ver la cantidad: ")
    if codigo_producto in Inventario:
        print(f"La cantidad de {Inventario[codigo_producto]['producto']} es: {Inventario[codigo_producto]['cantidad']}")
    else:
        print("Codigo de producto invalido.")
#añadimos productos nuevos al inventario, esto lo logramos mediante otro diccionario a los cuales inyectamos datos, y luego los agregamos al diccionario principal
def añadir_producto():
    """Permite al usuario añadir un nuevo producto al inventario."""
    codigo_nuevo = input("Ingrese un codigo unico para el nuevo producto: ")
    nombre_producto = input("Ingrese el nombre del producto: ")
    precio_producto = input("Ingrese el precio del producto: ")
    cantidad_producto = input("Ingrese la cantidad del producto: ")
#diccionario nuevo
    nuevo_producto = {
        codigo_nuevo: {
            'producto': nombre_producto,
            'precio': int(precio_producto),
            'cantidad': int(cantidad_producto)
        }
    }
    Inventario.update(nuevo_producto)
    print(f"Producto con codigo '{codigo_nuevo}' anadido al inventario.")
#actualizamos los precios de los productos 
def actualizar_precio():
    """Permite al usuario seleccionar un producto y actualizar su precio."""
    codigo_actualizar = input("Ingrese el codigo del producto cuyo precio desea actualizar: ")
    if codigo_actualizar in Inventario:
        nuevo_precio_str = input(f"Ingrese el nuevo precio para {Inventario[codigo_actualizar]['producto']}: ")
        try:
            if int(nuevo_precio_str) < 0:
                print("no se permiten numeros")
                return
            nuevo_precio = int(nuevo_precio_str)
            Inventario[codigo_actualizar]['precio'] = nuevo_precio
            print(f"El precio de {Inventario[codigo_actualizar]['producto']} ha sido actualizado a {nuevo_precio}.")
        except ValueError:
            print("El precio ingresado no es un numero valido.")
    else:
        print("Codigo de producto invalido.")
        
#eliminamos los productos mediante la funcion .pop
def Eliminar_Productos():
    """permite borrar el producto"""
    Eliminar = input("Ingrese el codigo del producto que desea eliminar: ")
    if Eliminar in Inventario:
        Inventario.pop(Eliminar)

# suma el valor total del inventario (precio x cantidad por producto)
def calcular_valor_total():
    """Calcula el valor total del inventario con precio x cantidad."""
    total = sum(map(lambda p: p['precio'] * p['cantidad'], Inventario.values()))
    print(f"\nEl valor total del inventario es: ${total}")

#Autenticacion primeramente, luego dentro de esta funcion llamamos a todas las funciones, para poder interactuar con el inventario, esto lo logramos mediante la invocaccion de estas funciones
if autenticar():
    while True:
        mostrar_inventario()
        opcion = input("Seleccione una opcion: ")

        if opcion == '1':
            mostrar_inventario_completo()
        elif opcion == '2':
            buscar_precio()
        elif opcion == '3':
            buscar_cantidad()
        elif opcion == "4":
            añadir_producto()
        elif opcion == '5':
            actualizar_precio()
        elif opcion == '6':
            Eliminar_Productos()
        elif opcion == '7':
            calcular_valor_total()
        elif opcion == '8':
            print("Saliendo del programa.")#opcion 8 para salir del programa
            break
        else:
            print("Opcion invalida. Por favor, intente de nuevo.")
else:
    print("El programa finalizo debido a un error de autenticacion.")
    
    
# School = {
#     '001': {'name': 'Mateo', 'age': 16, 'grade': 4.5},
#     '002': {'name': 'Luis', 'age': 18, 'grade': 5.0},
#     '003': {'name': 'Albeiro', 'age': 19, 'grade': 2.6},
#     '004': {'name': 'Jose', 'age': 15, 'grade': 2.5},
#     '005': {'name': 'Sebastian', 'age': 14, 'grade': 4.8}
# }

# password = "escuela"

# def display_menu():
#     """Muestra el menú principal del inventario."""
#     print("\nMENU")
#     print("1. Añadir estudiante")
#     print("2. Buscar estudiante por nombre")
#     print("3. Buscar estudiante por id")
#     print("4. Actualizar edad del estudiante")
#     print("5. Actualizar nota del estudiante")
#     print("6. Elinar estudiantes")
#     print("7. Calcular promedio de estudiantes")
#     print("8. Umbral de estudiantes por de bajo de 3.0")
#     print("9. Salir")

# def authenticate():
#     """Autenticacion"""
#     while True:
#         entered_password = input("Ingrese la contraseña de acceso: ")
#         if entered_password == password:
#             print("Autenticación exitosa")
#             return True
#         else:
#             print("Contraseña incorrecta.")

# def add_student():
#     """Permite al usuario ingresar nuevos estudiantes."""
#     new_id = input("Ingrese una ID unica para el estudiante: ")
#     if new_id in School:
#         print("El estudiante ya está registrado")
#     else:

#         new_name = input("Ingrese el nombre del produ: ")
#         new_age = input("Ingrese el precio del producto: ")
#         new_grade = input("Ingrese la cantidad del producto: ")

#         new_students = {
#             new_id: {
#                 'name': new_name,
#                 'age': int(new_age),
#                 'grade': int(new_grade)
#             }
#         }
#         School.update(new_students)
#         print(f"Estudiante con ID: '{new_id}' añadido a la Escula.")

# def search_student_by_name():
#     name = input("ingrese el nombre del estudiante")
#     if School[name]['name'] == name:
#         print(f"El estudiante {name} está en la lista")
#     else:
#         print("El estudiante no está registrado")

# def search_student_by_id():
#     """Permite al usuario ingresar estudiantes a la base de datos."""
#     id_to_search = input("Ingrese el código del producto para ver el precio: ")

#     if id_to_search in School:
#         print(f"Estudiante: {School[id_to_search]['name']}")
#     else:
#         print("No se encontró el estudiante")


# def update_student_age():
#     """Permite actualizar la información del estudiante"""
#     student_to_update = input("ingrese la ID del estudiante que desea actualizar: ")
#     if student_to_update in School:
#         new_age_str = input(f"Ingrese un nueva edad para {School[student_to_update]['name']}: ")
#         try:
#             if int(new_age_str) < 0:
#                 print("no se permiten numeros negativos")
#                 return
#             new_age = int(new_age_str)
#             School[student_to_update]['age'] = new_age
#             print(f"La edad de {School[student_to_update]['name']} ha sido actualizado a {new_age}.")
#         except ValueError:
#             print("La nota ingresada no es un número válido.")
#     else:
#         print("Código de producto inválido.")

# def update_student_grade():
#     """Permite actualizar la información del estudiante"""
#     student_to_update = input("ingrese la ID del estudiante que desea actualizar: ")
#     if student_to_update in School:
#         new_grade_str = input(f"Ingrese un nueva nota para {School[student_to_update]['name']}: ")
#         try:
#             if float(new_grade_str) < 0.0 or float(new_grade_str) > 5.0:
#                 print("No es posible insertar la nota. El rango es entre 0.0 y 5.0")
#                 return
#             new_grade = float(new_grade_str)
#             School[student_to_update]['grade'] = new_grade
#             print(f"La nota de {School[student_to_update]['name']} ha sido actualizado a {new_grade}.")
#         except ValueError:
#             print("La nota ingresada no es un número válido.")
#     else:
#         print("Código de producto inválido.")

# def calculate_average_grade():
#     """Permite calcular el promedio de las notas"""
#     total_grades = 0
#     student_count = 0
#     for student_id, student_info in School.items():
#         if 'grade' in student_info:
#             total_grades += student_info['grade']
#             student_count += 1

#     if student_count > 0:
#         average = total_grades / student_count
#         print(f"El promedio de las notas de los estudiantes es: {average}")
#     else:
#         print("No hay notas para calcular el promedio.")

# def low_grade_threshold():
#     """Muestra la cantidad y nombres de estudiantes con notas por debajo de 3.0."""
#     students_below_threshold = []
#     student_count = 0
#     for student_id, student_info in School.items():
#         if 'grade' in student_info:
#             if student_info['grade'] < 3.0:
#                 students_below_threshold.append(student_info['name'])
#                 student_count += 1

#     if student_count > 0:
#         print(f"\nHay {student_count} estudiantes con notas por debajo de 3.0:")
#         for name in students_below_threshold:
#             print(f"- {name}")
#     else:
#         print("\nNo hay estudiantes con notas por debajo de 3.0.")

# def delete_students():
#     """permite borrar el estudiante"""
#     student_to_delete = input("Ingrese la ID del estudiante que desea Eliminar: ")
#     if student_to_delete in School:
#         confirm = input("El estudiante existe, ¿deseas continuar con la eliminacion (si/no)?: ")
#         if confirm.lower() == "si":
#             School.pop(student_to_delete)
#             print(f"El estudiante con ID {student_to_delete} ha sido eliminado.")
#         elif confirm.lower() == "no":
#             print("La eliminacion ha sido cancelada.")
#         else:
#             print("Respuesta invalida. Por favor, ingresa 'si' o 'no'.")
#     else:
#         print(f"No se encontro ningun estudiante con la ID {student_to_delete}.")


# if authenticate():
#     while True:
#         display_menu()
#         option = input("Seleccione una opción: ")

#         if option == '1':
#             add_student()
#         elif option == '2':
#             search_student_by_name()
#         elif option == '3':
#             search_student_by_id()
#         elif option == '4':
#             update_student_age()
#         elif option == "5":
#             update_student_grade()
#         elif option == '6':
#             delete_students()
#         elif option == '7':
#             calculate_average_grade()
#         elif option == '8':
#             low_grade_threshold()
#         elif option == '9':
#             print("Saliendo del programa.")
#             break
#         else:
#             print("Opción inválida. Por favor, intente de nuevo.")
# else:
#     print("El programa finalizó debido a un error de autenticación.")