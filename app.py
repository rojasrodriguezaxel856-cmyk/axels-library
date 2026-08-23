from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
import os
app.secret_key = os.environ.get('SECRET_KEY', 'dev')

from database import (
    obtener_libros,
    agregar_libro,
    obtener_libro,
    actualizar_libro,
    eliminar_libro,
    buscar_libros,
)

@app.route("/")
def inicio():

    buscar = request.args.get("buscar", "").strip()

    if buscar:
        libros = buscar_libros(buscar)
    else:
        libros = obtener_libros()

    return render_template("index.html", libros=libros, buscar=buscar)


@app.route("/agregar", methods=["POST"])
def agregar():

    titulo = request.form.get("titulo")
    autor = request.form.get("autor")

    if not titulo or not autor:
        # Si faltan datos, no intentar insertar; redirigir a la vista principal
        return redirect(url_for('inicio'))

    agregar_libro(titulo, autor)

    # Mensaje flash para el usuario
    flash("✅ Libro agregado correctamente.")

    # Usar url_for para evitar rutas hardcodeadas
    return redirect(url_for('inicio'))


@app.route("/editar/<int:libro_id>")
def editar(libro_id):
    libro = obtener_libro(libro_id)
    if not libro:
        # Si el libro no existe, volver al listado principal
        return redirect(url_for('inicio'))
    return render_template("editar.html", libro=libro)


@app.route("/actualizar/<int:libro_id>", methods=["POST"])
def actualizar(libro_id):
    titulo = request.form.get("titulo")
    autor = request.form.get("autor")
    if not titulo or not autor:
        # Validación mínima: si falta dato, volver al formulario de edición
        return redirect(url_for('editar', libro_id=libro_id))
    actualizar_libro(libro_id, titulo, autor)
    # Mensaje flash para el usuario
    flash("✅ Libro actualizado correctamente.")
    # Redirigir a la página principal usando url_for en vez de ruta hardcodeada
    return redirect(url_for('inicio'))


@app.route("/eliminar/<int:libro_id>", methods=["POST"])
def eliminar(libro_id):

    eliminar_libro(libro_id)

    # Mensaje flash para el usuario
    flash("🗑️ Libro eliminado correctamente.")

    return redirect(url_for("inicio"))


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)