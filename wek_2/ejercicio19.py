Inventario = {
    '001':{'Producto': 'Arroz', 'Precio:': 3000, 'cantidad': 15},
    '002':{'Producto': 'Arepas', 'Precio:': 4500, 'cantidad': 13},
    '003':{'Producto': 'Leche', 'Precio:': 2000, 'cantidad': 9},
}

Contraseña = "skalibut"

def mostrar_inventario():
    """Muestrab el menu principal del inventario"""
    print("\nMenu de inventario")
    print("1. Mostrar inventario completo")
    print("2. Buscar precio de producto")
    print("3. Buscar cantidad de producto")
    print("4 .Ingresar Productos")
    print("5. Salir")
    
def Autenticar():
    while True:
        contraseña_Ingresada = input("Ingrese su contraseña de acceso")
        if contraseña_Ingresada == Contraseña:
            print("Autenticacion exitosa")
            return True
        else:
            print("Contraseña incorrecta")
            
def Mostrar_inventario_completo():
    """Muestra todos los productos del inventario"""
    for codigo, producto_info in Inventario.items():
        print(f"Codigo:{codigo}")
        for clave, valor in producto_info.items():
            print(f"   {clave.capitalize()}: {valor}")
        print("-"*20)

def Buscar_precio():
    """Permite al usuario buscar el precio de un producto"""
    codigo_producto = input("Ingrese el codigo del producto para ver el precio: ")
    if codigo_producto in Inventario:
        print(f"El precio de {Inventario[codigo_producto]['producto']} es: {Inventario[codigo_producto]['precio']}")
    else:
        print("Codigo de producto invalido")

def Buscar_cantidad():
    """Permite al usuario buscar la cantidad de un producto"""
    codigo_producto = input("Ingrese el codigo del producto para ver la cantidad: ")
    if codigo_producto in Inventario:
        print(f"La cantidad de {Inventario[codigo_producto]['producto']} es {Inventario[codigo_producto]['cantidad']}")
    else:
        print("Codigo de producto invalido")

def Ingresar_productos():
    codigo_nuevo = input("ingrese un nuevo codigo")
    producto = input("ingrese un nuevo producto")
    precio = input("ingrese un precio")
    cantidad = input("ingrese la cantidad")

    Inventario_nuevo = {
    codigo_nuevo:{
        'producto': producto,
        'precio': int(precio),
        'cantidad': int(cantidad)
        }
    }
    Inventario.update(Inventario_nuevo)
    
    print(f"Producto con codigo: '{codigo_nuevo}' añadido al inventario")
    
