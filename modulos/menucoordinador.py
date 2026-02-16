import json
import os
from creargrupos import menu_grupos

def cargar_campers():
    """Cargar datos de campers desde el JSON"""
    ruta_base = os.path.dirname(os.path.abspath(__file__))
    ruta_json = os.path.join(ruta_base, "../jsons/campers.json")
    try:
        with open(ruta_json, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except:
        return []

def mostrar_menu_coordinador():
    """Menú principal para coordinadores"""
    campers = cargar_campers()
    
    while True:
        print("-----------------------------------------------")
        print("Bienvenido que es lo que quieres hacer?")
        print("1. Agendar estudiantes a evaluacion de ingreso")
        print("2. Estudiantes para evalucion de ingreso")
        print("3. Asignar grupos a estudiantes Activos")
        print("4. Editar estado de estudiantes Activos")
        print("5. Resultados de examenes de ingreso")
        print("6. Agregar rutas nuevas a trainer")
        print("7. Lista de calificaciones de los cursos")
        print("8. Modulo de reportes")
        print("9. Crear Grupo")
        print("10. Salir")
        print("-----------------------------------------------")
        
        opcion = input("Ingrese el numero de la opcion que desea: ").strip()
        
        if opcion == "1":
            print("--- Agendar estudiantes a evaluación de ingreso ---")
            # TODO: Implementar funcionalidad
            print("Funcionalidad en desarrollo...")
        elif opcion == "2":
            print("--- Estudiantes para evaluación de ingreso ---")
            # TODO: Implementar funcionalidad
            print("Funcionalidad en desarrollo...")
        elif opcion == "3":
            print("--- Asignar grupos a estudiantes activos ---")
            # TODO: Implementar funcionalidad
            print("Funcionalidad en desarrollo...")
        elif opcion == "4":
            print("--- Editar estado de estudiantes activos ---")
            # TODO: Implementar funcionalidad
            print("Funcionalidad en desarrollo...")
        elif opcion == "5":
            print("--- Resultados de exámenes de ingreso ---")
            # TODO: Implementar funcionalidad
            print("Funcionalidad en desarrollo...")
        elif opcion == "6":
            print("--- Agregar rutas nuevas a trainer ---")
            # TODO: Implementar funcionalidad
            print("Funcionalidad en desarrollo...")
        elif opcion == "7":
            print("--- Lista de calificaciones de los cursos ---")
            # TODO: Implementar funcionalidad
            print("Funcionalidad en desarrollo...")
        elif opcion == "8":
            while True:
                print("-----------------------------------")
                print("1. Reporte de estudiantes por estado")
                print("2. Reporte de calificaciones por módulo")
                print("3. Reporte de asistencia")
                print("4. Volver al menú anterior")
                print("-----------------------------------")
                
                opcion_reportes = input("Ingrese el numero de la opcion que desea: ").strip()
                
                if opcion_reportes == "1":
                    print("--- Reporte de estudiantes por estado ---")
                    # TODO: Implementar funcionalidad
                    print("Funcionalidad en desarrollo...")
                elif opcion_reportes == "2":
                    print("--- Reporte de calificaciones por módulo ---")
                    # TODO: Implementar funcionalidad
                    print("Funcionalidad en desarrollo...")
                elif opcion_reportes == "3":
                    print("--- Reporte de asistencia ---")
                    # TODO: Implementar funcionalidad
                    print("Funcionalidad en desarrollo...")
                elif opcion_reportes == "4":
                    print("Volviendo al menú anterior...")
                    break
                else:
                    print("Opción no válida. Por favor intenta de nuevo.")
        elif opcion == "9":
            menu_grupos()
        elif opcion == "10":
            print("Sesión cerrada. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor intenta de nuevo.")
