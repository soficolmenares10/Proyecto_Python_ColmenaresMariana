import json

def cargar_campers():
    with open("campers.json", "r", encoding="utf-8") as archivo:
        return json.load(archivo)
def guardar_campers(campers):
    with open("campers.json", "w", encoding="utf-8") as archivo:
        json.dump(campers, archivo, indent=4)
camper_actual = "1"

def mostrar_menu_camper():
    """Menú principal para campers"""
    while True:
        print("===== MENU CAMPER =====")
        print("1. Ver mis datos")
        print("2. Ver mis calificaciones")
        print("3. Ver mi asignación de trainer y ruta")
        print("4. Ver horario de clases")
        print("5.Subir trabajos")
        print("6. Salir")   
        opcion = input("Selecciona una opción (1-6): ").strip()
        
        if opcion == "1":
            ver_datos_camper()
        elif opcion == "2":
            ver_calificaciones_camper()
        elif opcion == "3":
            ver_asignacion_camper()
        elif opcion == "4":
            ver_horario_clases()
        elif opcion == "5":
            subir_trabajos()
        elif opcion == "6": 
            print("Saliendo del menú...")
        else:
            print("Opción no válida. Por favor intenta de nuevo.")

def ver_datos_camper():
    print("\n--- Mis datos ---")
    campers = cargar_campers()    
    for camper in campers:
            if camper["id"] == camper_actual:
                    print("Nombre:", camper["nombres"], camper["apellidos"])
                    print("Dirección:", camper["direccion"])
                    print("Acudiente:", camper["acudiente"])
                    print("Teléfono celular:", camper["telefono_celular"])
                    print("Teléfono fijo:", camper["telefono_fijo"])
                    print("Correo:", camper["correo"])
                    print("Estado:", camper["estado"])
                    print("Riesgo:", camper["riesgo"])
    return
        
    print("Camper no encontrado.")

 
def ver_calificaciones_camper():
    print("\n--- Mis calificaciones ---")
    campers = cargar_campers()
    for camper in campers:
        if camper["id"] == camper_actual:
            if "calificaciones" in camper and camper["calificaciones"]:
                for modulo, nota in camper["calificaciones"].items():
                    print(f"{modulo}: {nota}")
            else:
                print("No tienes calificaciones registradas.")
            return
    print("Camper no encontrado.")

def ver_asignacion_camper():
    print("\n--- Mi asignación de trainer y ruta ---")
    campers = cargar_campers()
    for camper in campers:
        if camper["id"] == camper_actual:
            print("Ruta asignada:", camper["ruta_asignada"])
            print("Trainer asignado:", camper["trainer_asignado"])
            print("Salón asignado:", camper["salon_asignado"])
            return

print("Camper no encontrado.")

def ver_horario_clases():
    print("\n--- Mi horario de clases ---")
    campers = cargar_campers()
    for camper in campers:
        if camper["id"] == camper_actual:
            
            if camper["salon_asignado"]:
                print("Horario: Lunes a Viernes 6:00 AM - 10:00 AM")
            else:
                print("Aún no tienes salón asignado.")
            return
    print("Camper no encontrado.")

def subir_trabajos():
        print("\n--- Subir trabajos ---")       
        def subir_trabajos():
             print("\n--- Subir trabajos ---")
        campers = cargar_campers()
        for camper in campers:
            if camper["id"] == camper_actual:
         
                trabajo = input("Ingrese el nombre del trabajo: ")
            
            if "trabajos" not in camper:
                camper["trabajos"] = []
            
            camper["trabajos"].append(trabajo)
            
            guardar_campers(campers)
            
            print("Trabajo subido correctamente.")
            return
print("Camper no encontrado.")



