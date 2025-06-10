let imagenAmpliada = null;
let botonCerrar = null;

function mostrarDetalle(actividadId) {
    fetch(detalleActividadUrl.replace('0', actividadId))
        .then(response => response.text())
        .then(html => {
            document.getElementById("detalle-contenido").innerHTML = html;
            document.getElementById("listado-actividades").style.display = "none";
            document.getElementById("detalle-actividad").style.display = "block";
            asociarEventosGaleria();
            inicializarComentarios(actividadId);
        });
}

function volverListado() {
  document.getElementById("detalle-actividad").style.display = "none";
  document.getElementById("listado-actividades").style.display = "block";
}

function ampliarFoto(img) {
  if (img.classList.contains("ampliada")) {
    cerrarFoto();
    return;
  }
  if (imagenAmpliada) {
    cerrarFoto();
  }
  imagenAmpliada = img;
  img.classList.add("ampliada");

  botonCerrar = document.createElement("button");
  botonCerrar.textContent = "Cerrar";
  botonCerrar.onclick = cerrarFoto;
  botonCerrar.className = "boton-cerrar-foto";
  img.parentElement.appendChild(botonCerrar);
}

function cerrarFoto() {
  if (!imagenAmpliada) return;
  imagenAmpliada.classList.remove("ampliada");
  if (botonCerrar && botonCerrar.parentElement) {
    botonCerrar.parentElement.removeChild(botonCerrar);
  }
  imagenAmpliada = null;
  botonCerrar = null;
}

function asociarEventosGaleria() {
  document.querySelectorAll('.galeria img').forEach(img => {
    img.onclick = function() { ampliarFoto(this); };
  });
}

function inicializarComentarios(actividadId) {
    const form = document.getElementById('form-comentario');
    const erroresDiv = document.getElementById('comentario-errores');
    const comentariosLista = document.getElementById('comentarios-lista');
    if (!form) return; // Si no hay formulario, salir

    function cargarComentarios() {
        fetch(`/api/comentarios/${actividadId}`)
            .then(res => res.json())
            .then(comentarios => {
                comentariosLista.innerHTML = "";
                if (comentarios.length === 0) {
                    const p = document.createElement("p");
                    p.textContent = "No hay comentarios aún.";
                    comentariosLista.appendChild(p);
                } else {
                    comentarios.forEach(c => {
                        const div = document.createElement("div");
                        div.className = "comentario";
                        
                        const fecha = document.createElement("span");
                        fecha.className = "fecha-comentario";
                        fecha.textContent = c.fecha;

                        const nombre = document.createElement("strong");
                        nombre.textContent = c.nombre;

                        const texto = document.createElement("span");
                        texto.className = "texto-comentario";
                        texto.textContent = c.texto;

                        div.appendChild(nombre);
                        div.appendChild(fecha);
                        div.appendChild(texto);

                        comentariosLista.appendChild(div);
                    });
                }
            })
            .catch(() => {
                comentariosLista.innerHTML = "<p style='color:red;'>No se pudieron cargar los comentarios.</p>";
            });
    }

    form.addEventListener('submit', function(e) {
        e.preventDefault();
        erroresDiv.textContent = '';
        const nombre = form.nombre.value.trim();
        const texto = form.texto.value.trim();
        let errores = [];
        if (nombre.length < 3 || nombre.length > 80) {
            errores.push("El nombre debe tener entre 3 y 80 caracteres.");
        }
        if (texto.length < 5) {
            errores.push("El comentario debe tener al menos 5 caracteres.");
        }
        if (errores.length > 0) {
            erroresDiv.textContent = errores.join(" ");
            return;
        }
        fetch(`/api/comentarios/${actividadId}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ nombre, texto })
        })
        .then(res => {
            if (!res.ok) return res.json().then(data => { throw data; });
            return res.json();
        })
        .then(() => {
            form.reset();
            erroresDiv.textContent = "¡Comentario agregado!";
            cargarComentarios(); // Recarga los comentarios después de agregar uno nuevo
            setTimeout(() => { erroresDiv.textContent = ""; }, 2000);
        })
        .catch(data => {
            erroresDiv.textContent = (data.errores || ["Error al agregar comentario"]).join(" ");
            setTimeout(() => { erroresDiv.textContent = ""; }, 2000);
        });
    });

    cargarComentarios(); // Carga los comentarios al inicializar
}

document.addEventListener("DOMContentLoaded", function() {
  asociarEventosGaleria();
});
