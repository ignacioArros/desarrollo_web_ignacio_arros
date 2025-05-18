import re
import filetype

EMAIL_REGEX = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")
CELULAR_REGEX = re.compile(r"^\+\d{3}\.\d{8}$")
TEMAS_VALIDOS = {'música', 'deporte', 'ciencias', 'religión', 'política', 'tecnología', 'juegos', 'baile', 'comida', 'otro'}
MAX_FOTOS = 5
MAX_TAMANO_FOTO = 10 * 1024 * 1024  # 10 MB

def validar_email(email):
    return EMAIL_REGEX.match(email) is not None

def validar_celular(celular):
    return not celular or CELULAR_REGEX.match(celular)

def validar_contactos(contactos):
    # contactos es una lista de diccionarios [{'nombre':..., 'identificador':...}]
    if not contactos or len(contactos) == 0:
        return False
    if len(contactos) > 5:
        return False
    for c in contactos:
        if not c.get('nombre') or not c.get('identificador'):
            return False
        # Validación simple de identificador: no vacío y sin espacios al inicio/final
        if not c['identificador'].strip():
            return False
    return True

def validar_fecha_iso(fecha):
    try:
        from datetime import datetime
        datetime.fromisoformat(fecha)
        return True
    except Exception:
        return False

def validar_fechas_inicio_termino(inicio, termino):
    if not termino:
        return True
    from datetime import datetime
    try:
        inicio_dt = datetime.fromisoformat(inicio)
        termino_dt = datetime.fromisoformat(termino)
        return termino_dt > inicio_dt
    except Exception:
        return False

def validar_longitud_campo(valor, min_len, max_len):
    if valor is None:
        return False
    return min_len <= len(valor.strip()) <= max_len

def validar_tema_otro(temas, tema_otro):
    if 'otro' in temas:
        return tema_otro and len(tema_otro.strip()) >= 3
    return True

def validar_temas(temas):
    return all(t in TEMAS_VALIDOS for t in temas)

def validar_archivos_imagen(archivos):
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
    ALLOWED_MIMETYPES = {"image/jpeg", "image/png", "image/gif"}
    
    # Filtrar solo los archivos que realmente tienen un nombre (caso en que no se seleccionan más fotos en el formulario)
    archivos_validos = [archivo for archivo in archivos if archivo and archivo.filename]
    if not archivos_validos:
        return False
    if len(archivos_validos) > MAX_FOTOS:
        return False
    for archivo in archivos_validos:
        extension = archivo.filename.rsplit('.', 1)[-1].lower()
        if extension not in ALLOWED_EXTENSIONS:
            return False
        tipo = filetype.guess(archivo)
        if not tipo or tipo.mime not in ALLOWED_MIMETYPES:
            return False
        # Validar tamaño máximo por archivo
        archivo.seek(0, 2)  # Ir al final del archivo
        size = archivo.tell()
        archivo.seek(0)     # Volver al inicio
        if size > MAX_TAMANO_FOTO:
            return False
    return True

def validar_campos_obligatorios(data, archivos):
    campos = ['comuna', 'nombre', 'email', 'inicio', 'tema']
    for campo in campos:
        if not data.get(campo):
            return False
    archivos_validos = [archivo for archivo in archivos if archivo and archivo.filename]
    if not archivos_validos:
        return False
    return True

def validar_todo(data, archivos, contactos=None):
    errores = []
    temas = data.getlist('tema') if hasattr(data, 'getlist') else data.get('tema', [])
    if not validar_campos_obligatorios(data, archivos):
        errores.append('Faltan datos obligatorios o no se seleccionó ninguna foto.')
    if not validar_email(data.get('email', '')):
        errores.append('El correo electrónico no es válido.')
    if not validar_celular(data.get('celular', '')):
        errores.append('El número de celular no es válido.')
    if not validar_fecha_iso(data.get('inicio', '')):
        errores.append('La fecha de inicio no es válida.')
    if data.get('termino') and not validar_fecha_iso(data.get('termino')):
        errores.append('La fecha de término no es válida.')
    if not validar_fechas_inicio_termino(data.get('inicio', ''), data.get('termino', '')):
        errores.append('La fecha de término debe ser posterior a la de inicio.')
    if not validar_longitud_campo(data.get('nombre', ''), 0, 200):
        errores.append('El nombre no puede exceder 200 caracteres.')
    if data.get('sector') and not validar_longitud_campo(data.get('sector', ''), 0, 100):
        errores.append('El sector no puede exceder 100 caracteres.')
    if data.get('descripcion') and not validar_longitud_campo(data.get('descripcion', ''), 0, 500):
        errores.append('La descripción no puede exceder 500 caracteres.')
    if not validar_temas(temas):
        errores.append('Uno o más temas seleccionados no son válidos.')
    if not validar_tema_otro(temas, data.get('tema_otro')):
        errores.append('Debe ingresar un tema válido si selecciona "otro".')
    if not validar_archivos_imagen(archivos):
        errores.append('Todos los archivos deben ser imágenes válidas, no exceder 10 MB y máximo 5 fotos.')
    if contactos is not None and not validar_contactos(contactos):
        errores.append('Debes ingresar entre 1 y 5 formas de contacto válidas.')
    return errores

