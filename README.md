# ProyectoFinal
Proyecto final de 2025-1 DS IV 10:00hrs

## Miembros del equipo:
- Victor Javier Jurado Sanchez Jr.
- Jesus Alejandro Coronado Barraza (No alumno)

Utilización de inteligencia artificial: Si, se utilizo para limpiar el código y darle una mejor estructura. (ChatGPT)

Jesus Alejandro participo en este proyecto porque ya teníamos experiencia trabajando juntos y el quería expandir su portafolio de trabajo, asi que vimos esto como la perfecta oportunidad para hacerlo.

Aclaracion de subida de cambios al proyecto:
Al hacer todos los cambios estos se tuvieron que hacer desde un mismo equipo, por ello para diferenciar quien hizo que, se puso la inicial de un nombre, (V) para Victor y (A) para Jesus Alejandro.

## Estructura del proyecto:

proyecto/

├── app/

│─── main.py

│    ├─────── static/       <- Logotipo

│    └─────── templates/    <- Contenedor de html

├── scimago_scraper.py

├── datos/

│   ├─────── csv/

│   │ ├───────── areas/      <- Archivos csv

│   │ └───────── catalogos/  <- Archivos csv

│   └────── json/

│   ├──────────── revistas_basicas.json

│   └──────────── revistas_scimago.json

├─── requirimientos.txt

|─── generate_json.py

└─── README.md


## Requisitos

- Python 3.10+
- pip

Instalar dependencias:

bash:
pip install -r requerimientos.txt

# Instrucciones para el funcionamiento del programa:

## Parte 1:
Existe un sript para hacer que la parte 1 funcione por separado para probarlo, este es "generate_json.py" por si se desea probar, para probarse se tiene que ir a la raiz del proyecto y escribir en una terminal: "python generate_json.py".

Y esto genera el archivo en datos/json/revistas_basicas.json

## Parte 2:
Ejectura en terminal: python scimago_scraper.py (Tomara un largo tiempo, minimo 1 hora, pero hace la busqueda correctamente.)

Esto lee revistas_basicas.json, consulta SCIMAGO y genera revistas_scimago.json.

Nota: Si un título ya fue descargado, no se vuelve a consultar.

## Parte 3:
1. Primero se tiene que correr la Parte 2, despues:

2. Instalar los requerimientos.

3. Desde la carpeta raiz: python main.py

4. Posteriormente atraves del navegador acceder a: http://localhost:5000

## Puntos Extras cumplidos:
1. Logotipo con nombre del sistema (1 punto)
2. Presentacion con las funcionalidades claves del programa (2 puntos)

## Aclaracion final: 
Al momento de hacer actualizaciones en GitHub, los cambios tendían a ser muy grandes porque se solían hacer muchos cambios antes de subirse y estos se acumulaban.

