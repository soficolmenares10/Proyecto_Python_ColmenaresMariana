def mostrar_menu_camper():
    """Menú principal para campers"""
    while True:
        print("===== MENU CAMPER =====")
        print("1. Ver mis datos")
        print("2. Ver mis calificaciones")
        print("3. Ver mi asignación de trainer y ruta")
        
        opcion = input("Selecciona una opción (1-3): ").strip()
        
        if opcion == "1":
            ver_datos_camper()
        elif opcion == "2":
            ver_calificaciones_camper()
        elif opcion == "3":
            ver_asignacion_camper()
        else:
            print("Opción no válida. Por favor intenta de nuevo.")

def ver_datos_camper():
    """Ver datos personales del camper"""
    print("--- Mis datos ---")
    # TODO: Implementar funcionalidad
    print("Funcionalidad en desarrollo...")

def ver_calificaciones_camper():
    """Ver calificaciones del camper"""
    print("--- Mis calificaciones ---")
    # TODO: Implementar funcionalidad
    print("Funcionalidad en desarrollo...")

def ver_asignacion_camper():
    """Ver asignación de trainer y ruta"""
    print("--- Mi asignación de trainer y ruta ---")
    # TODO: Implementar funcionalidad
    print("Funcionalidad en desarrollo...")
