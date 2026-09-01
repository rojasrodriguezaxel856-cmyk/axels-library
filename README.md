# Axel's Library

Aplicación web para gestionar una biblioteca personal, construida con Flask, SQLite y HTML/CSS/JS.

Este proyecto fue desarrollado como una práctica real de backend, frontend y testing. La app permite administrar libros con operaciones CRUD y además incluye pruebas automatizadas con pytest.

## Características

- Agregar libros con título y autor
- Editar información existente
- Eliminar libros
- Buscar por título o autor
- Diseño responsivo
- Mensajes flash para feedback visual
- Base de datos SQLite aislada para pruebas
- Suite de pruebas automatizadas con pytest

## Tecnologías

- Python
- Flask
- SQLite
- HTML
- CSS
- JavaScript
- pytest

## Estructura del proyecto

```text
mi_primera_web/
├── app.py
├── database.py
├── conftest.py
├── .gitignore
├── .env.example
├── requirements.txt
├── README.md
├── templates/
│   ├── about.html
│   ├── editar.html
│   └── index.html
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
├── tests/
│   └── test_app.py
└── biblioteca.db   # base de datos local de desarrollo
```

## Requisitos

- Python 3.10+
- pip

## Instalación

1. Clona el repositorio:

```bash
git clone <url-del-repositorio>
cd mi_primera_web
```

2. Crea un entorno virtual (opcional pero recomendado):

```bash
python -m venv venv
venv\Scripts\activate
```

3. Instala dependencias:

```bash
pip install -r requirements.txt
```

4. Crea un archivo `.env` a partir del ejemplo:

```bash
copy .env.example .env
```

Contenido sugerido:

```env
SECRET_KEY=change-this-secret-key
FLASK_ENV=development
```

## Cómo ejecutar la app

```bash
python app.py
```

Abre en el navegador:

```text
http://127.0.0.1:5000/
```

## Cómo ejecutar las pruebas

```bash
py -m pytest -v
```

Resultado esperado:

```text
7 passed
```

## Funcionalidades principales

### Inicio
La página principal lista todos los libros disponibles y permite buscar por título o autor.

### Agregar libro
Se envía un formulario con título y autor. Si faltan datos, se muestra un mensaje flash.

### Editar libro
Se accede a la ruta `GET /editar/<id>` y luego se envían los cambios mediante `POST /actualizar/<id>`.

### Eliminar libro
Se elimina el registro mediante una petición `POST` a `/eliminar/<id>`.

### Búsqueda
La app filtra libros por texto ingresado en la barra de búsqueda.

## Seguridad

- `SECRET_KEY` se configura por entorno
- `DEBUG` está deshabilitado en producción
- No se suben variables sensibles a Git
- La base de datos de pruebas se separa de la real con `DB_PATH`

## Estado del proyecto

Este proyecto ya tiene:

- aplicación web funcional
- CRUD completo
- búsquedas
- diseño responsivo
- tests automatizados
- configuración segura para desarrollo y producción
- `.gitignore` para evitar archivos temporales y bases de datos locales

## Autor

Axel

## Nota

Este proyecto representa una base sólida para portfolio: combina backend, frontend, base de datos, testing y buenas prácticas básicas de desarrollo profesional.
