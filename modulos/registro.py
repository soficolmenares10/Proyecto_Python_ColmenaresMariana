import json
import os

def cargar_archivo(ruta):
    with open(ruta, "r", encoding="utf-8") as archivo:
        return json.load(archivo)

def iniciar_sesion():
    print("===== LOGIN =====")

    correo = input("Correo: ")
    contrasena = input("Contraseña: ")

    # Obtener la ruta del directorio actual del archivo
    ruta_base = os.path.dirname(os.path.abspath(__file__))
    ruta_jsons = os.path.join(ruta_base, "../jsons")
    
    coordinadores = cargar_archivo(os.path.join(ruta_jsons, "coordinadores.json"))
    trainers = cargar_archivo(os.path.join(ruta_jsons, "trainers.json"))
    campers = cargar_archivo(os.path.join(ruta_jsons, "campers.json"))

    # Buscar en coordinadores
    for user in coordinadores:
        if user.get("correo") == correo and user.get("contrasena") == contrasena:
            print("Bienvenido Coordinador")
            return "coordinador"

    # Buscar en trainers
    for user in trainers:
        if user.get("correo") == correo and user.get("contrasena") == contrasena:
            print("Bienvenido Trainer")
            return "trainer"

    # Buscar en campers
    for user in campers:
        if user.get("correo") == correo and user.get("contrasena") == contrasena:
            print("Bienvenido Camper")
            return "camper"

    print("Correo o contraseña incorrectos")
    return None

