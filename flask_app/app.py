from flask import Flask, render_template, request, redirect, url_for, flash, abort
from database.db import (
    get_all_regions, get_all_comunas, get_all_actividades, get_all_actividades_por_id_desc, get_actividad_by_id,
    get_actividad_by_campos, create_actividad, create_tema, create_contacto, create_foto
)
import hashlib
import os
import filetype
from datetime import datetime
from werkzeug.utils import secure_filename
from utils.validations import validar_todo

UPLOAD_FOLDER = 'static/uploads'

# Configuración
app = Flask(__name__)
app.secret_key = 'clave_secreta_segura'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Asegurarse que la carpeta de subida existe
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Ruta para la portada
@app.route('/')
def index():
    actividades = get_all_actividades_por_id_desc()[:5]
    return render_template('index.html', actividades=actividades)

# Ruta para agregar actividades
@app.route('/informar', methods=['GET', 'POST'])
def informar():
    regiones = get_all_regions()
    comunas = get_all_comunas()
    # Construir estructura para JS
    regiones_y_comunas = [
        {
            "id": region.id,
            "nombre": region.nombre,
            "comunas": [
                {"id": comuna.id, "nombre": comuna.nombre}
                for comuna in comunas if comuna.region_id == region.id
            ]
        }
        for region in regiones
    ]
    if request.method == 'POST':
        data = request.form
        archivos = request.files.getlist('fotos')
        errores = validar_todo(data, archivos)
        if errores:
            for error in errores:
                flash(error)
            return render_template('informar.html', regiones=regiones, regiones_y_comunas=regiones_y_comunas, mostrar_gracias=False)
        try:
            # Obtener datos del formulario 
            comuna_id = request.form.get('comuna')
            sector = request.form.get('sector', '')
            nombre = request.form.get('nombre')
            email = request.form.get('email')
            celular = request.form.get('telefono')
            inicio = request.form.get('inicio')
            termino = request.form.get('termino')
            descripcion = request.form.get('descripcion', '')
            temas = request.form.getlist('tema')
            tema_otro = request.form.get('tema_otro')
            contactos = request.form.getlist('contacto')
            archivos = request.files.getlist('fotos')
            # print(comuna_id, sector, nombre, email, celular, inicio, termino, descripcion, temas, tema_otro, contactos)

            # Insertar actividad
            create_actividad(
                comuna_id=int(comuna_id),
                sector=sector,
                nombre=nombre,
                email=email,
                celular=celular,
                dia_hora_inicio=datetime.fromisoformat(inicio),
                dia_hora_termino=datetime.fromisoformat(termino) if termino else None,
                descripcion=descripcion
            )
            # Recuperar la última actividad creada de forma segura
            actividad = get_actividad_by_campos(nombre=nombre, email=email, dia_hora_inicio=datetime.fromisoformat(inicio))
            if not actividad:
                flash('No se pudo recuperar la actividad recién creada.')
                return render_template('informar.html', regiones=regiones, regiones_y_comunas=regiones_y_comunas, mostrar_gracias=False)

            # Insertar temas 
            for t in temas:
                if t == 'otro':
                    create_tema(tema='otro', glosa_otro=tema_otro, actividad_id=actividad.id)
                else:
                    create_tema(tema=t, glosa_otro=None, actividad_id=actividad.id)

            # Insertar contactos
            for red in contactos:
                nombre = red.lower()
                identificador = request.form.get(f'{nombre}-id')
                if nombre == 'otro':
                    nombre = 'otra'
                if identificador:
                    create_contacto(nombre=nombre, identificador=identificador, actividad_id=actividad.id)

            # Guardar fotos
            for archivo in archivos[:5]:
                if archivo and archivo.filename:
                    _filename = hashlib.sha256(
                        secure_filename(archivo.filename) # nombre del archivo
                        .encode("utf-8") # encodear a bytes
                        ).hexdigest()
                    _extension = filetype.guess(archivo).extension
                    img_filename = f"{_filename}.{_extension}"
                    ruta = os.path.join(app.config['UPLOAD_FOLDER'], img_filename)
                    archivo.save(ruta)
                    create_foto(ruta_archivo=ruta, nombre_archivo=img_filename, actividad_id=actividad.id)

            flash('Actividad registrada exitosamente.')
            return render_template('informar.html', regiones=regiones, regiones_y_comunas=regiones_y_comunas, mostrar_gracias=True)

        except Exception as e:
            flash(f'Error al guardar en la base de datos: {str(e)}')
    return render_template('informar.html', regiones=regiones, regiones_y_comunas=regiones_y_comunas, mostrar_gracias=False)

# Ruta para el listado
@app.route('/listado')
def listado():
    page = int(request.args.get('page', 1))
    per_page = 5
    actividades = get_all_actividades_por_id_desc()
    total = len(actividades)
    actividades_pagina = actividades[(page-1)*per_page:page*per_page]
    max_page = (total + per_page - 1) // per_page
    if total == 0:
        max_page = 1
    return render_template(
        'listado.html',
        actividades=actividades_pagina,
        page=page,
        max_page=max_page
    )

# Ruta para el detalle de una actividad
@app.route('/actividad/<int:actividad_id>')
def detalle_actividad(actividad_id):
    actividad = get_actividad_by_id(actividad_id)
    if not actividad:
        abort(404)
    return render_template('detalle.html', actividad=actividad)

@app.route('/estadisticas')
def estadisticas():
    return render_template('estadisticas.html')

