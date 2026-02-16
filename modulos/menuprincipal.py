import json
from registro import iniciar_sesion
from menucoordinador import mostrar_menu_coordinador
from menutrainers import mostrar_menu_trainer
from menucampers import mostrar_menu_camper

def main():
    rol = iniciar_sesion()

    if rol == "coordinador":
        mostrar_menu_coordinador()
    elif rol == "trainer":
        mostrar_menu_trainer()
    elif rol == "camper":
        mostrar_menu_camper()
    else:
        print("Acceso denegado")

if __name__ == "__main__":
    main()
