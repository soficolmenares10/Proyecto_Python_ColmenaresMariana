import json
import os


# ===============================
# MENÚ PRINCIPAL TRAINER
# ===============================

def mostrar_menu_trainer():
    while True:
        print("\n===== MENU TRAINER =====")
        print("1. Registrar examen inicial")
        print("2. Registrar evaluación por módulo")
        print("3. Detectar campers en riesgo")
        print("4. Volver al menú anterior")

        opcion = input("Selecciona una opción (1-4): ").strip()

        if opcion == "1":
            registrar_examen_inicial()
        elif opcion == "2":
            registrar_evaluacion_modulo()
        elif opcion == "3":
            detectar_campers_riesgo()
        elif opcion == "4":
            print("Volviendo al menú anterior...")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")


# ===============================
# RUTAS Y ARCHIVOS
# ===============================

def obtener_ruta_json():
    ruta_base = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(ruta_base, "../jsons/campers.json")


def cargar_campers():
    try:
        with open(obtener_ruta_json(), "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print("No se encontró el archivo campers.json")
        return []
    except json.JSONDecodeError:
        print("Error en el formato del JSON.")
        return []


def guardar_campers(campers):
    with open(obtener_ruta_json(), "w", encoding="utf-8") as archivo:
        json.dump(campers, archivo, indent=4, ensure_ascii=False)


# ===============================
# REGISTRAR EXAMEN INICIAL
# ===============================

def registrar_examen_inicial():
    print("\n--- Registrar examen inicial ---")

    campers = cargar_campers()
    id_buscar = input("Ingrese ID del camper: ").strip()

    for camper in campers:
        if camper.get("id") == id_buscar:

            try:
                nota = float(input("Ingrese nota del examen (0-100): "))
                if nota < 0 or nota > 100:
                    print("La nota debe estar entre 0 y 100.")
                    return
            except ValueError:
                print("Nota inválida.")
                return

            camper["nota_ingreso"] = nota

            if nota >= 60:
                camper["estado"] = "Activo"
                print("Camper aprobado y activado.")
            else:
                camper["estado"] = "Inscrito"
                print("Camper no aprobó. Permanece inscrito.")

            guardar_campers(campers)
            return

    print("Camper no encontrado.")


# ===============================
# REGISTRAR EVALUACIÓN POR MÓDULO
# ===============================

def registrar_evaluacion_modulo():
    print("\n--- Registrar evaluación por módulo ---")

    campers = cargar_campers()
    id_buscar = input("Ingrese ID del camper: ").strip()

    for camper in campers:
        if camper.get("id") == id_buscar:

            if camper.get("estado") != "Activo":
                print("El camper no está activo.")
                return

            modulo = input("Nombre del módulo: ").strip()

            try:
                teorica = float(input("Nota teórica (0-100): "))
                practica = float(input("Nota práctica (0-100): "))
                quices = float(input("Nota quices (0-100): "))

                if any(n < 0 or n > 100 for n in [teorica, practica, quices]):
                    print("Todas las notas deben estar entre 0 y 100.")
                    return

            except ValueError:
                print("Notas inválidas.")
                return

            nota_final = (teorica * 0.30) + (practica * 0.60) + (quices * 0.10)

            if "calificaciones" not in camper:
                camper["calificaciones"] = {}

            camper["calificaciones"][modulo] = round(nota_final, 2)

            # Detectar riesgo automático
            camper["riesgo"] = "Alto" if nota_final < 60 else "Bajo"

            guardar_campers(campers)

            print(f"Nota final registrada: {round(nota_final, 2)}")
            print(f"Nivel de riesgo: {camper['riesgo']}")
            return

    print("Camper no encontrado.")


# ===============================
# DETECTAR CAMPERS EN RIESGO
# ===============================

def detectar_campers_riesgo():
    print("\n--- Detectar campers en riesgo ---")

    campers = cargar_campers()
    encontrados = False

    for camper in campers:

        riesgo = "Bajo"

        # Revisar calificaciones
        if "calificaciones" in camper:
            for nota in camper["calificaciones"].values():
                if nota < 60:
                    riesgo = "Alto"

        # Revisar asistencia si existe
        if camper.get("asistencia", 100) < 80:
            riesgo = "Alto"

        camper["riesgo"] = riesgo

        if riesgo == "Alto":
            print(f'{camper.get("nombre", "Camper sin nombre")} está en riesgo.')
            encontrados = True

    guardar_campers(campers)

    if not encontrados:
        print("No hay campers en riesgo.")



