// Función para cargar y mostrar el archivo CSV
function loadCSV() {
    // Ruta al archivo CSV
    const archivoCSV = 'DR.csv';

    // Realiza una solicitud HTTP para cargar el archivo CSV
    fetch(archivoCSV)
        // Convierte la respuesta a texto
        .then(response => response.text())
        // Muestra el archivo CSV en una tabla
        .then(data => {
            // Divide el archivo CSV en filas, toma la primera fila como encabezado
            const rows = data.split('\n');
            // Obtiene la tabla
            const table = document.getElementById('csvTable');

            // Crea las filas y celdas de la tabla
            for (let i = 0; i < rows.length; i++) {
                const row = document.createElement('tr');
                const cells = rows[i].split(',');

                for (let j = 0; j < cells.length; j++) {
                    const cell = document.createElement(i === 0 ? 'th' : 'td');
                    cell.textContent = cells[j];
                    row.appendChild(cell);
                }

                table.appendChild(row);
            }
        })
        .catch(error => console.error('Error al cargar el archivo CSV:', error));
}

// Cargar el archivo CSV al cargar la página
window.addEventListener('load', loadCSV);
