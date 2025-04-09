# Plataforma de Registro de Actividades - Tarea 1 - Desarrollo Web

Este proyecto es una aplicación web desarrollada para el curso CC5002 - Desarrollo de Aplicaciones Web, de la carrera de Ingeniería Civil en Computación de la Universidad de Chile. Permite registrar (pero no guardar), listar y visualizar actividades realizadas en distintas comunas y regiones, con detalles sobre el autor, el tema y fotografías. Esta es la Tarea 1.

---

## Estructura del proyecto

```
proyecto/
├── css/
│   ├── estadisticas.css
│   ├── formulario.css
│   ├── listado.css
│   └── styles.css
├── html/
│   ├── estadisticas.html    # Página con gráficos (estáticos)
│   ├── index.html           # Portada del sitio
│   ├── informar.html        # Formulario para ingresar nueva actividad
│   └── listado.html         # Listado de actividades
├── img/
│   └── [imágenes de ejemplo]
├── js/
│   ├── listado.js
│   ├── region_comuna.js
│   └── validaciones.js
├── region_comuna.json       # Mismo contenido que region_comuna.js pero en formato JSON
└── README.md
```

---

## Cómo usar

1. Abrir `index.html` en un navegador web (idealmente con la extensión Live Server).
2. Desde la portada, puedes:
   - **Agregar una actividad** mediante un formulario con validaciones.
   - **Ver el listado de 5 actividades** con detalles y fotos.
   - **Visualizar estadísticas** (gráficos como imágenes estáticas).

---

## Decisiones tomadas

- Para los CSS decidí usar ChatGPT para que me diera un diseño rápido que se vea legible (aunque de igual forma los modifiqué para que fueran más consistentes entre páginas). También me ayudó a corregir algunos errores (en especial cuando los metí al validador de HTML y CSS).
- En los HTML decidí no usar ningún required en los inputs y hacer todas las validaciones en el javascript, así cada error sale como alerta en vez de que el HTML lo indique por su cuenta.
- Las imágenes las saqué de internet, generalmente de Wikipedia y de algunos noticieros en línea, espero no infringir derechos de autor porque son placeholder jeje.
- Decidí copiar y pegar todo lo que estaba en el javascript de region_comuna y llevarlo al de validaciones, así lo podía tomar como una constante y no tener que hacer fetch (Ojalá esté bien xd).

---

## Tecnologías usadas

- HTML5
- CSS3
- JavaScript (Vanilla)

---

- Autor: Ignacio Andrés Arros Rodríguez
- Ramo: Desarrollo de Aplicaciones Web.
- Profesor: José Urzúa


