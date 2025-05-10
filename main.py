from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)

# Ruta al JSON generado por el scraper
RUTA_JSON = os.path.join("datos", "json", "revistas_completo.json")

# Cargar revistas desde JSON
with open(RUTA_JSON, "r", encoding="utf-8") as f:
    revistas = json.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/areas")
def mostrar_areas():
    areas = set()
    for datos in revistas.values():
        for area in datos.get("areas", []):
            areas.add(area)
    return render_template("areas.html", areas=sorted(areas))

@app.route("/area/<nombre>")
def revistas_por_area(nombre):
    filtradas = {titulo: datos for titulo, datos in revistas.items() if nombre in datos.get("areas", [])}
    return render_template("revistas_filtradas.html", tipo="Área", filtro=nombre, revistas=filtradas)

@app.route("/catalogos")
def mostrar_catalogos():
    catalogos = set()
    for datos in revistas.values():
        for cat in datos.get("catalogos", []):
            catalogos.add(cat)
    return render_template("catalogos.html", catalogos=sorted(catalogos))

@app.route("/catalogo/<nombre>")
def revistas_por_catalogo(nombre):
    filtradas = {titulo: datos for titulo, datos in revistas.items() if nombre in datos.get("catalogos", [])}
    return render_template("revistas_filtradas.html", tipo="Catálogo", filtro=nombre, revistas=filtradas)

@app.route("/explorar")
def explorar():
    letras = sorted(set(titulo[0].upper() for titulo in revistas))
    return render_template("explorar.html", letras=letras)

@app.route("/explorar/<letra>")
def revistas_por_letra(letra):
    filtradas = {titulo: datos for titulo, datos in revistas.items() if titulo.lower().startswith(letra.lower())}
    return render_template("revistas_letra.html", letra=letra, revistas=filtradas)

@app.route("/revista/<titulo>")
def detalle_revista(titulo):
    datos = revistas.get(titulo)
    if datos:
        return render_template("revista_detalle.html", titulo=titulo, datos=datos)
    else:
        return "Revista no encontrada", 404

@app.route("/busqueda")
def busqueda():
    query = request.args.get("q", "").lower()
    if query:
        resultados = {titulo: datos for titulo, datos in revistas.items() if query in titulo.lower()}
    else:
        resultados = {}
    return render_template("busqueda.html", query=query, revistas=resultados)

@app.route("/creditos")
def creditos():
    alumnos = ["Alumno A", "Alumno B"]
    return render_template("creditos.html", alumnos=alumnos)

if __name__ == "__main__":
    app.run(debug=True)
