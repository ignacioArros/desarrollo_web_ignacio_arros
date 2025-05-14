from flask import Flask, render_template, request, redirect, url_for, flash
from database.db import SessionLocal, engine, Region, Comuna, Actividad, ActividadTema, ContactarPor, Foto
from sqlalchemy.exc import SQLAlchemyError
import os
from datetime import datetime
from werkzeug.utils import secure_filename

# Configuración
app = Flask(__name__)
app.secret_key = 'clave_secreta_segura'
app.config['UPLOAD_FOLDER'] = 'uploads'

# Asegurarse que la carpeta de subida existe
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Ruta: Portada
@app.route('/')
def index():
    session = SessionLocal()
    actividades = session.query(Actividad).order_by(Actividad.dia_hora_inicio.desc()).limit(5).all()
    session.close()
    return render_template('index.html', actividades=actividades)

# Ruta: Informar Actividad
@app.route('/informar', methods=['GET', 'POST'])
def informar():
    session = SessionLocal()
    regiones = session.query(Region).order_by(Region.nombre).all()

    if request.method == 'POST':
        try:
            # === Obtener datos del formulario ===
            comuna_id = request.form.get('comuna')
            sector = request.form.get('sector', '')
            nombre = request.form.get('nombre')
            email = request.form.get('email')
            celular = request.form.get('celular')
            inicio = request.form.get('inicio')
            termino = request.form.get('termino')
            descripcion = request.form.get('descripcion', '')
            temas = request.form.getlist('tema')
            tema_otro = request.form.get('tema_otro')
            contactos = request.form.getlist('contacto')
            archivos = request.files.getlist('fotos')

            # === Validaciones básicas ===
            if not comuna_id or not nombre or not email or not inicio or not temas or len(archivos) == 0:
                flash('Faltan datos obligatorios o no se seleccionó ninguna foto.')
                return render_template('informar.html', regiones=regiones)

            if 'otro' in temas and (not tema_otro or len(tema_otro.strip()) < 3):
                flash('Debe ingresar un tema válido si selecciona "otro".')
                return render_template('informar.html', regiones=regiones)

            # === Insertar actividad ===
            actividad = Actividad(
                comuna_id=int(comuna_id),
                sector=sector,
                nombre=nombre,
                email=email,
                celular=celular,
                dia_hora_inicio=datetime.fromisoformat(inicio),
                dia_hora_termino=datetime.fromisoformat(termino) if termino else None,
                descripcion=descripcion
            )
            session.add(actividad)
            session.flush()  # Obtener ID

            # === Insertar temas ===
            for t in temas:
                tema_nombre = tema_otro if t == 'otro' else t
                session.add(ActividadTema(actividad_id=actividad.id, tema=tema_nombre))

            # === Insertar contactos ===
            for red in contactos:
                identificador = request.form.get(f'{red}-id')
                if identificador:
                    session.add(ContactarPor(actividad_id=actividad.id, red_social=red, identificador=identificador))

            # === Guardar fotos ===
            for archivo in archivos[:5]:
                if archivo and archivo.filename:
                    nombre_archivo = secure_filename(archivo.filename)
                    ruta = os.path.join(app.config['UPLOAD_FOLDER'], nombre_archivo)
                    archivo.save(ruta)
                    session.add(Foto(actividad_id=actividad.id, archivo=nombre_archivo))

            session.commit()
            flash('Actividad registrada exitosamente.')
            return redirect(url_for('index'))

        except SQLAlchemyError as e:
            session.rollback()
            flash(f'Error al guardar en la base de datos: {str(e)}')
        finally:
            session.close()

    else:
        session.close()
        return render_template('informar.html', regiones=regiones)

# Ruta para el listado
@app.route('/listado')
def listado():
    session = SessionLocal()
    try:
        page = int(request.args.get('page', 1))
        per_page = 5
        total = session.query(Actividad).count()
        actividades = (
            session.query(Actividad)
            .order_by(Actividad.dia_hora_inicio.desc())
            .offset((page - 1) * per_page)
            .limit(per_page)
            .all()
        )

        max_page = (total + per_page - 1) // per_page
        return render_template(
            'listado.html',
            actividades=actividades,
            page=page,
            max_page=max_page
        )
    finally:
        session.close()

@app.route('/estadisticas')
def estadisticas():
    return render_template('estadisticas.html')

