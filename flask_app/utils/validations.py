import re
import filetype

EMAIL_REGEX = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")
CELULAR_REGEX = re.compile(r"^\+\d{3}\.\d{8}$")

def validar_email(email):
    return EMAIL_REGEX.match(email) is not None

def validar_celular(celular):
    return not celular or CELULAR_REGEX.match(celular)

def validar_fecha_iso(fecha):
    try:
        from datetime import datetime
        datetime.fromisoformat(fecha)
        return True
    except Exception:
        return False

def validar_tema_otro(temas, tema_otro):
    if 'otro' in temas:
        return tema_otro and len(tema_otro.strip()) >= 3
    return True

def validar_archivos_imagen(archivos):
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
    ALLOWED_MIMETYPES = {"image/jpeg", "image/png", "image/gif"}
    
    if not archivos or len(archivos) == 0:
        return False
    for archivo in archivos:
        if archivo and archivo.filename:
            extension = archivo.filename.rsplit('.', 1)[-1].lower()
            if extension not in ALLOWED_EXTENSIONS:
                return False
            tipo = filetype.guess(archivo)
            if not tipo or tipo.mime not in ALLOWED_MIMETYPES:
                return False
        else:
            return False
    return True

def validar_campos_obligatorios(data, archivos):
    campos = ['comuna', 'nombre', 'email', 'inicio', 'tema']
    for campo in campos:
        if not data.get(campo):
            return False
    if not archivos or len(archivos) == 0:
        return False
    return True

def validar_todo(data, archivos):
    errores = []
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
    if not validar_tema_otro(data.getlist('tema'), data.get('tema_otro')):
        errores.append('Debe ingresar un tema válido si selecciona "otro".')
    if not validar_archivos_imagen(archivos):
        errores.append('Todos los archivos deben ser imágenes válidas.')
    return errores

