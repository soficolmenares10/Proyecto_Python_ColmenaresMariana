import json
import os


# ==============================
# RUTA CORRECTA DEL JSON
# ==============================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUTA_CAMPERS = os.path.join(BASE_DIR, "jsons", "campers.json")


# ==============================
# FUNCIONES DE ARCHIVO
# ==============================

def cargar_campers():
    if not os.path.exists(RUTA_CAMPERS):
        return []
    with open(RUTA_CAMPERS, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def guardar_campers(campers):
    with open(RUTA_CAMPERS, "w", encoding="utf-8") as archivo:
        json.dump(campers, archivo, indent=4, ensure_ascii=False)


# ==============================
# MENÚ PRINCIPAL (RECIBE CAMPER)
# ==============================

def mostrar_menu_camper(camper_actual):
    while True:
        print("===== MENU CAMPER =====")
        print("1. Ver mis datos")
        print("2. Ver mis calificaciones")
        print("3. Ver mi asignación")
        print("4. Ver horario de clases")
        print("5. Subir trabajos")
        print("6. Salir")

        opcion = input("Selecciona una opción (1-6): ").strip()

        if opcion == "1":
            ver_datos_camper(camper_actual)
        elif opcion == "2":
            ver_calificaciones_camper(camper_actual)
        elif opcion == "3":
            ver_asignacion_camper(camper_actual)
        elif opcion == "4":
            ver_horario_clases(camper_actual)
        elif opcion == "5":
            subir_trabajos(camper_actual)
        elif opcion == "6":
            print("Saliendo del menú...")
            break
        else:
            print("Opción no válida.")


# ==============================
# FUNCIONES DEL CAMPER
# ==============================

def ver_datos_camper(camper_actual):
    print("--- Mis datos ---")

    print("Nombre:", camper_actual.get("nombre", "No registrado"))
    print("Correo:", camper_actual.get("correo", "No registrado"))
    print("Estado:", camper_actual.get("estado", "No registrado"))
    print("Riesgo:", camper_actual.get("riesgo", "No registrado"))
    print("Ruta:", camper_actual.get("ruta_asignada", "No asignada"))
    print("Trainer:", camper_actual.get("trainer_asignado", "No asignado"))


def ver_calificaciones_camper(camper_actual):
    print("--- Mis calificaciones ---")

    if camper_actual.get("calificaciones"):
        for modulo, nota in camper_actual["calificaciones"].items():
            print(f"{modulo}: {nota}")
    else:
        print("No tienes calificaciones registradas.")


def ver_asignacion_camper(camper_actual):
    print("--- Mi asignación ---")

    print("Ruta asignada:", camper_actual.get("ruta_asignada", "No asignada"))
    print("Trainer asignado:", camper_actual.get("trainer_asignado", "No asignado"))
    print("Salón asignado:", camper_actual.get("salon_asignado", "No asignado"))


def ver_horario_clases(camper_actual):
    print("--- Mi horario ---")

    if camper_actual.get("salon_asignado"):
        print("Horario: Lunes a Viernes 6:00 AM - 10:00 AM")
    else:
        print("Aún no tienes salón asignado.")


def subir_trabajos(camper_actual):
    print("--- Subir trabajos ---")

    campers = cargar_campers()

    for camper in campers:
        if camper.get("id") == camper_actual.get("id"):

            trabajo = input("Ingrese el nombre del trabajo: ").strip()

            if not trabajo:
                print("Nombre inválido.")
                return

            if "trabajos" not in camper:
                camper["trabajos"] = []

            camper["trabajos"].append(trabajo)

            guardar_campers(campers)

            print("Trabajo subido correctamente.")
            return

    print("No se encontró el camper.")
