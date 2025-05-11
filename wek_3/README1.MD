## Estructura del Código y Propósito de Cada Función

El código está estructurado con un diccionario principal `School` para almacenar la información de los estudiantes. Los datos de cada estudiante se almacenan como un diccionario con las claves 'name', 'age' y 'grade'.

Aquí tienes una breve explicación de cada función:

* `display_menu()`: Imprime las opciones del menú principal al usuario
* `authenticate()`: Maneja el inicio de sesión del usuario solicitando una contraseña y verificándola con la `password` almacenada
* `add_student()`: Permite al usuario ingresar información para un nuevo estudiante y lo añade al diccionario `School`
* `search_student_by_name()`: Solicita al usuario el nombre de un estudiante y busca un estudiante con ese nombre exacto en el diccionario `School`.
* `search_student_by_id()`: Solicita al usuario el ID de un estudiante y muestra el nombre del estudiante con ese ID
* `update_student_age()`: Permite al usuario actualizar la edad de un estudiante existente proporcionando su ID. Incluye una validación básica para evitar edades negativas
* `update_student_grade()`: Permite al usuario actualizar la nota de un estudiante existente proporcionando su ID. Incluye validación para notas fuera del rango válido (0.0 - 5.0)
* `calculate_average_grade()`: Calcula y muestra el promedio de las notas de todos los estudiantes en el diccionario `School`
* `low_grade_threshold()`: Identifica y muestra la cantidad y los nombres de los estudiantes con notas por debajo de 3.0
* `delete_students()`: Permite al usuario eliminar un estudiante del diccionario `School` proporcionando su ID, con un paso de confirmación

La parte principal del script primero llama a la función `authenticate()`. Si la autenticación es exitosa, entra en un bucle que muestra el menú y ejecuta la función elegida según la entrada del usuario. El bucle continúa hasta que el usuario selecciona la opción 'Salir'