peso_str = input("Ingrese su peso en kilogramos: ")
altura_str = input("Ingrese su altura en metros: ")
try:
    peso = float(peso_str)
    altura = float(altura_str)

    if peso <= 0 or altura <= 0:
        print("Por favor, ingrese valores positivos para el peso y la altura")
    else:
        imc = peso / altura**2

        print(f"Tu peso es: {peso:.2f} kg")
        print(f"Tu altura es: {altura:.2f} m")
        print(f"Tu índice de masa corporal es: {imc:.2f}")
        if imc < 18.5:
            print("bajo peso")
        elif imc >= 18.5 and imc <= 24.9:
            print("peso normal")
        elif imc >= 25 and imc <= 29.9:
            print("tienes sobrepeso")
        else:
            print ("tienes obesidad")    

except ValueError:
    print("Por favor, ingrese números válidos para el peso y la altura")