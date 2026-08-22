function confirmarEliminacion() {
    return confirm("¿Seguro que quieres eliminar este libro?");
}

setTimeout(function () {
    const mensaje = document.getElementById("flash-message");
    if (mensaje) {
        mensaje.remove();
    }
}, 3000);
