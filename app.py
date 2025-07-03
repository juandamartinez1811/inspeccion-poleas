from flask import Flask, render_template, request,redirect, url_for
import firebase_admin
from firebase_admin import credentials, firestore
import webbrowser

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
    unidad = request.form['Unidad']

    if unidad=='Milimetros':
        try:
            val=float(valor1)
            return render_template('resultado.html',val=val,unidad=unidad)
        except ValueError:
            error='No se ingreso un valor numerico'
            return render_template('index.html',error=error)
    elif unidad=='Pulgadas':  
        try: 
            val=str(valor1)
            return render_template('resultado.html',val=val,unidad=unidad)
        except ValueError:
            error='No se ingreso un valor aceptable'
            return render_template('index.html',error=error)
            
if __name__ == '__main__':
    import os
    if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
        webbrowser.open("http://127.0.0.1:5000")
    app.run(debug=True)
