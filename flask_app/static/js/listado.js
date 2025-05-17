let imagenAmpliada = null;
let tamañoOriginal = {};
let botonCerrar = null;

function mostrarDetalle(actividadId) {
      fetch("{{ url_for('detalle_actividad', actividad_id=0) }}".replace('0', actividadId))
          .then(response => response.text())
          .then(html => {
              document.getElementById("detalle-contenido").innerHTML = html;
              document.getElementById("listado-actividades").style.display = "none";
              document.getElementById("detalle-actividad").style.display = "block";
          });
}

function volverListado() {
  document.getElementById("detalle-actividad").style.display = "none";
  document.getElementById("listado-actividades").style.display = "block";
}

function ampliarFoto(img) {
  if (imagenAmpliada) return;
  tamañoOriginal = { width: static/uploads.width, height: static/uploads.height };
  imagenAmpliada = static/uploads;
  img.width = 800;
  img.height = 600;

  const contenedor = static/uploads.parentElement;
  botonCerrar = document.createElement("button");
  botonCerrar.textContent = "Cerrar";
  botonCerrar.onclick = cerrarFoto;
  botonCerrar.style.position = "absolute";
  botonCerrar.style.top = "5px";
  botonCerrar.style.right = "5px";
  contenedor.appendChild(botonCerrar);
}

function cerrarFoto() {
  if (!imagenAmpliada) return;
  imagenAmpliada.width = tamañoOriginal.width;
  imagenAmpliada.height = tamañoOriginal.height;
  if (botonCerrar && botonCerrar.parentElement) {
    botonCerrar.parentElement.removeChild(botonCerrar);
  }
  imagenAmpliada = null;
  botonCerrar = null;
}

// Opcional: función para ampliar fotos si lo deseas
function cerrarModal() {
  document.getElementById("modal-foto").style.display = "none";
}
  