# Plataforma de Registro de Actividades - Tarea 3 - Desarrollo Web

Este proyecto es una aplicación web desarrollada para el curso CC5002 - Desarrollo de Aplicaciones Web, de la carrera de Ingeniería Civil en Computación de la Universidad de Chile. Posee las siguientes funcionalidades:

- Permite registrar, guardar, listar y visualizar actividades realizadas en distintas comunas y regiones, con detalles sobre el autor, el tema y fotografías. 

- Cada actividad posee una sección de comentarios (que son guardados en relación con la actividad).

- Hay estadísticas funcionales que permiten ver las actividades registradas, ya sea por la cantidad de actividades en un día, el total de actividades por tipo, y como se distribuyen las actividades por mes y hora del día. 

Esta es la Tarea 3.

---

## Estructura del proyecto

```
proyecto/
├── flask_app/
│   ├── database/
│   │   ├── create_user.sql
│   │   ├── db.py
│   │   ├── region-comuna.sql
│   │   ├── tabla-comentario.sql # Aquí se agregó la tabla de comentarios para la Tarea 3
│   │   └── tarea2.sql
│   ├── static/
│   │   ├── css/
│   │   │   ├── estadisticas.css
│   │   │   ├── formulario.css
│   │   │   ├── listado.css
│   │   │   └── styles.css
│   │   ├── js/
│   │   │   ├── listado.js
│   │   │   ├── region_comuna.js
│   │   │   └── validaciones.js
│   │   ├── svg/
│   │   └── uploads/
│   │       └── [imágenes de ejemplo]
│   ├── templates/
│   │   ├── detalle.html       # Detalle de actividades
│   │   ├── estadisticas.html  # Página con gráficos (estáticos)
│   │   ├── index.html         # Portada del sitio
│   │   ├── informar.html      # Formulario para ingresar nueva actividad
│   │   └── listado.html       # Listado de actividades
│   ├── utils/
│   │   └── validations.py
│   ├── app.py                 # Aplicación creada en Flask
│   ├── region_comuna.json     # Mismo contenido que region_comuna.js pero en formato JSON
│   └── requirements.txt       # Para instalar usar "pip install -r requirements.txt"
└── README.md
```

---

## Cómo usar

1. Posicionar una terminal en la carpeta "flask_app".
2. Idealmente crear un ambiente virtual con python ("python -m venv venv").
3. Ejecutar ambiente virtual (En Windows: venv/Scripts/activate || En Mac o Linux: source ./venv/bin/activate).
4. Instalar requisitos en la consola con "pip install -r requirements.txt".
5. Correr los sql para crear la base de datos:
   - **tarea2.sql**: Crea la base de datos.
   - **create_user.sql**: Crea el usuario para acceder a la base de datos.
   - **region-comuna.sql**: Inserta todas las regiones y comunas de Chile a la base de datos.
6. En la consola escribir "flask run" para ejecutar el proyecto e ir a la dirección donde corre (http://127.0.0.1:5000).
7. Desde la portada, puedes ver las últimas 5 actividades agregadas a la base de datos. Además hay un menú arriba donde puedes dirigirte a las siguientes páginas:
   - **Agregar una actividad** mediante un formulario con validaciones.
   - **Ver el listado de todas las actividades** con detalles y fotos.
   - **Visualizar estadísticas** (gráficos como imágenes estáticas).

---

## Decisiones tomadas

- Al igual que en la Tarea 1 y 2, para los cambios en los CSS (para los comentarios de las actividades en esta tarea en específico) decidí usar ChatGPT para que me diera un diseño rápido y legible (se modificaron para que sean más consistentes entre páginas). También me ayudó a corregir algunos errores (en especial cuando los metí al validador de HTML y CSS).
- Las imágenes siguen siendo las mismas de la tarea 1 y 2, y las usé para testear la subida de actividades a la base de datos (por eso están con sus nombres originales y sin encriptar dentro de static/uploads). Al momento de usarlas, cuando son subidas a la base de datos, los nombres se cambian a un formato más seguro y encriptado, como debería ser.
- Los gráficos en estadísticas toman en cuenta las actividades subidas a la base de datos, por lo tanto para ver como se visualizan los gráficos hay que primero añadir algunas actividades (se recomienda por lo menos 5, con distintos temas y fechas de inicio).
- Los comentarios se validan tanto en el Javascript (frontend) como en app.py (backend). Sin embargo, no se usa el campo "required" en esa parte del html, con el fin de que se muestre un mensaje de error en el formulario usando código de Javascript.

---

## Tecnologías usadas

### Base de datos
- MySQL
### Backend
- Flask
- SQLAlchemy
### Frontend
- HTML5
- CSS3
- JavaScript (Vanilla + AJAX)

---

- Autor: Ignacio Andrés Arros Rodríguez
- Ramo: Desarrollo de Aplicaciones Web.
- Profesor: José Urzúa


