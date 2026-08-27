import os
import sys

ROOT = os.path.dirname(__file__)
DB_PATH = os.path.join(ROOT, 'biblioteca.db')

# Ensure a clean DB
if os.path.exists(DB_PATH):
    os.remove(DB_PATH)

# Import database (this will recreate DB) and app
import database
from app import app

client = app.test_client()

PASSED = 0
FAILED = 0


def expect(cond, msg):
    global PASSED, FAILED
    if cond:
        print('PASS:', msg)
        PASSED += 1
    else:
        print('FAIL:', msg)
        FAILED += 1


# Test A - Add valid book
r = client.post('/agregar', data={'titulo': 'Clean Code', 'autor': 'Robert C. Martin'}, follow_redirects=True)
text = r.data.decode('utf-8')
expect('✅ Libro agregado correctamente.' in text, 'Test A - success flash')
books = database.buscar_libros('Clean Code')
expect(len(books) == 1 and books[0][1] == 'Clean Code', 'Test A - DB contains Clean Code')

# Test B - Empty title
r = client.post('/agregar', data={'titulo': '', 'autor': 'Robert C. Martin'}, follow_redirects=True)
text = r.data.decode('utf-8')
expect('⚠️ El título y el autor son obligatorios.' in text, 'Test B - empty title flash')
# DB should still have only the first book
books_after_b = database.obtener_libros()
expect(len(books_after_b) == 1, 'Test B - DB unchanged')

# Test C - Spaces only
r = client.post('/agregar', data={'titulo': '     ', 'autor': '     '}, follow_redirects=True)
text = r.data.decode('utf-8')
expect('⚠️ El título y el autor son obligatorios.' in text, 'Test C - spaces-only flash')
books_after_c = database.obtener_libros()
expect(len(books_after_c) == 1, 'Test C - DB unchanged')

# Test D - Edit existing book
book_id = books_after_c[0][0]
r = client.post(f'/actualizar/{book_id}', data={'titulo': 'Clean Code Revised', 'autor': 'Robert C. Martin'}, follow_redirects=True)
text = r.data.decode('utf-8')
expect('✅ Libro actualizado correctamente.' in text, 'Test D - update flash')
book = database.obtener_libro(book_id)
expect(book[1] == 'Clean Code Revised', 'Test D - DB updated title')

print('\nSummary: {} passed, {} failed'.format(PASSED, FAILED))
if FAILED > 0:
    sys.exit(1)
else:
    sys.exit(0)
