def guardar_campers(campers):
    ruta_base = os.path.dirname(os.path.abspath(__file__))
    ruta_json = os.path.join(ruta_base, "../jsons/campers.json")

    with open(ruta_json, "w", encoding="utf-8") as archivo:
        json.dump(campers, archivo, indent=4)


def mostrar_menu_coordinador():
    """Menú principal para coordinadores"""

    while True:
        campers = cargar_campers()

        print("-----------------------------------------------")
        print("Bienvenido que es lo que quieres hacer?")
        print("1. Agendar estudiantes a evaluacion de ingreso")
        print("2. Estudiantes para evaluacion de ingreso")
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

        # ==============================
        # OPCIÓN 1
        # ==============================
        if opcion == "1":
            print("--- Agendar estudiantes a evaluación ---")
            id_buscar = input("Ingrese el ID del estudiante: ").strip()

            for camper in campers:
                if camper["id"] == id_buscar:
                    camper["estado"] = "En evaluación"
                    guardar_campers(campers)
                    print("Estudiante agendado correctamente.")
                    break
            else:
                print("Estudiante no encontrado.")

        # ==============================
        # OPCIÓN 2
        # ==============================
        elif opcion == "2":
            print("--- Estudiantes en evaluación ---")
            encontrados = False

            for camper in campers:
                if camper["estado"] == "En evaluación":
                    print(f'{camper["id"]} - {camper["nombres"]} {camper["apellidos"]}')
                    encontrados = True

            if not encontrados:
                print("No hay estudiantes en evaluación.")

        # ==============================
        # OPCIÓN 3
        # ==============================
        elif opcion == "3":
            id_buscar = input("Ingrese el ID del estudiante: ").strip()

            for camper in campers:
                if camper["id"] == id_buscar:

                    if camper["estado"] != "Activo":
                        print("El estudiante no está ACTIVO.")
                        break

                    grupo = input("Ingrese nombre del grupo: ")
                    camper["grupo"] = grupo

                    guardar_campers(campers)
                    print("Grupo asignado correctamente.")
                    break
            else:
                print("Estudiante no encontrado.")

        # ==============================
        # OPCIÓN 4
        # ==============================
        elif opcion == "4":
            id_buscar = input("Ingrese el ID del estudiante: ")

            estados = {
                "1": "Inscrito",
                "2": "En evaluación",
                "3": "Activo",
                "4": "Graduado",
                "5": "Retirado"
            }

            for camper in campers:
                if camper["id"] == id_buscar:

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

        # ==============================
        # OPCIÓN 5
        # ==============================
        elif opcion == "5":
            id_buscar = input("Ingrese el ID del estudiante: ")

            for camper in campers:
                if camper["id"] == id_buscar:

                    if camper["estado"] != "En evaluación":
                        print("El estudiante no está en evaluación.")
                        break

                    try:
                        nota = float(input("Ingrese nota (0-100): "))
                    except:
                        print("Nota inválida.")
                        break

                    if nota >= 60:
                        camper["estado"] = "Activo"
                        print("Estudiante aprobado.")
                    else:
                        camper["estado"] = "Inscrito"
                        print("Estudiante reprobado.")

                    camper["nota_ingreso"] = nota
                    guardar_campers(campers)
                    break
            else:
                print("Estudiante no encontrado.")

        # ==============================
        # OPCIÓN 6
        # ==============================
        elif opcion == "6":
            id_buscar = input("Ingrese ID del estudiante: ")

            for camper in campers:
                if camper["id"] == id_buscar:
                    ruta = input("Ingrese nueva ruta: ")
                    trainer = input("Ingrese nombre del trainer: ")

                    camper["ruta_asignada"] = ruta
                    camper["trainer_asignado"] = trainer

                    guardar_campers(campers)
                    print("Ruta y trainer asignados.")
                    break
            else:
                print("Estudiante no encontrado.")

        # ==============================
        # OPCIÓN 7
        # ==============================
        elif opcion == "7":
            print("\n--- Lista de calificaciones ---")

            for camper in campers:
                if "calificaciones" in camper:
                    print(f'{camper["nombres"]} {camper["apellidos"]}')
                    for modulo, nota in camper["calificaciones"].items():
                        print(f"   {modulo}: {nota}")
                else:
                    print(f'{camper["nombres"]} no tiene calificaciones.')

        # ==============================
        # OPCIÓN 8 (REPORTES)
        # ==============================
        elif opcion == "8":

            while True:
                print("-----------------------------------")
                print("1. Reporte de estudiantes por estado")
                print("2. Reporte de calificaciones por módulo")
                print("3. Reporte de asistencia")
                print("4. Volver")
                print("-----------------------------------")

                opcion_reportes = input("Seleccione opción: ").strip()

                if opcion_reportes == "1":
                    contador = {}

                    for camper in campers:
                        estado = camper["estado"] if camper["estado"] else "Sin estado"
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
                        print(f"{modulo} - Promedio: {round(promedio,2)}")

                elif opcion_reportes == "3":
                    for camper in campers:
                        if "asistencia" in camper:
                            print(f'{camper["nombres"]}: {camper["asistencia"]}%')

                elif opcion_reportes == "4":
                    break
                else:
                    print("Opción no válida.")

        # ==============================
        # OPCIÓN 9
        # ==============================
        elif opcion == "9":
            menu_grupos()

        # ==============================
        # OPCIÓN 10
        # ==============================
        elif opcion == "10":
            print("Sesión cerrada. ¡Hasta luego!")
            break

        else:
            print("Opción no válida.")
