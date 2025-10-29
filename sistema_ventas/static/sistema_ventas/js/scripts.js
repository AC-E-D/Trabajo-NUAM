// Confirmación antes de eliminar un producto
document.addEventListener('DOMContentLoaded', function() {
    const deleteLinks = document.querySelectorAll('.delete-link');

    deleteLinks.forEach(function(link) {
        link.addEventListener('click', function(e) {
            const confirmDelete = confirm("¿Estás seguro de que deseas eliminar este producto?");
            if (!confirmDelete) {
                e.preventDefault(); // Cancela la acción si el usuario no confirma
            }
        });
    });

    // Validación simple de formularios
    const forms = document.querySelectorAll('.validate-form');
    forms.forEach(function(form) {
        form.addEventListener('submit', function(e) {
            let valid = true;
            const nombre = form.querySelector('input[name="nombre"]').value.trim();
            const precio = form.querySelector('input[name="precio"]').value.trim();
            const stock = form.querySelector('input[name="stock"]').value.trim();

            if (nombre === "") {
                alert("El nombre del producto es obligatorio");
                valid = false;
            }
            if (precio === "" || isNaN(precio) || Number(precio) <= 0) {
                alert("Ingrese un precio válido");
                valid = false;
            }
            if (stock === "" || isNaN(stock) || Number(stock) < 0) {
                alert("Ingrese un stock válido");
                valid = false;
            }

            if (!valid) {
                e.preventDefault(); // Cancela envío si hay errores
            }
        });
    });
});
