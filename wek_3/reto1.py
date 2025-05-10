usuarios = {
    "1234": {"clave": "abc", "saldo": 1000},
    "5678": {"clave": "def", "saldo": 500},
    "9012": {"clave": "ghi", "saldo": 2000}
}


def mostrar_menu():
    """Muestra el menú principal del banco."""
    print("\nBienvenido al Banco")
    print("1. Depositar")
    print("2. Retirar")
    print("3. Consultar saldo")
    print("4. Salir")

for cuenta, clave in usuarios:
    registro = input("ingrese su cuenta")
    if cuenta["1234"] == registro:
        print("usuario 1 ")
        