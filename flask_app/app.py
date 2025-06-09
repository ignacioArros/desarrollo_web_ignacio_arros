from flask import Flask, render_template, request, redirect, url_for, flash, abort, jsonify
from database.db import (
    get_all_regions, get_all_comunas, get_all_actividades, get_all_actividades_por_id_desc, get_actividad_by_id,
    get_actividad_by_campos, create_actividad, create_tema, create_contacto, create_foto,
    get_actividades_por_dia, get_actividades_por_tipo, get_actividades_por_horario, get_resumen_general,
    create_comentario, get_comentarios_por_actividad
)
import hashlib
import os
import filetype
from datetime import datetime
from werkzeug.utils import secure_filename
from utils.validations import validar_todo
from sqlalchemy import func

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

# Ruta para las estadísticas
@app.route('/estadisticas')
def estadisticas():
    return render_template('estadisticas.html')

# Rutas API
# Ruta para obtener las actividades por día
@app.route('/api/estadisticas/actividades_por_dia')
def api_actividades_por_dia():
    results = get_actividades_por_dia()
    dias = [str(r[0]) for r in results]
    cantidades = [r[1] for r in results]
    return jsonify({"dias": dias, "cantidades": cantidades})

# Ruta para obtener las actividades por tipo
@app.route('/api/estadisticas/actividades_por_tipo')
def api_actividades_por_tipo():
    results = get_actividades_por_tipo()
    tipos = [r[0] for r in results]
    cantidades = [r[1] for r in results]
    return jsonify({"tipos": tipos, "cantidades": cantidades})

# Ruta para obtener las actividades por horario
@app.route('/api/estadisticas/actividades_por_horario')
def api_actividades_por_horario():
    actividades = get_actividades_por_horario()
    meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    mes_idx = {i+1: meses[i] for i in range(12)}
    conteo = {mes: {'manana': 0, 'mediodia': 0, 'tarde': 0} for mes in meses}
    for act in actividades:
        if not act.dia_hora_inicio:
            continue
        mes = mes_idx[act.dia_hora_inicio.month]
        hora = act.dia_hora_inicio.hour
        if 6 <= hora < 12:
            conteo[mes]['manana'] += 1
        elif 12 <= hora < 18:
            conteo[mes]['mediodia'] += 1
        elif 18 <= hora < 24 or 0 <= hora < 6:
            conteo[mes]['tarde'] += 1
    meses_con_datos = [mes for mes in meses if sum(conteo[mes].values()) > 0]
    manana = [conteo[mes]['manana'] for mes in meses_con_datos]
    mediodia = [conteo[mes]['mediodia'] for mes in meses_con_datos]
    tarde = [conteo[mes]['tarde'] for mes in meses_con_datos]
    return jsonify({
        "meses": meses_con_datos,
        "manana": manana,
        "mediodia": mediodia,
        "tarde": tarde
    })

# Ruta para obtener el resumen general de estadísticas
@app.route('/api/estadisticas/resumen_general')
def api_resumen_general():
    data = get_resumen_general()
    total_actividades = data["total_actividades"]
    region_nombre = data["region"].nombre if data["region"] else ""
    tema_nombre = data["tema_frecuente"][0] if data["tema_frecuente"] else ""
    return jsonify({
        "total_actividades": total_actividades,
        "region_top": region_nombre,
        "tema_top": tema_nombre
    })

# Ruta para subir un comentario asociado a una actividad
@app.route('/api/comentarios/<int:actividad_id>', methods=['POST'])
def api_post_comentario(actividad_id):
    data = request.get_json()
    nombre = data.get('nombre', '').strip()
    texto = data.get('texto', '').strip()
    errores = []
    if not (3 <= len(nombre) <= 80):
        errores.append("El nombre debe tener entre 3 y 80 caracteres.")
    if not (len(texto) >= 5):
        errores.append("El comentario debe tener al menos 5 caracteres.")
    if errores:
        return jsonify({"ok": False, "errores": errores}), 400
    create_comentario(nombre=nombre, texto=texto, fecha=datetime.now(), actividad_id=actividad_id)
    return jsonify({"ok": True})

# Ruta para obtener los comentarios de una actividad
@app.route('/api/comentarios/<int:actividad_id>', methods=['GET'])
def api_get_comentarios(actividad_id):
    comentarios = get_comentarios_por_actividad(actividad_id)
    comentarios_json = [
        {
            "nombre": c.nombre,
            "texto": c.texto,
            "fecha": c.fecha.strftime('%Y-%m-%d %H:%M')
        }
        for c in comentarios
    ]
    return jsonify(comentarios_json)

