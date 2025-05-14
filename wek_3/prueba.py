#create a dictionary of dictionaries
Inventory = {
    '001': {'producto': 'aceite', 'precio': 8000, 'cantidad': 2},
    '002': {'producto': 'arepas', 'precio': 2500, 'cantidad': 2},
    '003': {'producto': 'arroz', 'precio': 3000, 'cantidad': 3},
}

#create a password
password = "inventario"

#show inventory menu
def show_inventory():
    """Muestra el menu principal del inventario."""
    print("\nInventario")
    print("1. Mostrar inventario completo ")
    print("2. Añadir producto")
    print("3. Buscar producto por nombre")
    print("4. Actulizar precio")
    print("5. Borrar productos")
    print("6. Calcular valor total del inventario")
    print("7. Buscar productos por ID")
    print("8. Salir")


#authenticate password
def authenticate():
    """Autenticacion"""
    while True:
        password_entered = input("Ingrese la contrasena de acceso: ")#enter password
        if password_entered == password:
            print("Autenticacion exitosa")
            return True
        else:
            print("Contrasena incorrecta.") 

#show full inventory
def show_full_inventory():
    """Muestra todos los productos en el inventario."""
    print("\n--- Inventario Completo ---")#complete inventory
    for code, product_info in Inventory.items():#We search using a for, one iterable searches for the key, and the other for the value
        print(f"Codigo: {code}")
        for clue, worth in product_info.items():#We search within what was saved in product info
             print(f"  {clue.capitalize()}: {worth}")#we convert the first letter of the key values ​​to uppercase
        print("-" * 20)#lines for each product above and below

#insert product for 5 times maximum
def add_product():
    """Permite al usuario añadir un nuevo producto al inventario."""
    new_code = input("Ingrese un codigo unico para el nuevo producto: ")#we enter data
    product_name = input("Ingrese el nombre del producto: ")
    product_price = input("Ingrese el precio del producto: ")
    product_quantity = input("Ingrese la cantidad del producto: ")
#We create a new dictionary with data
    new_product = {
        new_code: {
            'producto': product_name,
            'precio': int(product_price),
            'cantidad': int(product_quantity)
        }
    }
    Inventory.update(new_product)#
    print(f"Producto con codigo '{new_code}' añadido al inventario.")

    new_code = input("Ingrese un codigo unico para el nuevo producto: ")#we enter data
    product_name = input("Ingrese el nombre del producto: ")
    product_price = input("Ingrese el precio del producto: ")
    product_quantity = input("Ingrese la cantidad del producto: ")
#We create a new dictionary with data
    new_product = {
        new_code: {
            'producto': product_name,
            'precio': int(product_price),
            'cantidad': int(product_quantity)
        }
    }
    Inventory.update(new_product)#
    print(f"Producto con codigo '{new_code}' añadido al inventario.")


    new_code = input("Ingrese un codigo unico para el nuevo producto: ")#we enter data
    product_name = input("Ingrese el nombre del producto: ")
    product_price = input("Ingrese el precio del producto: ")
    product_quantity = input("Ingrese la cantidad del producto: ")
#We create a new dictionary with data
    new_product = {
        new_code: {
            'producto': product_name,
            'precio': int(product_price),
            'cantidad': int(product_quantity)
        }
    }
    Inventory.update(new_product)#
    print(f"Producto con codigo '{new_code}' añadido al inventario.")


    new_code = input("Ingrese un codigo unico para el nuevo producto: ")#we enter data
    product_name = input("Ingrese el nombre del producto: ")
    product_price = input("Ingrese el precio del producto: ")
    product_quantity = input("Ingrese la cantidad del producto: ")
