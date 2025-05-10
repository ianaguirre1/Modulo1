usuarios = {
    "1234": {"clave": "abc", "saldo": 1000}, #creamos una listado, de cuentas y claves de acceso
    "5678": {"clave": "def", "saldo": 500},
    "9012": {"clave": "ghi", "saldo": 2000}
}

def mostrar_menu(): #creamos una funcion que me muestre el menu
    """Muestra el menú principal del banco."""
    print("\nBienvenido al Banco")
    print("1. Depositar")
    print("2. Retirar")
    print("3. Consultar saldo")
    print("4. Salir")

def autenticar_usuario():
    """Permite al usuario ingresar su número de cuenta y clave para acceder."""
    while True:
        numero_cuenta = input("Ingrese su número de cuenta: ") #ingresamos un numero de cuenta
        clave = input("Ingrese su clave: ") #ingresamos un clave
        if numero_cuenta in usuarios and usuarios[numero_cuenta]["clave"] == clave: # si numero_cuenta está en usuarios y buscamos en usuarios la clave "clave" si es igual a la clave que ingresamos 
            print("Autenticación exitosa.") #autenticación exitosa
            return numero_cuenta #retornamos el numero de cuenta  ##
        else:
            print("Número de cuenta o clave incorrectos. Intente de nuevo.")


def depositar(numero_cuenta): #traemos lo que reotornsmaos de numero de cuenta 
    """Permite al usuario depositar dinero en su cuenta."""
    try:
        monto = float(input("Ingrese el monto a depositar: ")) #creamos una variable monto 
        if monto > 0:
            usuarios[numero_cuenta]["saldo"] += monto # buscamos en usuarios deacuerdo con numero de cuenta, especificamente en "saldo" y el monto se le suma a saldo
            print(f"Se depositaron ${monto} en su cuenta.") # muestra lo que depositamos
            print(f"Su nuevo saldo es: ${usuarios[numero_cuenta]['saldo']:.2f}") #
        else:
            print("El monto a depositar debe ser mayor que cero.")
    except ValueError:
        print("Error: Por favor, ingrese un monto válido.")

def retirar(numero_cuenta):
    """Permite al usuario retirar dinero de su cuenta."""
    try:
        monto = float(input("Ingrese el monto a retirar: "))
        if monto > 0:
            if monto <= usuarios[numero_cuenta]["saldo"]:
                usuarios[numero_cuenta]["saldo"] -= monto
                print(f"Se retiraron ${monto} de su cuenta.")
                print(f"Su nuevo saldo es: ${usuarios[numero_cuenta]['saldo']:.2f}")
            else:
                print("Fondos insuficientes.")
        else:
            print("El monto a retirar debe ser mayor que cero.")
    except ValueError:
        print("Error: Por favor, ingrese un monto válido.")

def consultar_saldo(numero_cuenta):
    """Muestra el saldo actual del usuario."""
    saldo = usuarios[numero_cuenta]["saldo"]
    print(f"Su saldo actual es: ${saldo:.2f}")

def main():
    """Función principal que controla el flujo del programa."""
    print("Bienvenido al Sistema Bancario.")
    numero_cuenta_usuario = autenticar_usuario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        try:
            opcion = int(opcion)
            if opcion == 1:
                depositar(numero_cuenta_usuario)
            elif opcion == 2:
                retirar(numero_cuenta_usuario)
            elif opcion == 3:
                consultar_saldo(numero_cuenta_usuario)
            elif opcion == 4:
                print("Gracias por usar nuestro banco. ¡Hasta luego!")
                # En lugar de sys.exit(), usamos break para salir del bucle
                break
            else:
                print("Opción inválida. Por favor, seleccione una opción del menú.")
        except ValueError:
            print("Error: Por favor, ingrese un número como opción.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    main()

print("El programa ha finalizado.")