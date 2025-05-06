from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/informar')
def informar():
    return render_template('informar.html')

@app.route('/listado')
def listado():
    return render_template('listado.html')

@app.route('/estadisticas')
def estadisticas():
    return render_template('estadisticas.html')

