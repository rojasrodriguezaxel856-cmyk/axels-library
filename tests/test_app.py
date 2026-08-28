from app import app


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
