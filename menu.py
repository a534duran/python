# Lista para almacenar las notas (puedes usar números enteros o decimales)
notas = []
opcion = None # Inicializamos la variable para la opción

# Función para mostrar el menú
def mostrar_menu():
    """Muestra las opciones del menú principal."""
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Agregar una nota")
    print("2. Mostrar todas las notas")
    print("3. Calcular promedio, mayor y menor")
    print("4. Terminar programa")
    
# Simulación del bucle do-while
while True:
    mostrar_menu()
    
    # Solicitar la opción al usuario
    try:
        opcion = int(input("Seleccione una opción (1-4): "))
    except ValueError:
        print("🛑 ¡Opción inválida! Por favor, ingrese un número del 1 al 4.")
        continue # Vuelve al inicio del bucle
        
    # Lógica del menú
    if opcion == 1:
        # --- Agregar una nota ---
        try:
            nota = float(input("Ingrese la nota a agregar: "))
            notas.append(nota)
            print(f"✅ Nota {nota} agregada correctamente.")
        except ValueError:
            print("🛑 ¡Entrada inválida! Debe ingresar un número para la nota.")
            
    elif opcion == 2:
        # --- Mostrar todas las notas ---
        if notas:
            print("\n--- LISTA DE NOTAS ---")
            for i, nota in enumerate(notas):
                print(f"Nota #{i+1}: {nota}")
        else:
            print("ℹ️ Aún no hay notas registradas.")
            
    elif opcion == 3:
        # --- Calcular promedio, mayor y menor ---
        if notas:
            promedio = sum(notas) / len(notas)
            mayor = max(notas)
            menor = min(notas)
            print("\n--- RESULTADOS ---")
            print(f"📊 Promedio de notas: {promedio:.2f}")
            print(f"⭐ Nota más alta: {mayor}")
            print(f"⬇️  Nota más baja: {menor}")
        else:
            print("ℹ️ Necesita agregar notas para realizar cálculos.")
            
    elif opcion == 4:
        # --- Terminar programa ---
        print("👋 Terminando programa. ¡Hasta pronto!")
        break # Sale del bucle while True, finalizando la ejecución
        
    else:
        # Opción fuera del rango (1-4)
        print("❌ Opción no reconocida. Seleccione un número entre 1 y 4.")
