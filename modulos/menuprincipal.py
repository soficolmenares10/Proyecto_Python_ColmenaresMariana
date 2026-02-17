from registro import iniciar_sesion
from menucoordinador import mostrar_menu_coordinador
from menutrainers import mostrar_menu_trainer
from menucampers import mostrar_menu_camper
import json


def buscar_camper_por_id(id_camper):
    try:
        with open("campers.json", "r", encoding="utf-8") as archivo:
            campers = json.load(archivo)

        for camper in campers:
            if camper["id"] == id_camper:
                return camper

        return None

    except FileNotFoundError:
        print("Archivo campers.json no encontrado.")
        return None


def main():
    try:
        print("===== SISTEMA CAMPUSLANDS =====")
        print("1. Coordinador")
        print("2. Trainer")
        print("3. Camper")

        opcion = input("Seleccione su rol: ")

        # ---------------- COORDINADOR ----------------
        if opcion == "1":
            rol = iniciar_sesion()
            if rol and rol.lower() == "coordinador":
                mostrar_menu_coordinador()
            else:
                print("Credenciales incorrectas.")

        # ---------------- TRAINER ----------------
        elif opcion == "2":
            rol = iniciar_sesion()
            if rol and rol.lower() == "trainer":
                mostrar_menu_trainer()
            else:
                print("Credenciales incorrectas.")

        # ---------------- CAMPER ----------------
        elif opcion == "3":
            print("===== INGRESO CAMPER =====")
            id_camper = input("Ingrese su ID: ")

            camper = buscar_camper_por_id(id_camper)

            if camper:
                mostrar_menu_camper(camper)
            else:
                print("ID no encontrado.")

        else:
            print("Opción inválida.")

    except Exception as e:
        print("Ocurrió un error:", e)


if __name__ == "__main__":
    main()