#We create a new dictionary with data
    new_product = {
        new_code: {
            'producto': product_name,
            'precio': int(product_price),
            'cantidad': int(product_quantity)
        }
    }
    Inventory.update(new_product)#
    print(f"Producto con codigo '{new_code}' añadido al inventario.")


    new_code = input("Ingrese un codigo unico para el nuevo producto: ")#we enter data
    product_name = input("Ingrese el nombre del producto: ")
    product_price = input("Ingrese el precio del producto: ")
    product_quantity = input("Ingrese la cantidad del producto: ")
#We create a new dictionary with data
    new_product = {
        new_code: {
            'producto': product_name,
            'precio': int(product_price),
            'cantidad': int(product_quantity)
        }
    }
    Inventory.update(new_product)#
    print(f"Producto con codigo '{new_code}' añadido al inventario.")


#search product by name
def search_product_name(): 

    name = input("ingrese el nombre del producto")#enter name
    if Inventory ['001']['producto'] == name:#if the product is equal to the name
        print(f"El producto {name} está en la lista")     
    else:
        print("El producto no está registrado")

#search product by id
def search_product_by_id():
    """Permite buscar el producto por ID."""
    id_to_search = input("Ingrese el código del producto para ver el precio: ")

    if id_to_search in Inventory: # Check if ID exists.
        print(f"Producto: {Inventory[id_to_search]['producto']} precio: {Inventory[id_to_search]['precio']} cantidad:{Inventory[id_to_search]['cantidad']}") # displays the product name, price, quantity.
    else:
        print("No se encontró el producto") # Product not found.
    

#update product prices
def update_price():
    """Permite al usuario seleccionar un producto y actualizar su precio."""
    code_update = input("Ingrese el codigo del producto cuyo precio desea actualizar: ")
    if code_update in Inventory:
        new_price_str = input(f"Ingrese el nuevo precio para {Inventory[code_update]['producto']}: ")
        try:
            if int(new_price_str) < 0:
                print("no se permiten numeros negativos")
                return
            new_price = int(new_price_str)
            Inventory[code_update]['precio'] = new_price
            print(f"El precio de {Inventory[code_update]['producto']} ha sido actualizado a {new_price}.")
        except ValueError:
            print("El precio ingresado no es un numero valido.")
    else:
        print("Codigo de producto invalido.")


#delete products from inventory
def delete_products():
    """permite borrar productos"""
    product_delete = input("Ingrese la ID del producto que desea Eliminar: ")
    if product_delete in Inventory:
        confirm = input("El producto existe, ¿deseas continuar con la eliminacion (si/no)?: ")
        if confirm.lower() == "si":
            Inventory.pop(product_delete) # Remove the product.
            print(f"El producto con ID {product_delete} ha sido eliminado.") # Confirmation.
        elif confirm.lower() == "no":
            print("La eliminacion ha sido cancelada.") # Deletion cancelled.
        else:
            print("Respuesta invalida. Por favor, ingresa 'si' o 'no'.") # Invalid confirmation input.
    else:
        print(f"No se encontro ningun producto con la ID {product_delete}.") # Product ID not found.


# add the total value of the inventory (price x quantity per product)
def calculate_total_value():
    """Calcula el valor total del inventario con precio x cantidad."""
    total = sum(map(lambda p: p['precio'] * p['cantidad'], Inventory.values()))
    print(f"\nEl valor total del inventario es: ${total:.2f}")

#We initially authenticate with the password, if the password is correct, we show the inventory menu
if authenticate():
    while True:
        show_inventory()
        option = input("Seleccione una opcion: ")

        if option == '1':
            show_full_inventory()
        elif option == '2':
            add_product()
        elif option == '3':
            search_product_name()
        elif option == "4":
            update_price()
        elif option == '5':
            delete_products()
        elif option == '6':
            calculate_total_value()
        elif option == '7':
            search_product_by_id()
        elif option == '8':
            print("Saliendo del programa.")#leaving the program
            break
        else:
            print("Opcion invalida. Por favor, intente de nuevo.")
else:
    print("El programa finalizo debido a un error de autenticacion.")