def saludar():
    print("hola todos")
    
saludar()
saludar()

####
def saludar(nombre):
    print("hola", nombre)
    
saludar("wenas")

###

def sumar(nombre1):
    print("wenas",nombre1)
    return f"Wenas {nombre1}"

resultado = sumar("nada")
print(resultado)

#####
def variable(num1,num2):
    resultado1 = num1 + num2
    resultado1 = resultado1/3
    return resultado1

llamada = variable(2,2)
print(llamada)

###

def media (num4, num5, num6):
    return (num4 + num5 + num6)/3

llamada1 = media(4,5,6)
print(llamada1)

#####

def resta(num8,num9):
    return (num8 - num9)
print(resta(num8 = 9, num9 = 5))

primero = int(input("ingrese un numero"))
segundo = int(input("ingrese otro numero"))


def sumarnumeros (num1,num2):
    total = num1 + num2
    print(total) 
    
sumarnumeros(primero,segundo)
