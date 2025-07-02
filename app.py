from flask import Flask, render_template, request,redirect, url_for
import firebase_admin
from firebase_admin import credentials, firestore

#aqui se inicializa flask
app = Flask(__name__)

#Inicializar la base de datos
cred = credentials.Certificate("firebase/credenciales.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.route('/')
def formulario():
    return render_template('index.html')

@app.route('/procesar', methods=['POST'])
def procesar():
    valor1 = request.form['valor1']
    try:
        numero=str(valor1)
#Hay que programar los dos botones para elegir si se debe hacer la busqueda por pulgada o por milimetros#
#programar las dos querys#

    except ValueError:  
        error = "⚠️ Debes ingresar un número válido"
        return render_template('index.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)
