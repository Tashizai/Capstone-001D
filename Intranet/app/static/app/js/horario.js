document.addEventListener('DOMContentLoaded', function() {
    const editarBtn = document.getElementById('editar-horario');
    const guardarBtn = document.getElementById('guardar-horario');
    const tablaHorarios = document.getElementById('tabla-horarios');
    const mensajeGuardado = document.getElementById('mensaje-guardado');

    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    // Habilitar la edición
    editarBtn.addEventListener('click', function() {
        const celdas = tablaHorarios.querySelectorAll('[contenteditable="false"]');
        celdas.forEach(celda => {
            celda.setAttribute('contenteditable', 'true');
            celda.style.backgroundColor = "#f0f0f0"; // Indicar que está editable
        });
        guardarBtn.classList.remove('hidden');
    });

    // Guardar los cambios
    guardarBtn.addEventListener('click', function(event) {
        event.preventDefault();

        const datosHorario = [];
        const filas = tablaHorarios.querySelectorAll('tr');
        filas.forEach((fila) => {
            const celdas = fila.querySelectorAll('td');
            celdas.forEach((celda) => {
                const dia = celda.getAttribute('data-dia');
                const hora = celda.getAttribute('data-hora');
                const asignatura = celda.innerText.trim();

                // Solo agrega si tiene asignatura
                if (asignatura) {
                    datosHorario.push({
                        'dia': dia,
                        'hora': hora,
                        'asignatura': asignatura,
                        'clase': ""  // Puedes añadir un campo para el curso si es necesario
                    });
                }
            });
        });

        // Verificar los datos antes de enviarlos
        console.log(datosHorario);

        fetch('/guardar-horario/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({
                horario: datosHorario  // Enviar los datos al backend
            })
        })
        .then(response => {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error('Error al guardar los cambios');
            }
        })
        .then(data => {
            mensajeGuardado.classList.remove('hidden');
            setTimeout(() => {
                mensajeGuardado.classList.add('hidden');
            }, 3000);
        })
        .catch(error => {
            console.error('Error al guardar el horario:', error);
        });
    });
});
