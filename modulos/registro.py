import json
import os


def cargar_archivo(ruta):
    """Carga un archivo JSON de forma segura"""
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print(f"Archivo no encontrado: {ruta}")
        return []
    except json.JSONDecodeError:
        print(f"Error en el formato JSON: {ruta}")
        return []


def iniciar_sesion():
    print("===== LOGIN =====")

    correo = input("Correo: ").strip()
    contrasena = input("Contraseña: ").strip()

    # 📌 Ruta base del proyecto
    ruta_base = os.path.dirname(os.path.abspath(__file__))

    # 📌 Carpeta jsons (misma estructura que ya tienes)
    ruta_jsons = os.path.join(ruta_base, "../jsons")

    # 📌 Rutas completas
    ruta_coordinadores = os.path.join(ruta_jsons, "coordinadores.json")
    ruta_trainers = os.path.join(ruta_jsons, "trainers.json")

    # 📌 Cargar archivos
    coordinadores = cargar_archivo(ruta_coordinadores)
    trainers = cargar_archivo(ruta_trainers)

    # ---------------- BUSCAR COORDINADOR ----------------
    for user in coordinadores:
        if (
            user.get("correo", "").strip().lower() == correo.lower()
            and user.get("contrasena", "").strip() == contrasena
        ):
            print("Bienvenido Coordinador")
            return "coordinador"

    # ---------------- BUSCAR TRAINER ----------------
    for user in trainers:
        if (
            user.get("correo", "").strip().lower() == correo.lower()
            and user.get("contrasena", "").strip() == contrasena
        ):
            print("Bienvenido Trainer")
            return "trainer"

    # ❌ Si no coincide nada
    print("Correo o contraseña incorrectos")
    return None
