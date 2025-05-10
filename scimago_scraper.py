import os
import json
import time
import requests
from bs4 import BeautifulSoup

REVISTAS_JSON = 'datos/json/revistas_basicas.json'
SCIMAGO_JSON = 'datos/json/scimago_data.json'
BASE_SEARCH_URL = "https://www.scimagojr.com/journalsearch.php?q="

# Cargar revistas
with open(REVISTAS_JSON, 'r', encoding='utf-8') as f:
    revistas = json.load(f)

# Cargar base existente de datos scrappeados
if os.path.exists(SCIMAGO_JSON):
    with open(SCIMAGO_JSON, 'r', encoding='utf-8') as f:
        scimago_data = json.load(f)
else:
    scimago_data = {}

headers = {
    "User-Agent": "Mozilla/5.0"
}

def buscar_en_scimago(nombre_revista):
    try:
        query = nombre_revista.replace(" ", "+")
        search_url = f"https://www.scimagojr.com/journalsearch.php?q={query}"
        r = requests.get(search_url, headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')

        enlace = soup.find("a", class_="search_results_title")
        if not enlace:
            return None
        
        revista_url = "https://www.scimagojr.com/" + enlace['href']
        r_detalle = requests.get(revista_url, headers=headers)
        soup_detalle = BeautifulSoup(r_detalle.text, 'html.parser')

        # Extracción de campos
        info = {}
        tabla = soup_detalle.find("div", {"id": "journaldescription"})
        if tabla:
            info["website"] = tabla.find("a").get("href", "") if tabla.find("a") else ""
            info["publisher"] = tabla.find("p").text.strip().split("\n")[0] if tabla.find("p") else ""
        
        info["h_index"] = soup_detalle.find("div", class_="hindexnumber").text.strip()
        info["subject_areas"] = [x.text.strip() for x in soup_detalle.select(".cell.subjectarea")]
        info["publication_type"] = soup_detalle.find("div", class_="publicationtype").text.strip() if soup_detalle.find("div", class_="publicationtype") else ""
        info["issn"] = soup_detalle.find("div", class_="issn").text.strip().replace("ISSN: ", "") if soup_detalle.find("div", class_="issn") else ""
        info["widget"] = revista_url.replace("journalsearch.php?q=", "journalrank.php?journal=")

        return info

    except Exception as e:
        print(f"Error buscando {nombre_revista}: {e}")
        return None

# Procesar cada revista
for titulo in revistas:
    if titulo in scimago_data:
        print(f"✓ Ya existe: {titulo}")
        continue

    print(f"🔍 Buscando: {titulo}")
    data = buscar_en_scimago(titulo)
    if data:
        scimago_data[titulo] = data
        # Guardar progresivamente para no perder avances
        with open(SCIMAGO_JSON, 'w', encoding='utf-8') as f:
            json.dump(scimago_data, f, indent=4, ensure_ascii=False)
    else:
        print(f"⚠️ No se encontró información de: {titulo}")
    
    time.sleep(2)  # Cortesía para evitar bloquear IP

print("✅ Scraping completo.")
