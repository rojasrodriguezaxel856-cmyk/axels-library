# 📚 Axel's Library - Mi Primera Web

Una aplicación web para gestionar una biblioteca personal, desarrollada con **Flask**, **SQLite** y **JavaScript vanila**.

## ✨ Características

- ✅ Agregar libros con título y autor
- ✏️ Editar información de libros
- 🗑️ Eliminar libros con confirmación
- 📚 Ver lista completa de libros
- ⏱️ Mensajes de notificación que desaparecen automáticamente
- 📱 Diseño responsivo (funciona en móvil y desktop)

## 🛠️ Tecnologías

| Tecnología | Uso |
|-----------|-----|
| **Python** | Lenguaje de programación |
| **Flask** | Framework web backend |
| **SQLite** | Base de datos |
| **HTML** | Estructura |
| **CSS** | Estilos y diseño responsivo |
| **JavaScript** | Interactividad (DOM manipulation) |

## 📁 Estructura del Proyecto

```
mi_primera_web/
├── app.py                 # Aplicación principal Flask
├── database.py            # Funciones de base de datos
├── requirements.txt       # Dependencias Python
├── biblioteca.db          # Base de datos SQLite
│
├── templates/             # Archivos HTML
│   ├── index.html        # Página principal
│   ├── editar.html       # Página para editar libro
│   └── about.html        # Página acerca de
│
├── static/               # Archivos estáticos
│   ├── css/
│   │   └── style.css     # Estilos CSS
│   ├── js/
│   │   └── script.js     # JavaScript
│   └── img/              # Imágenes
│
└── README.md             # Este archivo
```

## 🚀 Instalación y uso

### Requisitos previos
- Python 3.7+
- pip (gestor de paquetes Python)

### Pasos para ejecutar

1. **Clonar o descargar el proyecto**
   ```bash
   cd mi_primera_web
   ```

2. **Instalar las dependencias**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar la aplicación**
   ```bash
   python app.py
   ```

4. **Abrir en el navegador**
   - Ir a: `http://127.0.0.1:5000/`

## 📖 Cómo usar

### Agregar un libro
1. Ve a la sección "Agregar libro"
2. Ingresa el título y autor
3. Haz clic en "➕ Agregar Libro"
4. Verás una notificación verde que desaparece en 3 segundos

### Editar un libro
1. Haz clic en "✏️ Editar" en el libro que quieres modificar
2. Cambia el título o autor
3. Haz clic en "💾 Guardar cambios"

### Eliminar un libro
1. Haz clic en "🗑️ Eliminar" en el libro
2. Confirma que deseas eliminarlo
3. El libro se borrará inmediatamente

## 🎓 Lo que aprendí

Este proyecto fue mi primer paso en desarrollo web:

- 🐍 **Python con Flask**: Cómo crear un servidor web
- 🗄️ **SQLite**: Cómo crear y consultar bases de datos
- 🌐 **HTML/CSS**: Estructura y estilos web
- ⚡ **JavaScript**: Manipulación del DOM y eventos
- 🎨 **Diseño responsivo**: Cómo hacer apps que se adapten a todos los tamaños de pantalla

## 🔧 Comandos útiles

```bash
# Ejecutar la app (modo desarrollo con debug)
python app.py

# Instalar dependencias
pip install -r requirements.txt
```

## 📝 Notas

- La base de datos `biblioteca.db` se crea automáticamente al ejecutar la app
- Los mensajes de flash desaparecen después de 3 segundos
- Los libros se ordenan por ID descendente (más nuevos primero)

## 👨‍💻 Autor

Axel - Mi primera aplicación web 🚀

---

**Hecho con ❤️ y mucho JavaScript**
