// static/js/custom-script.js

// Función para obtener todos los checkboxes de los clientes
function getAllClientCheckboxes() {
  return document.querySelectorAll('input[name="selected_clients"]');
}

// Función para manejar el evento de cambio en el checkbox "select-all"
function handleSelectAllCheckbox() {
  const selectAllCheckbox = document.getElementById('select-all');
  const clientCheckboxes = getAllClientCheckboxes();

  for (const checkbox of clientCheckboxes) {
    checkbox.checked = selectAllCheckbox.checked;
  }
}

// Función para eliminar los clientes seleccionados
function deleteSelectedClients() {
  const clientCheckboxes = getAllClientCheckboxes();
  const selectedClientIds = [];

  for (const checkbox of clientCheckboxes) {
    if (checkbox.checked) {
      selectedClientIds.push(checkbox.value);
    }
  }
}

// Event listener para el checkbox "select-all"
document.getElementById('select-all').addEventListener('change', handleSelectAllCheckbox);

// Event listener para el botón "Eliminar seleccionados"
document.querySelector('button.btn.btn-danger').addEventListener('click', deleteSelectedClients);


function checkAndDelete() {
  // Obtener la referencia a todos los elementos seleccionados (checkboxes)
  var elementosSeleccionados = document.querySelectorAll('input[type="checkbox"]:checked');

  if (elementosSeleccionados.length === 0) {
    // Si no hay elementos seleccionados, mostrar un mensaje de advertencia
    const myModal2 = new bootstrap.Modal(document.getElementById('errorModal'));
    myModal2.show();
  } else {
    // Si hay elementos seleccionados, mostrar el mensaje de confirmación
    const myModal = new bootstrap.Modal(document.getElementById('confirmModal'));
    myModal.show();
  }
}




