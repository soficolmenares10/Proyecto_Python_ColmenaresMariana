def mostrar_menu_trainer():
    """Menú principal para trainers"""
    while True:
        print("===== MENU TRAINER =====")
        print("1. Registrar examen inicial")
        print("2. Registrar evaluación por módulo")
        print("3. Detectar campers en riesgo")
        
        opcion = input("Selecciona una opción (1-3): ").strip()
        
        if opcion == "1":
            registrar_examen_inicial()
        elif opcion == "2":
            registrar_evaluacion_modulo()
        elif opcion == "3":
            detectar_campers_riesgo()
        else:
            print("Opción no válida. Por favor intenta de nuevo.")

def registrar_examen_inicial():
    """Registrar examen inicial de un camper"""
    print("--- Registrar examen inicial ---")
    # TODO: Implementar funcionalidad
    print("Funcionalidad en desarrollo...")

def registrar_evaluacion_modulo():
    """Registrar evaluación por módulo"""
    print("--- Registrar evaluación por módulo ---")
    # Fórmula: nota_final = (teorica * 0.30) + (practica * 0.60) + (quices * 0.10)
    # TODO: Implementar funcionalidad
    print("Funcionalidad en desarrollo...")

def detectar_campers_riesgo():
    """Detectar campers en riesgo académico"""
    print("--- Detectar campers en riesgo ---")
    # TODO: Implementar funcionalidad
    print("Funcionalidad en desarrollo...")

