import sqlite3
import os

# Ruta absoluta al archivo de base de datos dentro del proyecto
DB_PATH = os.path.join(os.path.dirname(__file__), "biblioteca.db")

# Inicializar la base de datos y la tabla si no existen
def init_db():
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS libros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL
    )
    """)
    conexion.commit()
    conexion.close()

init_db()


def obtener_libros():
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()

    cursor.execute("SELECT id, titulo, autor FROM libros ORDER BY id DESC")

    libros = cursor.fetchall()

    conexion.close()

    return libros


def agregar_libro(titulo, autor):
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO libros (titulo, autor) VALUES (?, ?)", (titulo, autor))
    conexion.commit()
    conexion.close()


def obtener_libro(id):
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    cursor.execute("SELECT id, titulo, autor FROM libros WHERE id = ?", (id,))
    libro = cursor.fetchone()
    conexion.close()
    return libro


def actualizar_libro(id, titulo, autor):
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    cursor.execute("UPDATE libros SET titulo = ?, autor = ? WHERE id = ?", (titulo, autor, id))
    conexion.commit()
    conexion.close()


def eliminar_libro(libro_id):
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()

    cursor.execute(
        "DELETE FROM libros WHERE id = ?",
        (libro_id,)
    )

    conexion.commit()
    conexion.close()


def buscar_libros(query):
    """Buscar libros por título o autor (case-insensitive).
    Usa parámetros para evitar inyección y COLLATE NOCASE para ignorar mayúsculas.
    """
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()

    patrón = f"%{query}%"

    cursor.execute(
        "SELECT id, titulo, autor FROM libros "
        "WHERE titulo LIKE ? COLLATE NOCASE OR autor LIKE ? COLLATE NOCASE "
        "ORDER BY id DESC",
        (patrón, patrón),
    )

    libros = cursor.fetchall()
    conexion.close()
    return libros
