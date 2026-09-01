import os
import sqlite3

import pytest

from app import app
from database import agregar_libro, obtener_libro, init_db


@pytest.fixture(autouse=True)
def preparar_base_de_datos():
    init_db()

    yield

    conexion = sqlite3.connect(os.environ["DB_PATH"])

    cursor = conexion.cursor()

    cursor.execute("DELETE FROM libros")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='libros'")

    conexion.commit()
    conexion.close()


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

    libro = obtener_libro(1)

    assert libro is not None
    assert libro[1] == "1984"
    assert libro[2] == "George Orwell"


def test_actualizar_libro():
    agregar_libro(
        "Libro original",
        "Autor original"
    )

    cliente = app.test_client()

    respuesta = cliente.post(
        "/actualizar/1",
        data={
            "titulo": "Libro actualizado",
            "autor": "Autor actualizado"
        },
        follow_redirects=True
    )

    assert respuesta.status_code == 200

    libro_actualizado = obtener_libro(1)

    assert libro_actualizado[1] == "Libro actualizado"
    assert libro_actualizado[2] == "Autor actualizado"
