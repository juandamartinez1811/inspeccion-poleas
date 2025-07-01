from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def formulario():
    return render_template('index.html')

@app.route('/procesar', methods=['POST'])
def procesar():
    valor1 = request.form['valor1']
    return render_template('resultado.html', val=valor1)

if __name__ == '__main__':
    app.run(debug=True)
