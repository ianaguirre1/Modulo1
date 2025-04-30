list = [1,2,3,4,5]
numero = int(input("ingresa numero"))

for i in list :
    if numero in list:
        valid = True
        break
    else:
        valid = False
        break
if valid == False:
    print("no esta en la lista")
else:
    print("esta en la lista")
    
        