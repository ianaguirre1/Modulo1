#  Objetivo del ejercicio:
#  Construir un menú interactivo que permita gestionar una lista de reparaciones:
#  Requisitos:
#  1. El sistema debe mostrar un menú con las siguientes opciones:
#  • 1: Registrar una nueva reparación pendiente (por ejemplo: “cambio de 
# cadena” o “ajuste de frenos”).
#  • 2: Ver todas las reparaciones pendientes.
#  • 3: Marcar una reparación como completada (eliminarla de la lista).
#  • 4: Salir del sistema.
#  2. El sistema debe funcionar en un ciclo continuo hasta que se seleccione la opción de 
# salir.
#  3. Se debe validar si la reparación que se quiere marcar como completada existe en la 
# lista.
#  4. El sistema debe usar una lista para almacenar las reparaciones
reparaciones_c = []
reparacionesp = []

while True:
    print("\n--- MENÚ DE REPARACIONES ---")
    print("1. Registrar nueva reparación")
    print("2. Ver reparaciones pendientes")
    print("3. Marcar reparación como completada")
    print("4. Salir")
    
    opcion = input("Selecciona una opción (1-4): ")

    if opcion == "1":
        nueva = input("Escribe la reparación que deseas registrar: ")
        reparacionesp.append(nueva)
        print("Reparación registrada.")
        
    elif opcion == "2":
        if reparacionesp:
            print("\n--- Reparaciones pendientes ---")
            for i, rep in enumerate(reparacionesp):
                print(f"{i+1}. {rep}")
        else:
            print("No hay reparaciones pendientes.")
    
    elif opcion == "3":
        if reparacionesp:
            print("\n--- Reparaciones pendientes ---")
            for i, rep in enumerate(reparacionesp):
                print(f"{i+1}. {rep}")
            completar = int(input("Selecciona el número de la reparación completada: ")) 
            if 0 <= completar < len(reparacionesp):
                reparaciones_c.append(reparacionesp.pop(completar))  
                print("Reparación marcada como completada.")
            else:
                print("Opción inválida.")
        else:
            print("No hay reparaciones pendientes para completar.")
    
    elif opcion == "4":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida, por favor selecciona entre 1 y 4.")
