# Plataforma de Registro de Actividades - Tarea 4 - Desarrollo Web

Este proyecto es una aplicación web desarrollada para el curso CC5002 - Desarrollo de Aplicaciones Web, de la carrera de Ingeniería Civil en Computación de la Universidad de Chile. Está dividida en dos aplicaciones diferentes (una hecha con Flask y otra con Spring Boot). 

La aplicación de Flask posee las siguientes funcionalidades:

- Permite registrar, guardar, listar y visualizar actividades realizadas en distintas comunas y regiones, con detalles sobre el autor, el tema y fotografías. 

- Cada actividad posee una sección de comentarios (que son guardados en relación con la actividad).

- Hay estadísticas funcionales que permiten ver las actividades registradas, ya sea por la cantidad de actividades en un día, el total de actividades por tipo, y como se distribuyen las actividades por mes y hora del día. 

La aplicación de Spring Boot posee la siguiente funcionalidad:

- Permite evaluar las actividades que ya han finalizado (fecha de término anterior a la actual) con una nota del 1 al 7.

Esta es la Tarea 4.

---

## Estructura del proyecto

```
proyecto/
├── flask_app/                   # Aplicación hecha con Flask
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
├── springboot_app/            # Aplicación hecha con Spring Boot
│   ├── src/
│   │   ├── main
│   │   │   ├── java/springboot_app/springboot_app
│   │   │   │   ├── controllers
│   │   │   │   │   ├── ActividadController.java        # Controlador para actividades
│   │   │   │   │   ├── NotaController.java             # Controlador para notas
│   │   │   │   │   └── VistaController.java            # Controlador para vista (HTML)
│   │   │   │   ├── dto
│   │   │   │   │   └── ActividadDto.java               # Data Transfer Object para actividades
│   │   │   │   ├── models
│   │   │   │   │   ├── Actividad.java                  # Modelo para actividades
│   │   │   │   │   ├── ActividadTema.java              # Modelo para temas de actividades
│   │   │   │   │   └── Nota.java                       # Modelo para notas
│   │   │   │   ├── repositories
│   │   │   │   │   ├── ActividadRepository.java        # Repositorio de actividades
│   │   │   │   │   ├── ActividadTemaRepository.java    # Repositorio de temas de actividades
│   │   │   │   │   └── NotaRepository.java             # Repositorio de notas
│   │   │   │   ├── services
│   │   │   │   │   ├── ActividadService.java           # Servicio de actividades
│   │   │   │   │   └── NotaService.java                # Servicio de notas
│   │   │   │   └── SpringbootAppApplication.java       # Manejo de aplicación de Spring Boot 
│   │   │   └── resources
│   │   │   │   ├── static
│   │   │   │   │   ├── css
│   │   │   │   │   │   └── styles.css
│   │   │   │   │   └── js
│   │   │   │   │       └── notas.js
│   │   │   │   ├── templates
│   │   │   │   │   └── notas.html                      # Página de evaluación de actividades
│   │   │   │   └── application.properties              # Configuración de app de Spring Boot
│   │   └── test/java/springboot_app/springboot_app
│   │       └── SpringbootAppApplicationTests.java      # (No hay tests aquí)
│   └── ...                    # Otras cosas configuradas automáticamente por Spring Boot
└── README.md
```

---

## Cómo usar

### Aplicación de Flask

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

### Aplicación de Spring Boot

**NOTA:** Esta aplicación solo tiene funcionalidad si es que ya se han ingresado actividades a la base de datos local (mediante la aplicación de Flask o manualmente).

1. Asegurarse de tener la última versión de Spring Boot (3.5.3), JPA y al menos tener Java versión 17 instalado.
2. Usando un IDE como VSCode, abrir el archivo "SpringbootAppApplication.java".
3. Clickear el botón "run" en la esquina superior derecha.
4. (Método alternativo): Si se tiene instalado las extensiones de Spring Boot en VSCode (en específico Spring Boot Dashboard), se puede iniciar clickeando el submenú de Spring Boot y clickear el boton de "Run".
5. El proyecto debería abrirse en la dirección localhost en el puerto 8080 (http://127.0.0.1:8080, o también, http://localhost:8080).
6. Al ir a esa dirección en su navegador, debería encontrarse con una página que tenga un listado de actividades que ya han terminado de realizarse (fecha de término de la actividad es menor que la actual). En ella se puede evaluar la actividad con una nota del 1 al 7.
---

## Decisiones tomadas

- Se usó el mismo CSS principal en la app de Spring Boot que en la app de Flask, por lo que se hizo el nuevo HTML (notas.html) en torno a lo que ya estaba configurado (similar a lo que estaba en index.html).
- Las imágenes siguen siendo las mismas de las tareas anteriores, y las usé para testear la subida de actividades a la base de datos (por eso están con sus nombres originales y sin encriptar dentro de static/uploads). Al momento de usarlas, cuando son subidas a la base de datos, los nombres se cambian a un formato más seguro y encriptado, como debería ser.
- Aunque instalé Thymeleaf en conjunto con Spring Boot tal como se vió en las auxiliares 9 y 10, no lo utilicé en ningún momento de la tarea, principalmente porque no encontré que lo necesitara para realizarla.
- Aún cuando no se vio los DTOs en auxiliares, yo los he usado anteriormente para mi práctica 2 (donde tuve que usar DTOs en Spring Boot). Por eso es que decidí incorporar uno en esta tarea (ActividadDto) para que el código estuviera mejor organizado y los datos se transfirieran de una mejor forma.

---

## Tecnologías usadas

### Base de datos
- MySQL
### Backend
- Flask
- SQLAlchemy
- Spring Boot
- JPA
### Frontend
- HTML5
- CSS3
- JavaScript (Vanilla + AJAX)

---

- Autor: Ignacio Andrés Arros Rodríguez
- Ramo: Desarrollo de Aplicaciones Web.
- Profesor: José Urzúa


