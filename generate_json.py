import os
import csv
import json

# Rutas relativas a la estructura del proyecto
AREAS_DIR = "datos/csv/areas"
CATALOGOS_DIR = "datos/csv/catalogos"
OUTPUT_JSON = "datos/json/revistas_basicas.json"

def normalizar_titulo(titulo):
    return titulo.strip().lower()

def procesar_csv_por_directorio(directorio, tipo):
    data = {}
    for archivo in os.listdir(directorio):
        if archivo.endswith(".csv"):
            nombre = archivo.split(" ")[0].strip()  # Ejemplo: CIENCIAS_EXA
            path = os.path.join(directorio, archivo)
            with open(path, encoding="latin1") as f:
                lector = csv.reader(f)
                next(lector, None)  # Saltar encabezado
                for linea in lector:
                    if not linea:
                        continue
                    titulo = normalizar_titulo(linea[0])
                    if titulo not in data:
                        data[titulo] = {"areas": [], "catalogos": []}
                    data[titulo][tipo].append(nombre)
    return data

def merge_datos(areas_data, catalogos_data):
    all_titles = set(areas_data.keys()) | set(catalogos_data.keys())
    final_data = {}
    for titulo in all_titles:
        final_data[titulo] = {
            "areas": list(set(areas_data.get(titulo, {}).get("areas", []))),
            "catalogos": list(set(catalogos_data.get(titulo, {}).get("catalogos", [])))
        }
    return final_data

def main():
    print("Procesando archivos CSV...")
    areas = procesar_csv_por_directorio(AREAS_DIR, "areas")
    catalogos = procesar_csv_por_directorio(CATALOGOS_DIR, "catalogos")
    combinado = merge_datos(areas, catalogos)

    os.makedirs(os.path.dirname(OUTPUT_JSON), exist_ok=True)
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(combinado, f, indent=4, ensure_ascii=False)

    print(f"JSON generado exitosamente en: {OUTPUT_JSON}")

if __name__ == "__main__":
    main()
