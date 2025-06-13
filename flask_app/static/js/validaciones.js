// Función para mostrar/ocultar campos según checkbox
function revisaCheck(checkbox) {
  const input = document.getElementById(checkbox.value + "-id");
  if (checkbox.checked) {
    input.style.display = "inline-block";
  } else {
    input.style.display = "none";
    input.value = "";
  }
}

document.addEventListener("DOMContentLoaded", () => {
    const regionSelect = document.getElementById("region");
    const comunaSelect = document.getElementById("comuna");
    const form = document.getElementById("actividad-form");
    const confirmBox = document.getElementById("confirmacion");
    const graciasBox = document.getElementById("gracias");
    const btnIniciar = document.getElementById("iniciar-confirmacion");
    const btnConfirmar = document.getElementById("confirmar");
    const btnCancelar = document.getElementById("cancelar");
    const fotoContainer = document.getElementById("foto-container");
    const agregarFotoBtn = document.getElementById("agregar-foto");
    const temaSelect = document.getElementById("tema");
    const temaExtra = document.getElementById("tema-extra");

    function obtenerTemasSeleccionados() {
        return Array.from(document.querySelectorAll("input[name='tema']:checked")).map(cb => cb.value);
    }

    // Cambiar comunas al seleccionar región
    regionSelect.addEventListener("change", (e) => {
      comunaSelect.innerHTML = '<option value="">Seleccione una comuna</option>';
      const regionId = parseInt(e.target.value);
      const selectedRegion = regionesYComunas.find(r => r.id === regionId);
      if (selectedRegion && selectedRegion.comunas) {
        selectedRegion.comunas.forEach(comuna => {
          const option = document.createElement("option");
          option.value = comuna.id;
          option.textContent = comuna.nombre;
          comunaSelect.appendChild(option);
        });
      }
    });

    // Formatear fecha
    const formatDate = (date) => {
      const year = date.getFullYear();
      const month = ('0' + (date.getMonth() + 1)).slice(-2);
      const day = ('0' + date.getDate()).slice(-2);
      const hours = ('0' + date.getHours()).slice(-2);
      const minutes = ('0' + date.getMinutes()).slice(-2);
      return `${year}-${month}-${day}T${hours}:${minutes}`;
    };
  
    // Prellenar fecha actual en inicio y término (3h después)
    const ahora = new Date();
    const tresHorasDespues = new Date(ahora.getTime() + 3 * 60 * 60 * 1000);
    document.getElementById("inicio").value = formatDate(ahora);
    document.getElementById("termino").value = formatDate(tresHorasDespues);
  
    // Manejo agregar más fotos
    agregarFotoBtn.addEventListener("click", () => {
      const currentFiles = fotoContainer.querySelectorAll("input[type='file']").length;
      if (currentFiles < 5) {
        const newInput = document.createElement("input");
        newInput.type = "file";
        newInput.name = "fotos";
        newInput.accept = "image/*";
        fotoContainer.appendChild(newInput);
      } else {
        alert("Solo se permiten hasta 5 fotos.");
      }
    });

    btnIniciar.addEventListener("click", function() {
        // --- VALIDACIONES ---
        const region = regionSelect.value;
        const comuna = comunaSelect.value;
        const sector = document.getElementById("sector").value;
        const nombre = document.getElementById("nombre").value;
        const email = document.getElementById("email").value;
        const telefono = document.getElementById("telefono").value;
        const inicioVal = document.getElementById("inicio").value;
        const terminoVal = document.getElementById("termino").value;
        const temaOtro = temaExtra.querySelector("input");
        const fotos = fotoContainer.querySelectorAll("input[type='file']");

        if (!region) return alert("Debe seleccionar una región.");
        if (!comuna) return alert("Debe seleccionar una comuna.");
        if (sector.length > 100) return alert("El sector no puede tener más de 100 caracteres.");
        if (!nombre || nombre.length > 200) return alert("Debe ingresar un nombre (máximo 200 caracteres).");

        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!email || !emailRegex.test(email) || email.length > 100)
            return alert("Debe ingresar un email válido (máximo 100 caracteres).");

        const telRegex = /^\+\d{3}\.\d{8}$/;
        if (telefono && !telRegex.test(telefono))
            return alert("El teléfono debe tener formato +NNN.NNNNNNNN");

        const redes = ["WhatsApp", "Instagram", "Telegram", "X", "TikTok", "Otro"];
        const seleccionadas = redes.filter(r => document.querySelector(`input[value='${r}']`).checked);

        if (seleccionadas.length > 5) return alert("Puedes seleccionar hasta 5 redes sociales.");
        for (const red of seleccionadas) {
            const input = document.getElementById(red + "-id");
            if (!input || input.value.length < 4 || input.value.length > 50)
                return alert(`El campo para ${red} debe tener entre 4 y 50 caracteres.`);
        }

        if (!inicioVal) return alert("Debe ingresar la fecha de inicio.");
        if (terminoVal && new Date(terminoVal) <= new Date(inicioVal)) return alert("La fecha de término debe ser posterior a la de inicio.");

        const temas = obtenerTemasSeleccionados();

        if (temas.length === 0) return alert("Debe seleccionar al menos un tema.");
        if (temas.includes("otro")) {
          if (!temaOtro || temaOtro.value.length < 3 || temaOtro.value.length > 15) return alert("El tema debe tener entre 3 y 15 caracteres.");
        }

        let alMenosUnaSeleccionada = false;
        fotos.forEach(input => {
            if (input.files.length > 0) alMenosUnaSeleccionada = true;
        });
        if (!alMenosUnaSeleccionada) return alert("Debe seleccionar al menos una foto.");

        // Si todo está bien, mostrar confirmación
        form.style.display = "none";
        confirmBox.style.display = "block";
    });
  
    btnConfirmar.addEventListener("click", function() {
      confirmBox.style.display = "none";
      form.submit();
      graciasBox.style.display = "block";
    });
  
    btnCancelar.addEventListener("click", () => {
      confirmBox.style.display = "none";
      form.style.display = "block";
    });
    
    // Mostrar/ocultar input para "otro"
    const temaOtroCheckbox = document.getElementById("tema-otro-checkbox");

    if (temaOtroCheckbox) {
        temaOtroCheckbox.addEventListener("change", function() {
            temaExtra.innerHTML = "";
            if (this.checked) {
                const input = document.createElement("input");
                input.type = "text";
                input.name = "tema_otro";
                input.placeholder = "Especifique el tema";
                input.minLength = 3;
                input.maxLength = 15;
                temaExtra.appendChild(input);
            }
        });
    }
});