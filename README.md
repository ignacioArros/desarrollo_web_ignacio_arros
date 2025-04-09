# Plataforma de Registro de Actividades

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

## Funcionalidades destacadas

- Formulario validado manualmente con JavaScript (sin validación HTML nativa).
- Menús dinámicos: las comunas cambian según la región seleccionada.
- Agregado progresivo de fotos (máximo 5).
- Confirmación previa antes de enviar actividad.
- Detalles interactivos en el listado: permite ampliar imágenes.

---

## Tecnologías usadas

- HTML5
- CSS3
- JavaScript (Vanilla)

---

- Autor: Ignacio Andrés Arros Rodríguez
- Ramo: Desarrollo de Aplicaciones Web.
- Profesor: José Urzúa


