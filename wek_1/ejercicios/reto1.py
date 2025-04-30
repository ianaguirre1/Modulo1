lista = list(range(0,11))     
lista1 = list(range(0,21,2))   
lista2 = list(range(0,31,3))   
lista3 = list(range(0,41,4))   
lista4 = list(range(0,51,5))   
lista5 = list(range(0,61,6))   
lista6 = list(range(0,71,7))   
lista7 = list(range(0,81,8))   
lista8 = list(range(0,91,9))
lista9 = list(range(0,101,10))   
tablas = []  
for i in range(11):
    elemento = [lista[i], lista1[i], lista2[i], lista3[i], lista4[i],lista5[i], lista6[i], lista7[i], lista8[i], lista9[i]]
    tablas.append(elemento)
for fila in tablas:
    print(fila)
        

        
    
