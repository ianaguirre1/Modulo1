Inventario = {
    '001': {'producto': 'aceite', 'precio': 8000, 'cantidad': 50},
    '002': {'producto': 'arepas', 'precio': 2500, 'cantidad': 40},
    '003': {'producto': 'arroz', 'precio': 3000, 'cantidad': 35},
}

Contra = "skalibut"

def mostrar_inventario():
    """Muestra el menú principal del inventario."""
    print("\nInventario")
    print("1. Mostrar inventario completo")
    print("2. Buscar precio de producto")
    print("3. Buscar cantidad de producto")
    print("4. Ingresar productos")
    print("5. Actualizar precio de producto")
    print("6. Eliminar productos")
    print("7. Salir")

def autenticar():
    """Autenticacion"""
    while True:
        contraseña_ingresada = input("Ingrese la contraseña de acceso: ")
        if contraseña_ingresada == Contra:
            print("Autenticación exitosa")
            return True
        else:
            print("Contraseña incorrecta.")

def mostrar_inventario_completo():
    """Muestra todos los productos en el inventario."""
    print("\n--- Inventario Completo ---")
    for codigo, producto_info in Inventario.items():
        print(f"Código: {codigo}")
        for clave, valor in producto_info.items():
            print(f"  {clave.capitalize()}: {valor}")
        print("-" * 20)

def buscar_precio():
    """Permite al usuario buscar el precio de un producto."""
    codigo_producto = input("Ingrese el código del producto para ver el precio: ")
    if codigo_producto in Inventario:
        print(f"El precio de {Inventario[codigo_producto]['producto']} es: {Inventario[codigo_producto]['precio']}")
    else:
        print("Código de producto inválido.")

def buscar_cantidad():
    """Permite al usuario buscar la cantidad de un producto."""
    codigo_producto = input("Ingrese el código del producto para ver la cantidad: ")
    if codigo_producto in Inventario:
        print(f"La cantidad de {Inventario[codigo_producto]['producto']} es: {Inventario[codigo_producto]['cantidad']}")
    else:
        print("Código de producto inválido.")

def añadir_producto():
    """Permite al usuario añadir un nuevo producto al inventario."""
    codigo_nuevo = input("Ingrese un código único para el nuevo producto: ")
    nombre_producto = input("Ingrese el nombre del producto: ")
    precio_producto = input("Ingrese el precio del producto: ")
    cantidad_producto = input("Ingrese la cantidad del producto: ")

    nuevo_producto = {
        codigo_nuevo: {
            'producto': nombre_producto,
            'precio': int(precio_producto),
            'cantidad': int(cantidad_producto)
        }
    }
    Inventario.update(nuevo_producto)
    print(f"Producto con código '{codigo_nuevo}' añadido al inventario.")

def actualizar_precio():
    """Permite al usuario seleccionar un producto y actualizar su precio."""
    codigo_actualizar = input("Ingrese el código del producto cuyo precio desea actualizar: ")
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
            print("El precio ingresado no es un número válido.")
    else:
        print("Código de producto inválido.")
        
def Eliminar_Productos():
    """permite borrar el producto"""
    Eliminar= input("Ingrese la ID del estudiante que desea Eliminar: ")
    if Eliminar in Inventario:
        Inventario.pop(Eliminar)

if autenticar():
    while True:
        mostrar_inventario()
        opcion = input("Seleccione una opción: ")

        if opcion == '8':
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
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")
else:
    print("El programa finalizó debido a un error de autenticación.")