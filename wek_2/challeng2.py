lista = list(range(51,101))
lista1 = list(range(0,51))

calificación = int(input("ingresa una calificacion numerica"))

if calificación in lista:
    print("aprovaste")
    
elif calificación in lista1:
    print("no aprovaste")         
entrada = input("ingresa las calificaciones separadas por comas: ejmeplo: 80,65,35: ")
calificaciones = [int(valor.strip())for valor in entrada.split(",")]

promedio = sum(calificaciones) / len(calificaciones)
print("El promedio es:", promedio)

print("Aqui estuve yo, el mejor, Matius")