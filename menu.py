# Lista para almacenar las notas (puedes usar números enteros o decimales)
notas = []
# Inicializamos la variable que guardará la opción elegida por el usuario
opcion = None 

# Definición de una función para mostrar el menú
def mostrar_menu():
    """Muestra las opciones del menú principal."""
    # Imprime una línea de separación y el título
    print("\n--- MENÚ PRINCIPAL ---")
    # Imprime las opciones disponibles
    print("1. Agregar una nota")
    print("2. Mostrar todas las notas")
    print("3. Calcular promedio, mayor y menor")
    print("4. Terminar programa")
    
# Simulación del bucle do-while en Python:
# El bucle 'while True' crea un ciclo infinito que se ejecuta al menos una vez.
# La única forma de salir será con un 'break' (opción 4).
while True:
    # Llama a la función para mostrar las opciones del menú
    mostrar_menu()
    
    # Bloque para manejar la entrada del usuario y posibles errores
    try:
        # Solicita al usuario que ingrese la opción y la convierte a entero
        opcion = int(input("Seleccione una opción (1-4): "))
    # Si la entrada no puede convertirse a entero (ej: el usuario escribe "hola")
    except ValueError:
        # Imprime un mensaje de error y usa 'continue'
        print("🛑 ¡Opción inválida! Por favor, ingrese un número del 1 al 4.")
        # 'continue' salta el resto del código del bucle y vuelve a la línea 'while True'
        continue 
        
    # Estructura condicional (if/elif/else) para ejecutar la acción según la opción
    if opcion == 1:
        # --- Lógica para Agregar una nota ---
        try:
            # Pide la nota y la convierte a número decimal (float)
            nota = float(input("Ingrese la nota a agregar: "))
            # Agrega la nota a la lista 'notas'
            notas.append(nota)
            # Confirma la acción
            print(f"✅ Nota {nota} agregada correctamente.")
        except ValueError:
            # Maneja el error si el usuario no ingresa un número para la nota
            print("🛑 ¡Entrada inválida! Debe ingresar un número para la nota.")
            
    elif opcion == 2:
        # --- Lógica para Mostrar todas las notas ---
        # Verifica si la lista 'notas' tiene elementos
        if notas:
            print("\n--- LISTA DE NOTAS ---")
            # Itera sobre la lista para mostrar cada nota con su índice
            for i, nota in enumerate(notas):
                # Imprime el número de nota (i+1) y su valor
                print(f"Nota #{i+1}: {nota}")
        else:
            # Mensaje si la lista está vacía
            print("ℹ️ Aún no hay notas registradas.")
            
    elif opcion == 3:
        # --- Lógica para Calcular promedio, mayor y menor ---
        # Verifica si hay notas para evitar la división por cero o errores en max/min
        if notas:
            # Calcula el promedio: suma de todos los elementos dividido por la cantidad de elementos
            promedio = sum(notas) / len(notas)
            # Encuentra la nota más alta usando la función max()
            mayor = max(notas)
            # Encuentra la nota más baja usando la función min()
            menor = min(notas)
            
            print("\n--- RESULTADOS ---")
            # Imprime los resultados. :.2f formatea el promedio a dos decimales
            print(f"📊 Promedio de notas: {promedio:.2f}")
            print(f"⭐ Nota más alta: {mayor}")
            print(f"⬇️  Nota más baja: {menor}")
        else:
            # Mensaje si la lista está vacía
            print("ℹ️ Necesita agregar notas para realizar cálculos.")
            
    elif opcion == 4:
        # --- Terminar programa ---
        print("👋 Terminando programa. ¡Hasta pronto!")
        # 'break' sale inmediatamente del bucle 'while True' y termina el programa
        break 
        
    else:
        # Mensaje para opciones numéricas fuera del rango (1-4)
        print("❌ Opción no reconocida. Seleccione un número entre 1 y 4.")
