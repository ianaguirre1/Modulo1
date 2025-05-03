contactos = {
    '001':{'nombre': 'mariana','email': 'mariana56194@gmail.com','telefono': 3126585495},
    '002':{'nombre': 'juan','email': 'juan5456194@gmail.com','telefono': 3165875212},
    '003':{'nombre': 'mateo','email': 'mateo5456194@gmail.com','telefono': 3195468552}
}

nuevos_contactos = {
    '004':{'nombre': 'julian','email': 'julian5456194@gmail.com','telefono': 313468582}
}

contactos.update(nuevos_contactos)
print(contactos)

for i in contactos.values():
    print(i['nombre'])
    
contactos.update({'002':{'nombre': 'santiago'}})
print(contactos['002']['nombre'])

contactos.pop('002')
print(contactos)

codigo = (input("ingresa un codigo"))
nombre1 =(input("ingresa un nombre"))
email1 = (input("ingresa un email"))
telefono1 = (input("ingresa un telefono"))

nuevo_contactos1 = {
    codigo:{
        'nombre': nombre1,
        'email': email1,
        'telefono': telefono1}
}

contactos.update(nuevo_contactos1)

print("\nBiblioteca actualizada: ")
for clave, datos in contactos.items():
    print(f"{clave}: {datos}")




