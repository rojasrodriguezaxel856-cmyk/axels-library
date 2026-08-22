import sqlite3

conexion = sqlite3.connect("biblioteca.db")
cursor = conexion.cursor()

cursor.execute("SELECT * FROM libros")
libros = cursor.fetchall()
for libro in libros:
    print(libro)

conexion.close()