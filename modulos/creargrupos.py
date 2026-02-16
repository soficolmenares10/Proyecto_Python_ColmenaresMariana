import json
import os

def cargar_grupos():
    """Cargar datos de grupos desde el JSON"""
    ruta_base = os.path.dirname(os.path.abspath(__file__))
    ruta_json = os.path.join(ruta_base, "../jsons/grupos.json")
    try:
        with open(ruta_json, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except:
        return []

def guardar_grupos(grupos):
    """Guardar datos de grupos en el JSON"""
    ruta_base = os.path.dirname(os.path.abspath(__file__))
    ruta_json = os.path.join(ruta_base, "../jsons/grupos.json")
    try:
        with open(ruta_json, "w", encoding="utf-8") as archivo:
            json.dump(grupos, archivo, indent=4, ensure_ascii=False)
        return True
    except:
        return False

def obtener_proximo_id(grupos):
    """Obtener el próximo ID disponible"""
    if not grupos:
        return "1"
    ids = [int(grupo["id"]) for grupo in grupos]
    return str(max(ids) + 1)

def menu_grupos():
    """Menú de gestión de grupos"""
    while True:
        print("--- Menú Gestión de Grupos ---")
        print("1. Crear grupo")
        print("2. Listar grupos")
        print("3. Editar grupo")
        print("4. Eliminar grupo")
        print("5. Volver al menú anterior")
        
        opcion = input("\nSeleccione una opción: ").strip()
        
        if opcion == "1":
            crear_grupo()
        elif opcion == "2":
            listar_grupos()
        elif opcion == "3":
            editar_grupo()
        elif opcion == "4":
            eliminar_grupo()
        elif opcion == "5":
            print("Volviendo al menú anterior...")
            break
        else:
            print("Opción no válida")

def crear_grupo():
    """Crear un nuevo grupo"""
    grupos = cargar_grupos()
    
    print("--- Crear Nuevo Grupo ---")
    
    nombre = input("Ingrese el nombre del grupo: ").strip()
    ruta = input("Ingrese la ruta (JAVA, NodeJS, NETCORE, etc): ").strip()
    trainer = input("Ingrese el nombre del trainer: ").strip()
    salon = input("Ingrese el salón: ").strip()
    fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ").strip()
    fecha_fin = input("Ingrese la fecha de fin (YYYY-MM-DD): ").strip()
    
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
        print(f"✓ Grupo '{nombre}' creado exitosamente con ID: {nuevo_id}")
    else:
        print("✗ Error al guardar el grupo")

def listar_grupos():
    """Listar todos los grupos"""
    grupos = cargar_grupos()
    
    if not grupos:
        print("No hay grupos registrados.")
        return
    
    print("--- Lista de Grupos ---")
    print("-" * 80)
    for grupo in grupos:
        print(f"ID: {grupo['id']} | Nombre: {grupo['nombre']} | Ruta: {grupo['ruta']} | Trainer: {grupo['trainer']}")
        print(f"Salón: {grupo['salon']} | Estado: {grupo['estado']}")
        print(f"Inicio: {grupo['fecha_inicio']} | Fin: {grupo['fecha_fin']}")
        print(f"Campers: {len(grupo['campers'])}")
        print("-" * 80)

def editar_grupo():
    """Editar un grupo existente"""
    grupos = cargar_grupos()
    
    if not grupos:
        print("\nNo hay grupos para editar.")
        return
    
    listar_grupos()
    
    id_grupo = input("Ingrese el ID del grupo a editar: ").strip()
    
    grupo_encontrado = None
    for grupo in grupos:
        if grupo["id"] == id_grupo:
            grupo_encontrado = grupo
            break
    
    if not grupo_encontrado:
        print(f"\n✗ Grupo con ID {id_grupo} no encontrado.")
        return
    
    print(f"\nEditando grupo: {grupo_encontrado['nombre']}")
    print("Deje en blanco si no desea cambiar un valor")
    
    nombre = input(f"Nombre ({grupo_encontrado['nombre']}): ").strip()
    if nombre:
        grupo_encontrado['nombre'] = nombre
    
    ruta = input(f"Ruta ({grupo_encontrado['ruta']}): ").strip()
    if ruta:
        grupo_encontrado['ruta'] = ruta
    
    trainer = input(f"Trainer ({grupo_encontrado['trainer']}): ").strip()
    if trainer:
        grupo_encontrado['trainer'] = trainer
    
    salon = input(f"Salón ({grupo_encontrado['salon']}): ").strip()
    if salon:
        grupo_encontrado['salon'] = salon
    
    if guardar_grupos(grupos):
        print(f"\n✓ Grupo actualizado exitosamente")
    else:
        print("\n✗ Error al guardar los cambios")

def eliminar_grupo():
    """Eliminar un grupo"""
    grupos = cargar_grupos()
    
    if not grupos:
        print("\nNo hay grupos para eliminar.")
        return
    
    listar_grupos()
    
    id_grupo = input("\nIngrese el ID del grupo a eliminar: ").strip()
    
    grupo_encontrado = None
    for i, grupo in enumerate(grupos):
        if grupo["id"] == id_grupo:
            grupo_encontrado = (i, grupo)
            break
    
    if not grupo_encontrado:
        print(f"\n✗ Grupo con ID {id_grupo} no encontrado.")
        return
    
    confirmacion = input(f"\n¿Está seguro de que desea eliminar el grupo '{grupo_encontrado[1]['nombre']}'? (s/n): ").strip().lower()
    
    if confirmacion == 's':
        grupos.pop(grupo_encontrado[0])
        if guardar_grupos(grupos):
            print(f"\n✓ Grupo eliminado exitosamente")
        else:
            print("\n✗ Error al eliminar el grupo")
    else:
        print("Operación cancelada")

if __name__ == "__main__":
    menu_grupos()
