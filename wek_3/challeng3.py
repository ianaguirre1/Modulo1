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
