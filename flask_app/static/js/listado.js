const actividades = [
    {
      inicio: "2025-04-10 10:00",
      termino: "2025-04-10 12:00",
      comuna: "Providencia",
      sector: "Parque Bustamante",
      tema: "Yoga al aire libre",
      organizador: "Camila Soto",
      contacto: "X: @camila_soto",
      fotos: ["../static/uploads/yoga1.jpeg", "../static/uploads/yoga2.png", "../static/uploads/yoga3.jpeg"]
    },
    {
      inicio: "2025-04-12 15:00",
      termino: "2025-04-12 18:00",
      comuna: "Ñuñoa",
      sector: "Plaza Ñuñoa",
      tema: "Clase de pintura",
      organizador: "Andrés Rojas",
      contacto: "instagram: @andres_rojas",
      fotos: ["../static/uploads/pintura1.jpg", "../static/uploads/pintura2.jpg"]
    },
    {
      inicio: "2025-04-15 09:00",
      termino: "2025-04-15 11:30",
      comuna: "Las Condes",
      sector: "Parque Araucano",
      tema: "Taller de cerámica",
      organizador: "Lucía Fernández",
      contacto: "X: @lucia_fernandez ; instagram: @lucia_fernandez",
      fotos: ["../static/uploads/ceramica1.jpeg", "../static/uploads/ceramica2.jpg", "../static/uploads/ceramica3.jpg", "../static/uploads/ceramica4.jpg"]
    },
    {
      inicio: "2025-04-18 17:00",
      termino: "2025-04-18 20:00",
      comuna: "La Reina",
      sector: "Casa de la Cultura",
      tema: "Cine al aire libre",
      organizador: "José Ramírez",
      contacto: "whatsapp: +56912345678",
      fotos: ["../static/uploads/cinelibre1.jpg"]
    },
    {
      inicio: "2025-04-22 14:00",
      termino: "2025-04-22 16:00",
      comuna: "Macul",
      sector: "Centro Comunitario",
      tema: "Charla medioambiental",
      organizador: "Daniela López",
      contacto: "tiktok: @daniela_lopez ; instagram: @daniela_lopez",
      fotos: ["../static/uploads/medio1.jpeg", "../static/uploads/medio2.jpeg"]
    }
  ];
  
  let imagenAmpliada = null;
  let tamañoOriginal = {};
  let botonCerrar = null;
  
  function mostrarDetalle(index) {
    const actividad = actividades[index];
    const detalle = document.getElementById("detalle-contenido");
    detalle.innerHTML = `
      <p><strong>Inicio:</strong> ${actividad.inicio}</p>
      <p><strong>Término:</strong> ${actividad.termino}</p>
      <p><strong>Comuna:</strong> ${actividad.comuna}</p>
      <p><strong>Sector:</strong> ${actividad.sector}</p>
      <p><strong>Tema:</strong> ${actividad.tema}</p>
      <p><strong>Organizador:</strong> ${actividad.organizador}</p>
      <p><strong>Contacto:</strong> ${actividad.contacto}</p>
      <p><strong>Total de fotos:</strong> ${actividad.fotos.length}</p>
      <div class="galeria">
        ${actividad.fotos
          .map(
            (src, i) => `
          <div class="foto-contenedor" style="display: inline-block; position: relative;">
            <img id="foto-${i}" src="${src}" width="320" height="240" onclick="ampliarFoto(this)" alt="foto actividad">
          </div>
        `
          )
          .join("")}
      </div>
    `;
    document.getElementById("listado-actividades").style.display = "none";
    document.getElementById("detalle-actividad").style.display = "block";
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
  