import json
import os

# ===============================
# RUTAS Y ARCHIVO
# ===============================

def obtener_ruta_json():
    ruta_base = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(ruta_base, "jsons", "campers.json")


def cargar_campers():
    try:
        with open(obtener_ruta_json(), "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except:
        return []


def guardar_campers(campers):
    with open(obtener_ruta_json(), "w", encoding="utf-8") as archivo:
        json.dump(campers, archivo, indent=4, ensure_ascii=False)


# ===============================
# MENÚ COORDINADOR
# ===============================

def mostrar_menu_coordinador():

    while True:
        campers = cargar_campers()

        print("\n-----------------------------------------------")
        print("Bienvenido Coordinador ¿Qué deseas hacer?")
        print("1. Agendar estudiantes a evaluación")
        print("2. Ver estudiantes en evaluación")
        print("3. Asignar grupo a estudiantes Activos")
        print("4. Editar estado de estudiantes")
        print("5. Registrar resultado examen ingreso")
        print("6. Asignar ruta y trainer")
        print("7. Lista de calificaciones")
        print("8. Módulo de reportes")
        print("9. Crear Grupo (pendiente)")
        print("10. Salir")
        print("-----------------------------------------------")

        opcion = input("Ingrese el número de la opción: ").strip()

        # =================================================
        # 1. AGENDAR ESTUDIANTE
        # =================================================
        if opcion == "1":
            id_buscar = input("Ingrese el ID del estudiante: ").strip()

            for camper in campers:
                if camper.get("id") == id_buscar:
                    camper["estado"] = "En evaluación"
                    guardar_campers(campers)
                    print("Estudiante agendado correctamente.")
                    break
            else:
                print("Estudiante no encontrado.")

        # =================================================
        # 2. VER EN EVALUACIÓN
        # =================================================
        elif opcion == "2":
            encontrados = False

            for camper in campers:
                if camper.get("estado") == "En evaluación":
                    print(f'{camper.get("id")} - {camper.get("nombre")}')
                    encontrados = True

            if not encontrados:
                print("No hay estudiantes en evaluación.")

        # =================================================
        # 3. ASIGNAR GRUPO
        # =================================================
        elif opcion == "3":
            id_buscar = input("Ingrese el ID del estudiante: ").strip()

            for camper in campers:
                if camper.get("id") == id_buscar:

                    if camper.get("estado") != "Activo":
                        print("El estudiante no está ACTIVO.")
                        break

                    grupo = input("Ingrese nombre del grupo: ")
                    camper["grupo"] = grupo
                    guardar_campers(campers)
                    print("Grupo asignado correctamente.")
                    break
            else:
                print("Estudiante no encontrado.")

        # =================================================
        # 4. EDITAR ESTADO
        # =================================================
        elif opcion == "4":
            id_buscar = input("Ingrese el ID del estudiante: ").strip()

            estados = {
                "1": "Inscrito",
                "2": "En evaluación",
                "3": "Activo",
                "4": "Graduado",
                "5": "Retirado"
            }

            for camper in campers:
                if camper.get("id") == id_buscar:

                    print("1. Inscrito")
                    print("2. En evaluación")
                    print("3. Activo")
                    print("4. Graduado")
                    print("5. Retirado")

                    opcion_estado = input("Seleccione nuevo estado: ")

                    if opcion_estado in estados:
                        camper["estado"] = estados[opcion_estado]
                        guardar_campers(campers)
                        print("Estado actualizado.")
                    else:
                        print("Opción inválida.")
                    break
            else:
                print("Estudiante no encontrado.")

        # =================================================
        # 5. RESULTADO EXAMEN
        # =================================================
        elif opcion == "5":
            id_buscar = input("Ingrese el ID del estudiante: ")

            for camper in campers:
                if camper.get("id") == id_buscar:

                    if camper.get("estado") != "En evaluación":
                        print("El estudiante no está en evaluación.")
                        break

                    try:
                        nota = float(input("Ingrese nota (0-100): "))
                        if nota < 0 or nota > 100:
                            print("La nota debe estar entre 0 y 100.")
                            break
                    except:
                        print("Nota inválida.")
                        break

                    camper["nota_ingreso"] = nota

                    if nota >= 60:
                        camper["estado"] = "Activo"
                        print("Estudiante aprobado.")
                    else:
                        camper["estado"] = "Inscrito"
                        print("Estudiante reprobado.")

                    guardar_campers(campers)
                    break
            else:
                print("Estudiante no encontrado.")

        # =================================================
        # 6. ASIGNAR RUTA Y TRAINER
        # =================================================
        elif opcion == "6":
            id_buscar = input("Ingrese ID del estudiante: ")

            for camper in campers:
                if camper.get("id") == id_buscar:
                    ruta = input("Ingrese nueva ruta: ")
                    trainer = input("Ingrese nombre del trainer: ")

                    camper["ruta_asignada"] = ruta
                    camper["trainer_asignado"] = trainer

                    guardar_campers(campers)
                    print("Ruta y trainer asignados.")
                    break
            else:
                print("Estudiante no encontrado.")

        # =================================================
        # 7. LISTA DE CALIFICACIONES
        # =================================================
        elif opcion == "7":
            print("\n--- Lista de calificaciones ---")

            for camper in campers:
                print(f'\n{camper.get("nombre")}')

                if "calificaciones" in camper:
                    for modulo, nota in camper["calificaciones"].items():
                        print(f"   {modulo}: {nota}")
                else:
                    print("   No tiene calificaciones registradas.")

        # =================================================
        # 8. REPORTES
        # =================================================
        elif opcion == "8":

            while True:
                print("\n--- MÓDULO REPORTES ---")
                print("1. Reporte por estado")
                print("2. Promedio por módulo")
                print("3. Reporte de asistencia")
                print("4. Volver")
                opcion_reportes = input("Seleccione opción: ").strip()

                if opcion_reportes == "1":
                    contador = {}

                    for camper in campers:
                        estado = camper.get("estado", "Sin estado")
                        contador[estado] = contador.get(estado, 0) + 1

                    for estado, cantidad in contador.items():
                        print(f"{estado}: {cantidad}")

                elif opcion_reportes == "2":
                    modulos = {}

                    for camper in campers:
                        if "calificaciones" in camper:
                            for modulo, nota in camper["calificaciones"].items():
                                modulos.setdefault(modulo, []).append(nota)

                    for modulo, notas in modulos.items():
                        promedio = sum(notas) / len(notas)
                        print(f"{modulo} - Promedio: {round(promedio, 2)}")

                elif opcion_reportes == "3":
                    for camper in campers:
                        print(f'{camper.get("nombre")}: {camper.get("asistencia", "Sin dato")}%')

                elif opcion_reportes == "4":
                    break
                else:
                    print("Opción no válida.")

        # =================================================
        # 9. CREAR GRUPO
        # =================================================
        elif opcion == "9":
            print("Función crear grupo pendiente.")

        # =================================================
        # 10. SALIR
        # =================================================
        elif opcion == "10":
            print("Sesión cerrada. ¡Hasta luego!")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    mostrar_menu_coordinador()
