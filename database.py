import os
import sqlite3

DB_PATH = os.environ.get(
    "DB_PATH",
    os.path.join(os.path.dirname(__file__), "biblioteca.db"),
)


def _get_connection():
    return sqlite3.connect(DB_PATH)


def init_db():
    with _get_connection() as conexion:
        cursor = conexion.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS libros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                autor TEXT NOT NULL
            )
            """
        )
        conexion.commit()


init_db()


def obtener_libros():
    with _get_connection() as conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT id, titulo, autor FROM libros ORDER BY id DESC")
        return cursor.fetchall()


def agregar_libro(titulo, autor):
    with _get_connection() as conexion:
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO libros (titulo, autor) VALUES (?, ?)",
            (titulo, autor),
        )
        conexion.commit()


def obtener_libro(libro_id):
    with _get_connection() as conexion:
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT id, titulo, autor FROM libros WHERE id = ?",
            (libro_id,),
        )
        return cursor.fetchone()


def actualizar_libro(libro_id, titulo, autor):
    with _get_connection() as conexion:
        cursor = conexion.cursor()
        cursor.execute(
            "UPDATE libros SET titulo = ?, autor = ? WHERE id = ?",
            (titulo, autor, libro_id),
        )
        conexion.commit()


def eliminar_libro(libro_id):
    with _get_connection() as conexion:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM libros WHERE id = ?", (libro_id,))
        conexion.commit()


def buscar_libros(query):
    """Buscar libros por título o autor (case-insensitive)."""
    with _get_connection() as conexion:
        cursor = conexion.cursor()

        patron = f"%{query}%"

        cursor.execute(
            "SELECT id, titulo, autor FROM libros "
            "WHERE titulo LIKE ? COLLATE NOCASE OR autor LIKE ? COLLATE NOCASE "
            "ORDER BY id DESC",
            (patron, patron),
        )
        return cursor.fetchall()
