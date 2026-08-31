from app import app
from database import agregar_libro, obtener_libro, obtener_libros


def test_inicio():
    cliente = app.test_client()

    respuesta = cliente.get("/")

    assert respuesta.status_code == 200


def test_agregar_libro():
    cliente = app.test_client()

    respuesta = cliente.post(
        "/agregar",
        data={
            "titulo": "Libro de prueba",
            "autor": "Autor de prueba"
        },
        follow_redirects=True
    )

    assert respuesta.status_code == 200


def test_database_agregar_y_leer():
    agregar_libro(
        "1984",
        "George Orwell"
    )

    libros = obtener_libros()

    assert len(libros) == 1
    assert libros[0][1] == "1984"
    assert libros[0][2] == "George Orwell"
