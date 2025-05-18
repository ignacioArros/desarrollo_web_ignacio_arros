from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Enum, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base, relationship, joinedload

DB_NAME = "tarea2"
DB_USERNAME = "cc5002"
DB_PASSWORD = "programacionweb"
DB_HOST = "localhost"
DB_PORT = 3306

DATABASE_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

# --- Models ---

class Region(Base):
    __tablename__ = 'region'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(200), nullable=False)

    comunas = relationship("Comuna", back_populates="region")


class Comuna(Base):
    __tablename__ = 'comuna'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(200), nullable=False)
    region_id = Column(Integer, ForeignKey('region.id'), nullable=False)

    region = relationship("Region", back_populates="comunas")
    actividades = relationship("Actividad", back_populates="comuna")


class Actividad(Base):
    __tablename__ = 'actividad'
    id = Column(Integer, primary_key=True, autoincrement=True)
    comuna_id = Column(Integer, ForeignKey('comuna.id'), nullable=False)
    sector = Column(String(100), nullable=True)
    nombre = Column(String(200), nullable=False)
    email = Column(String(100), nullable=False)
    celular = Column(String(15), nullable=True)
    dia_hora_inicio = Column(DateTime, nullable=False)
    dia_hora_termino = Column(DateTime, nullable=True)
    descripcion = Column(String(500), nullable=True)

    comuna = relationship("Comuna", back_populates="actividades")
    fotos = relationship("Foto", back_populates="actividad")
    contactos = relationship("ContactarPor", back_populates="actividad")
    temas = relationship("ActividadTema", back_populates="actividad")


class Foto(Base):
    __tablename__ = 'foto'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ruta_archivo = Column(String(300), nullable=False)
    nombre_archivo = Column(String(300), nullable=False)
    actividad_id = Column(Integer, ForeignKey('actividad.id'), nullable=False)

    actividad = relationship("Actividad", back_populates="fotos")


class ContactarPor(Base):
    __tablename__ = 'contactar_por'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(Enum('whatsapp', 'telegram', 'X', 'instagram', 'tiktok', 'otra'), nullable=False)
    identificador = Column(String(150), nullable=False)
    actividad_id = Column(Integer, ForeignKey('actividad.id'), nullable=False)

    actividad = relationship("Actividad", back_populates="contactos")


class ActividadTema(Base):
    __tablename__ = 'actividad_tema'
    id = Column(Integer, primary_key=True, autoincrement=True)
    tema = Column(Enum('música', 'deporte', 'ciencias', 'religión', 'política', 'tecnología', 'juegos', 'baile', 'comida', 'otro'), nullable=False)
    glosa_otro = Column(String(15), nullable=True)
    actividad_id = Column(Integer, ForeignKey('actividad.id'), nullable=False)

    actividad = relationship("Actividad", back_populates="temas")

# --- Database Functions ---

# --- Region ---
def get_all_regions():
    session = SessionLocal()
    regions = session.query(Region).all()
    session.close()
    return regions

def get_region_by_id(region_id):
    session = SessionLocal()
    region = session.query(Region).filter_by(id=region_id).first()
    session.close()
    return region

def create_region(nombre):
    session = SessionLocal()
    new_region = Region(nombre=nombre)
    session.add(new_region)
    session.commit()
    session.close()

def delete_region(region_id):
    session = SessionLocal()
    region = session.query(Region).filter_by(id=region_id).first()
    if region:
        session.delete(region)
        session.commit()
    session.close()

# --- Comuna ---
def get_all_comunas():
    session = SessionLocal()
    comunas = session.query(Comuna).all()
    session.close()
    return comunas

def get_comuna_by_id(comuna_id):
    session = SessionLocal()
    comuna = session.query(Comuna).filter_by(id=comuna_id).first()
    session.close()
    return comuna

def get_comunas_by_region(region_id):
    session = SessionLocal()
    comunas = session.query(Comuna).filter_by(region_id=region_id).all()
    session.close()
    return comunas

def create_comuna(nombre, region_id):
    session = SessionLocal()
    new_comuna = Comuna(nombre=nombre, region_id=region_id)
    session.add(new_comuna)
    session.commit()
    session.close()

def delete_comuna(comuna_id):
    session = SessionLocal()
    comuna = session.query(Comuna).filter_by(id=comuna_id).first()
    if comuna:
        session.delete(comuna)
        session.commit()
    session.close()

# --- Actividad ---
def get_all_actividades():
    session = SessionLocal()
    actividades = session.query(Actividad).options(
        joinedload(Actividad.comuna),
        joinedload(Actividad.contactos),
        joinedload(Actividad.temas),
        joinedload(Actividad.fotos)).all()
    session.close()
    return actividades

def get_actividad_by_id(actividad_id):
    session = SessionLocal()
    actividad = session.query(Actividad).filter_by(id=actividad_id).options(
        joinedload(Actividad.comuna),
        joinedload(Actividad.contactos), 
        joinedload(Actividad.temas),
        joinedload(Actividad.fotos)).first()
    session.close()
    return actividad

def get_actividad_by_campos(nombre, email, dia_hora_inicio):
    session = SessionLocal()
    actividad = session.query(Actividad).filter_by(
        nombre=nombre,
        email=email,
        dia_hora_inicio=dia_hora_inicio
    ).first()
    session.close()
    return actividad

def create_actividad(comuna_id, sector, nombre, email, celular, dia_hora_inicio, dia_hora_termino, descripcion):
    session = SessionLocal()
    new_actividad = Actividad(
        comuna_id=comuna_id,
        sector=sector,
        nombre=nombre,
        email=email,
        celular=celular,
        dia_hora_inicio=dia_hora_inicio,
        dia_hora_termino=dia_hora_termino,
        descripcion=descripcion
    )
    session.add(new_actividad)
    session.commit()
    session.close()

def delete_actividad(actividad_id):
    session = SessionLocal()
    actividad = session.query(Actividad).filter_by(id=actividad_id).first()
    if actividad:
        session.delete(actividad)
        session.commit()
    session.close()

# --- Foto ---
def get_all_fotos():
    session = SessionLocal()
    fotos = session.query(Foto).all()
    session.close()
    return fotos

def create_foto(ruta_archivo, nombre_archivo, actividad_id):
    session = SessionLocal()
    new_foto = Foto(ruta_archivo=ruta_archivo, nombre_archivo=nombre_archivo, actividad_id=actividad_id)
    session.add(new_foto)
    session.commit()
    session.close()

# --- ContactarPor ---
def get_all_contactos():
    session = SessionLocal()
    contactos = session.query(ContactarPor).all()
    session.close()
    return contactos

def create_contacto(nombre, identificador, actividad_id):
    session = SessionLocal()
    new_contacto = ContactarPor(nombre=nombre, identificador=identificador, actividad_id=actividad_id)
    session.add(new_contacto)
    session.commit()
    session.close()

# --- ActividadTema ---
def get_all_temas():
    session = SessionLocal()
    temas = session.query(ActividadTema).all()
    session.close()
    return temas

def create_tema(tema, glosa_otro, actividad_id):
    session = SessionLocal()
    new_tema = ActividadTema(tema=tema, glosa_otro=glosa_otro, actividad_id=actividad_id)
    session.add(new_tema)
    session.commit()
    session.close()