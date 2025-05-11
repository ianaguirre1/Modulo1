School = {
    '001': {'name': 'Mateo', 'age': 16, 'grade': 4.5},
    '002': {'name': 'Luis', 'age': 18, 'grade': 5.0},
    '003': {'name': 'Albeiro', 'age': 19, 'grade': 2.6},
    '004': {'name': 'Jose', 'age': 15, 'grade': 2.5},
    '005': {'name': 'Sebastian', 'age': 14, 'grade': 4.8}
}
# 'School' dictionary holds student data.

password = "escuela"
# Password for system access.

def display_menu():
    """Muestra el menú principal del inventario."""
    print("\nMENU")
    print("1. Añadir estudiante")
    print("2. Buscar estudiante por nombre")
    print("3. Buscar estudiante por id")
    print("4. Actualizar edad del estudiante")
    print("5. Actualizar nota del estudiante")
    print("6. Elinar estudiantes")
    print("7. Calcular promedio de estudiantes")
    print("8. Umbral de estudiantes por de bajo de 3.0")
    print("9. Salir")

def authenticate():
    """Autenticacion"""
    while True:
        entered_password = input("Ingrese la contraseña de acceso: ")
        if entered_password == password:
            print("Autenticación exitosa")
            return True # Successful login.
        else:
            print("Contraseña incorrecta.") # Incorrect password.

def add_student():
    """Permite al usuario ingresar nuevos estudiantes."""
    new_id = input("Ingrese una ID unica para el estudiante: ")
    if new_id in School:
        print("El estudiante ya está registrado") # Student already exists.
    else:
        new_name = input("Ingrese el nombre del produ: ")
        new_age = input("Ingrese el precio del producto: ")
        new_grade = input("Ingrese la cantidad del producto: ")

        new_students = {
            new_id: {
                'name': new_name,
                'age': int(new_age),
                'grade': int(new_grade)
            }
        }
        School.update(new_students) # Add new student to School.
        print(f"Estudiante con ID: '{new_id}' añadido a la Escula.") # Confirmation.

def search_student_by_name():
    name = input("ingrese el nombre del estudiante")
    if School[name]['name'] == name:
        print(f"El estudiante {name} está en la lista")
    else:
        print("El estudiante no está registrado")

def search_student_by_id():
    """Permite al usuario ingresar estudiantes a la base de datos."""
    id_to_search = input("Ingrese el código del producto para ver el precio: ")

    if id_to_search in School: # Check if ID exists.
        print(f"Estudiante: {School[id_to_search]['name']}") # Display student name.
    else:
        print("No se encontró el estudiante") # Student not found.

def update_student_age():
    """Permite actualizar la información del estudiante"""
    student_to_update = input("ingrese la ID del estudiante que desea actualizar: ")
    if student_to_update in School:
        new_age_str = input(f"Ingrese un nueva edad para {School[student_to_update]['name']}: ")
        try:
            if int(new_age_str) < 0:
                print("no se permiten numeros negativos") # No negative ages.
                return
            new_age = int(new_age_str)
            School[student_to_update]['age'] = new_age # Update age.
            print(f"La edad de {School[student_to_update]['name']} ha sido actualizado a {new_age}.") # Confirmation.
        except ValueError:
            print("La nota ingresada no es un número válido.") # Invalid age input.
    else:
        print("Código de producto inválido.") # Invalid student ID.

def update_student_grade():
    """Permite actualizar la información del estudiante"""
    student_to_update = input("ingrese la ID del estudiante que desea actualizar: ")
    if student_to_update in School:
        new_grade_str = input(f"Ingrese un nueva nota para {School[student_to_update]['name']}: ")
        try:
            if float(new_grade_str) < 0.0 or float(new_grade_str) > 5.0:
                print("No es posible insertar la nota. El rango es entre 0.0 y 5.0") # Grade range is 0.0 to 5.0.
                return
            new_grade = float(new_grade_str)
            School[student_to_update]['grade'] = new_grade # Update grade.
            print(f"La nota de {School[student_to_update]['name']} ha sido actualizado a {new_grade}.") # Confirmation.
        except ValueError:
            print("La nota ingresada no es un número válido.") # Invalid grade input.
    else:
        print("Código de producto inválido.") # Invalid student ID.

def calculate_average_grade():
    """Permite calcular el promedio de las notas"""
    total_grades = 0
    student_count = 0
    for student_id, student_info in School.items():
        if 'grade' in student_info:
            total_grades += student_info['grade']
            student_count += 1

    if student_count > 0:
        average = total_grades / student_count
        print(f"El promedio de las notas de los estudiantes es: {average}") # Display average grade.
    else:
        print("No hay notas para calcular el promedio.") # No grades to calculate average.

def low_grade_threshold():
    """Muestra la cantidad y nombres de estudiantes con notas por debajo de 3.0."""
    students_below_threshold = []
    student_count = 0
    for student_id, student_info in School.items():
        if 'grade' in student_info:
            if student_info['grade'] < 3.0:
                students_below_threshold.append(student_info['name'])
                student_count += 1

    if student_count > 0:
        print(f"\nHay {student_count} estudiantes con notas por debajo de 3.0:") # Display count of students below threshold.
        for name in students_below_threshold:
            print(f"- {name}") # Display names of students below threshold.
    else:
        print("\nNo hay estudiantes con notas por debajo de 3.0.") # No students below threshold.

def delete_students():
    """permite borrar el estudiante"""
    student_to_delete = input("Ingrese la ID del estudiante que desea Eliminar: ")
    if student_to_delete in School:
        confirm = input("El estudiante existe, ¿deseas continuar con la eliminacion (si/no)?: ")
        if confirm.lower() == "si":
            School.pop(student_to_delete) # Remove the student.
            print(f"El estudiante con ID {student_to_delete} ha sido eliminado.") # Confirmation.
        elif confirm.lower() == "no":
            print("La eliminacion ha sido cancelada.") # Deletion cancelled.
        else:
            print("Respuesta invalida. Por favor, ingresa 'si' o 'no'.") # Invalid confirmation input.
    else:
        print(f"No se encontro ningun estudiante con la ID {student_to_delete}.") # Student ID not found.


if authenticate(): # Start main program if authenticated.
    while True: # Main program loop.
        display_menu() # Show menu.
        option = input("Seleccione una opción: ") # Get user choice.

        if option == '1':
            add_student()
        elif option == '2':
            search_student_by_name()
        elif option == '3':
            search_student_by_id()
        elif option == '4':
            update_student_age()
        elif option == "5":
            update_student_grade()
        elif option == '6':
            delete_students()
        elif option == '7':
            calculate_average_grade()
        elif option == '8':
            low_grade_threshold()
        elif option == '9':
            print("Saliendo del programa.") # Exit program.
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.") # Invalid option.
else:
    print("El programa finalizó debido a un error de autenticación.") # Authentication failed.