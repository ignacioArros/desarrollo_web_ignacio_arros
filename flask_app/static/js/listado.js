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

document.addEventListener("DOMContentLoaded", function() {
  asociarEventosGaleria();
});
