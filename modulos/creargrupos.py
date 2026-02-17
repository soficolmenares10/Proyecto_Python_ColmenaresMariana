import json
import os

# ==============================
# CONFIGURACIÓN DE RUTA CORRECTA
# ==============================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, "jsons", "grupos.json")


# ==============================
# FUNCIONES DE ARCHIVO
# ==============================

def cargar_grupos():
    """Cargar grupos desde JSON"""
    try:
        print("Ruta del JSON:", JSON_PATH)  # Puedes quitar esto luego
        with open(JSON_PATH, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print(" El archivo grupos.json no existe en la ruta indicada.")
        return []
    except json.JSONDecodeError:
        print(" Error: El archivo JSON está mal formado.")
        return []
    except Exception as e:
        print(f" Error inesperado: {e}")
        return []


def guardar_grupos(grupos):
    """Guardar grupos en JSON"""
    try:
        with open(JSON_PATH, "w", encoding="utf-8") as archivo:
            json.dump(grupos, archivo, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f" Error al guardar grupos: {e}")
        return False


def obtener_proximo_id(grupos):
    """Obtener siguiente ID disponible"""
    if not grupos:
        return "1"

    try:
        ids = [int(grupo["id"]) for grupo in grupos]
        return str(max(ids) + 1)
    except:
        return "1"


# ==============================
# MENÚ PRINCIPAL
# ==============================

    def menu_grupos():
     while True:
        print("\n===== MENÚ GESTIÓN DE GRUPOS =====")
        print("1. Crear grupo")
        print("2. Listar grupos")
        print("3. Editar grupo")
        print("4. Eliminar grupo")
        print("5. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            crear_grupo()
        elif opcion == "2":
            listar_grupos()
        elif opcion == "3":
            editar_grupo()
        elif opcion == "4":
            eliminar_grupo()
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print(" Opción no válida")


# ==============================
# FUNCIONES CRUD
# ==============================

    def crear_grupo():
        grupos = cargar_grupos()

    print("\n--- Crear Nuevo Grupo ---")

    nombre = input("Nombre del grupo: ").strip()
    ruta = input("Ruta (JAVA, NodeJS, NETCORE, etc): ").strip()
    trainer = input("Trainer: ").strip()
    salon = input("Salón: ").strip()
    fecha_inicio = input("Fecha inicio (YYYY-MM-DD): ").strip()
    fecha_fin = input("Fecha fin (YYYY-MM-DD): ").strip()

    if not nombre:
        print(" El nombre es obligatorio.")
        return

    nuevo_id = obtener_proximo_id(grupos)

    nuevo_grupo = {
        "id": nuevo_id,
        "nombre": nombre,
        "ruta": ruta,
        "trainer": trainer,
        "salon": salon,
        "fecha_inicio": fecha_inicio,
        "fecha_fin": fecha_fin,
        "estado": "Activo",
        "campers": []
    }

    grupos.append(nuevo_grupo)

    if guardar_grupos(grupos):
        print(f"Grupo creado con ID {nuevo_id}")
    else:
        print(" Error al guardar el grupo")


    def listar_grupos():
        grupos = cargar_grupos()

    if not grupos:
        print("No hay grupos registrados.")
        return

    print("\n===== LISTA DE GRUPOS =====")

    for grupo in grupos:
        print("-" * 60)
        print(f"ID: {grupo['id']}")
        print(f"Nombre: {grupo['nombre']}")
        print(f"Ruta: {grupo['ruta']}")
        print(f"Trainer: {grupo['trainer']}")
        print(f"Salón: {grupo['salon']}")
        print(f"Inicio: {grupo['fecha_inicio']}")
        print(f"Fin: {grupo['fecha_fin']}")
        print(f"Estado: {grupo['estado']}")
        print(f"Campers: {len(grupo['campers'])}")
    print("-" * 60)


    def editar_grupo():
        grupos = cargar_grupos()

    if not grupos:
        print("No hay grupos para editar.")
        return

    listar_grupos()

    id_grupo = input("ID del grupo a editar: ").strip()

    grupo = next((g for g in grupos if g["id"] == id_grupo), None)

    if not grupo:
        print(" Grupo no encontrado.")
        return

    print("Deje en blanco para no modificar.")

    nombre = input(f"Nombre ({grupo['nombre']}): ").strip()
    ruta = input(f"Ruta ({grupo['ruta']}): ").strip()
    trainer = input(f"Trainer ({grupo['trainer']}): ").strip()
    salon = input(f"Salón ({grupo['salon']}): ").strip()

    if nombre:
        grupo["nombre"] = nombre
    if ruta:
        grupo["ruta"] = ruta
    if trainer:
        grupo["trainer"] = trainer
    if salon:
        grupo["salon"] = salon

    if guardar_grupos(grupos):
        print("Grupo actualizado correctamente")
    else:
        print("Error al guardar cambios")


    def eliminar_grupo():
        grupos = cargar_grupos()

    if not grupos:
        print("No hay grupos para eliminar.")
        return

    listar_grupos()

    id_grupo = input("ID del grupo a eliminar: ").strip()

    grupo = next((g for g in grupos if g["id"] == id_grupo), None)

    if not grupo:
        print(" Grupo no encontrado.")
        return

    confirmacion = input(f"¿Eliminar '{grupo['nombre']}'? (s/n): ").lower()

    if confirmacion == "s":
        grupos.remove(grupo)
        if guardar_grupos(grupos):
            print("Grupo eliminado correctamente")
        else:
            print(" Error al eliminar")
    else:
        print("Operación cancelada")


# ==============================
# EJECUCIÓN
# ==============================

if __name__ == "__main__":
    menu_grupos()

