numeroSecreto = 7

numero = int(input("adivina el numero"))
if numero > 0:
    if numero > numeroSecreto:
        print("tu numero es mayor que el numero secreto")
    elif numero < numeroSecreto:
        print("numero es menor que el numero secreto")
    else:
        print("adivinaste el numero")
else:print("este numero no es valido")

