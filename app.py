import os

from flask import Flask, flash, redirect, render_template, request, url_for


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key-change-me")


class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = os.environ.get("SECRET_KEY")


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}


def get_config():
    env_name = os.environ.get("FLASK_ENV", "development")
    selected = config.get(env_name, config["development"])

    if env_name == "production" and not selected.SECRET_KEY:
        raise RuntimeError("SECRET_KEY must be set for production")

    return selected


app = Flask(__name__)
app.config.from_object(get_config())

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

    titulo = request.form.get("titulo", "").strip()
    autor = request.form.get("autor", "").strip()

    if not titulo or not autor:
        flash("⚠️ El título y el autor son obligatorios.")
        return redirect(url_for("inicio"))

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
    titulo = request.form.get("titulo", "").strip()
    autor = request.form.get("autor", "").strip()
    if not titulo or not autor:
        flash("⚠️ El título y el autor son obligatorios.")
        return redirect(url_for("editar", libro_id=libro_id))
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
    app.run(debug=app.config["DEBUG"])
