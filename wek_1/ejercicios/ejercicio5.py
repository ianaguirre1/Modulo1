cuenta = 875
propina = 0
print(f"tu valor a pagar es: {cuenta}")
valores = [10,15,20]
porcentaje =int(input(f"que porcentaje de propina quieres dejar? {valores}:"))

if porcentaje in valores:
    propina = cuenta * porcentaje / 100
    print(f"tu propina a pagra es: {propina:.0f}")
else:
    print("valor no valido")
    
total = propina + cuenta
print(f"tu valor total a pagar es: {total}")
