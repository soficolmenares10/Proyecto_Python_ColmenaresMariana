import json
import os

def obtener_ruta_json():
    ruta_base = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(ruta_base, "../jsons/campers.json")

def cargar_campers():
    try:
        with open(obtener_ruta_json(), "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except:
        return []

def guardar_campers(campers):
    with open(obtener_ruta_json(), "w", encoding="utf-8") as archivo:
        json.dump(campers, archivo, indent=4)
def registrar_examen_inicial():
    print("--- Registrar examen inicial ---")
    
    campers = cargar_campers()
    id_buscar = input("Ingrese ID del camper: ").strip()
    
    for camper in campers:
        if camper["id"] == id_buscar:
            
            try:
                nota = float(input("Ingrese nota del examen (0-100): "))
            except:
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
def registrar_evaluacion_modulo():
    print("--- Registrar evaluación por módulo ---")
    
    campers = cargar_campers()
    id_buscar = input("Ingrese ID del camper: ").strip()
    
    for camper in campers:
        if camper["id"] == id_buscar:
            
            if camper.get("estado") != "Activo":
                print("El camper no está activo.")
                return
            
            modulo = input("Nombre del módulo: ").strip()
            
            try:
                teorica = float(input("Nota teórica: "))
                practica = float(input("Nota práctica: "))
                quices = float(input("Nota quices: "))
            except:
                print("Notas inválidas.")
                return
            
            nota_final = (teorica * 0.30) + (practica * 0.60) + (quices * 0.10)
            
            if "calificaciones" not in camper:
                camper["calificaciones"] = {}
            
            camper["calificaciones"][modulo] = round(nota_final, 2)
            
            # Detectar riesgo automáticamente
            if nota_final < 60:
                camper["riesgo"] = "Alto"
            else:
                camper["riesgo"] = "Bajo"
            
            guardar_campers(campers)
            
            print(f"Nota final registrada: {round(nota_final,2)}")
            print(f"Nivel de riesgo: {camper['riesgo']}")
            return
    
    print("Camper no encontrado.")
def detectar_campers_riesgo():
    print("--- Detectar campers en riesgo ---")
    
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
        if "asistencia" in camper:
            if camper["asistencia"] < 80:
                riesgo = "Alto"
        
        camper["riesgo"] = riesgo
        
        if riesgo == "Alto":
            print(f'{camper["nombres"]} {camper["apellidos"]} está en riesgo.')
            encontrados = True
    
    guardar_campers(campers)
    
    if not encontrados:
        print("No hay campers en riesgo.")


