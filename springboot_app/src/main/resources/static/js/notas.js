function cargarActividades() {
    fetch('/api/actividades/finalizadas')
        .then(res => res.json())
        .then(data => {
            const tbody = document.getElementById('actividades-list');
            tbody.innerHTML = '';
            data.forEach(act => {
                // Si tienes el campo tema como lista, ajústalo aquí
                let tema = act.tema || '-';
                if (Array.isArray(act.temas)) {
                    tema = act.temas.map(t => t.tema === 'otro' && t.glosa_otro ? t.tema + ' (' + t.glosa_otro + ')' : t.tema).join(', ');
                }
                const tr = document.createElement('tr');
                tr.innerHTML = `
                    <td>${act.id}</td>
                    <td>${act.diaHoraInicio ? act.diaHoraInicio.replace('T', ' ').substring(0, 16) : '-'}</td>
                    <td>${act.sector || '-'}</td>
                    <td>${act.nombre}</td>
                    <td>${tema}</td>
                    <td class="nota">${act.promedioNotas || '-'}</td>
                    <td><button onclick="evaluar(${act.id}, this)">Evaluar</button></td>
                `;
                tbody.appendChild(tr);
            });
        });
}

function evaluar(actividadId, btn) {
    const nota = prompt("Ingrese una nota entre 1 y 7:");
    const valor = parseInt(nota);
    if (isNaN(valor) || valor < 1 || valor > 7) {
        alert("Nota inválida");
        return;
    }
    fetch('/api/notas', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({actividadId: actividadId, nota: valor})
    })
    .then(res => res.ok ? res.json() : Promise.reject(res))
    .then(promedio => {
        btn.closest('tr').querySelector('.nota').textContent = promedio;
    })
    .catch(() => alert("Error al guardar la nota"));
}

cargarActividades();