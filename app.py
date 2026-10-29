import random
import json
from flask import Flask, render_template

with open('datos.json', 'r', encoding='utf-8') as f:
    datos = json.load(f)
    
    
def aleatorizar_nombre():
    prefijo = random.choice(datos["prefijos"])
    sufijo = random.choice(datos["sufijos"])
    nombre = prefijo + sufijo
    return nombre

def generar_pnj():
    nombre = aleatorizar_nombre()
    raza = random.choice(datos["razas"])
    oficio = random.choice(datos["oficios"])
    personalidad = random.choice(datos["personalidades"])
    tic = random.choice(datos["tics"])
    intencion = random.choice(datos["intenciones"])
    info = random.choice(datos["informacion"])
    personaje = {"nombre" : nombre, "raza" : raza, "oficio" : oficio, "personalidad" : personalidad, "tic" : tic, "intencion" : intencion, "informacion" : info}
    return personaje

app = Flask(__name__)
@app.route("/")
def home():
    # Llamamos a tu función para que cree un PNJ nuevo cada vez que entres
    pnj = generar_pnj()
    # Por ahora devolvemos el diccionario en formato texto limpio a la pantalla
    return render_template("index.html", pnj=pnj)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)