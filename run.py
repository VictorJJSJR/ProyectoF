from flask import Flask, render_template, request, redirect, url_for
import json
import os
import string

app = Flask(__name__)

with open("datos/json/scimago_catalogo.json", "r", encoding="utf-8") as f:
    revistas = json.load(f)

# Obtener todas las áreas y catálogos únicos
todas_areas = set()
todos_catalogos = set()
for datos in revistas.values():
    todas_areas.update(datos.get("areas", []))
    todos_catalogos.update(datos.get("catalogos", []))
todas_areas = sorted(todas_areas)
todos_catalogos = sorted(todos_catalogos)

@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/areas")
def areas():
    return render_template("areas.html", areas=todas_areas)

@app.route("/areas/<area>")
def revistas_por_area(area):
    revistas_area = {
        titulo: datos
        for titulo, datos in revistas.items()
        if area in datos.get("areas", [])
    }
    return render_template("revistas_area.html", area=area, revistas=revistas_area)

@app.route("/catalogos")
def catalogos():
    return render_template("catalogos.html", catalogos=todos_catalogos)

@app.route("/catalogos/<catalogo>")
def revistas_por_catalogo(catalogo):
    revistas_catalogo = {
        titulo: datos
        for titulo, datos in revistas.items()
        if catalogo in datos.get("catalogos", [])
    }
    return render_template("revistas_catalogo.html", catalogo=catalogo, revistas=revistas_catalogo)

@app.route("/explorar")
def explorar():
    letras = list(string.ascii_uppercase)
    return render_template("explorar.html", letras=letras)

@app.route("/explorar/<letra>")
def explorar_letra(letra):
    revistas_filtradas = {
        titulo: datos
        for titulo, datos in revistas.items()
        if titulo.lower().startswith(letra.lower())
    }
    return render_template("revistas_letra.html", letra=letra, revistas=revistas_filtradas)

@app.route("/revista/<titulo>")
def detalle_revista(titulo):
    datos = revistas.get(titulo)
    return render_template("revista_detalle.html", titulo=titulo, datos=datos)

@app.route("/creditos")
def creditos():
    return render_template("creditos.html")

if __name__ == "__main__":
    app.run(debug=True)
