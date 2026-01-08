# API REST Django - Gestión de Productos

Una API REST completa desarrollada con Django y Django REST Framework para la gestión de productos.

## 📋 Características

- ✅ Configuración de proyecto Django
- ✅ Modelo Producto con atributos: id, nombre, precio, cantidad
- ✅ Migraciones de base de datos
- ✅ Serializador para el modelo Producto
- ✅ ViewSets para operaciones CRUD
- ✅ Rutas API configuradas
- ✅ Acciones personalizadas (aumentar/disminuir cantidad)
- ✅ Soporte para MySQL y SQLite

## 🚀 Configuración Inicial

### 1. Requisitos Previos

- Python 3.8+
- pip (gestor de paquetes de Python)
- MySQL (opcional, por defecto usa SQLite)

### 2. Instalación

#### Crear entorno virtual
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1  # En Windows PowerShell
# o
.\venv\Scripts\activate.bat  # En Windows CMD
```

#### Instalar dependencias
```bash
pip install django djangorestframework mysqlclient python-dotenv
```

### 3. Configuración de Base de Datos

#### Opción A: SQLite (por defecto, sin configuración adicional)
La base de datos SQLite se crea automáticamente.

#### Opción B: MySQL
1. Crear la base de datos en MySQL:
```sql
CREATE DATABASE api_rest_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

2. Modificar `config/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'api_rest_db',
        'USER': 'root',
        'PASSWORD': 'tu_contraseña',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 4. Aplicar Migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Crear Datos de Prueba

```bash
python manage.py shell < test_api.py
```

O manualmente:
```bash
python manage.py shell
```

```python
from productos.models import Producto

Producto.objects.create(nombre="Laptop", precio=1200.00, cantidad=5)
Producto.objects.create(nombre="Mouse", precio=99.99, cantidad=15)
Producto.objects.create(nombre="Teclado", precio=199.99, cantidad=8)
```

## 🏃 Ejecutar el Servidor

```bash
python manage.py runserver
```

El servidor estará disponible en: `http://localhost:8000`

## 📡 Endpoints de la API

### Base URL
```
http://localhost:8000/api/productos/
```

### Operaciones CRUD

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/productos/` | Listar todos los productos |
| GET | `/api/productos/{id}/` | Obtener un producto específico |
| POST | `/api/productos/` | Crear un nuevo producto |
| PUT | `/api/productos/{id}/` | Actualizar completamente un producto |
| PATCH | `/api/productos/{id}/` | Actualizar parcialmente un producto |
| DELETE | `/api/productos/{id}/` | Eliminar un producto |

### Acciones Personalizadas

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/api/productos/{id}/aumentar_cantidad/` | Aumentar la cantidad de un producto |
| POST | `/api/productos/{id}/disminuir_cantidad/` | Disminuir la cantidad de un producto |

## 💡 Ejemplos de Uso

### 1. Listar todos los productos
```bash
curl http://localhost:8000/api/productos/
```

### 2. Obtener un producto específico
```bash
curl http://localhost:8000/api/productos/1/
```

### 3. Crear un nuevo producto
```bash
curl -X POST http://localhost:8000/api/productos/ \
  -H "Content-Type: application/json" \
  -d '{"nombre": "Monitor Samsung", "precio": 299.99, "cantidad": 10}'
```

### 4. Actualizar un producto (PUT)
```bash
curl -X PUT http://localhost:8000/api/productos/1/ \
  -H "Content-Type: application/json" \
  -d '{"nombre": "Laptop Actualizada", "precio": 1300.00, "cantidad": 4}'
```

### 5. Actualización parcial (PATCH)
```bash
curl -X PATCH http://localhost:8000/api/productos/1/ \
  -H "Content-Type: application/json" \
  -d '{"precio": 1250.00}'
```

### 6. Eliminar un producto
```bash
curl -X DELETE http://localhost:8000/api/productos/1/
```

### 7. Aumentar cantidad
```bash
curl -X POST http://localhost:8000/api/productos/1/aumentar_cantidad/ \
  -H "Content-Type: application/json" \
  -d '{"cantidad": 5}'
```

### 8. Disminuir cantidad
```bash
curl -X POST http://localhost:8000/api/productos/1/disminuir_cantidad/ \
  -H "Content-Type: application/json" \
  -d '{"cantidad": 3}'
```

## 📁 Estructura del Proyecto

```
API_REST_Django/
├── config/                 # Configuración del proyecto Django
│   ├── settings.py        # Configuración principal
│   ├── urls.py            # Rutas principales
│   ├── wsgi.py
│   └── asgi.py
├── productos/             # Aplicación de productos
│   ├── migrations/        # Migraciones de base de datos
│   ├── models.py          # Modelo Producto
│   ├── serializers.py     # Serializador ProductoSerializer
│   ├── views.py           # ViewSet ProductoViewSet
│   ├── urls.py            # Rutas de la API de productos
│   ├── admin.py
│   ├── apps.py
│   └── tests.py
├── manage.py              # Script de gestión de Django
├── db.sqlite3             # Base de datos (SQLite, opcional)
├── .env                   # Variables de entorno
├── test_api.py            # Script de pruebas
├── test_curl_examples.bat # Ejemplos con curl
├── setup_database.sql     # Script SQL para MySQL
└── README.md              # Este archivo
```

## 🔧 Configuración Avanzada

### Variables de Entorno (.env)
```
DB_NAME=api_rest_db
DB_USER=root
DB_PASSWORD=
DB_HOST=localhost
DB_PORT=3306
DEBUG=True
```

### Agregar autenticación
Para agregar autenticación JWT, instala:
```bash
pip install djangorestframework-simplejwt
```

Y configura en `settings.py`:
```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}
```

## 🧪 Herramientas de Prueba

### Postman
1. Importar en Postman:
   - GET: http://localhost:8000/api/productos/
   - POST: http://localhost:8000/api/productos/
   - PUT: http://localhost:8000/api/productos/{id}/
   - DELETE: http://localhost:8000/api/productos/{id}/

### Curl
Ver archivo `test_curl_examples.bat` para ejemplos

### Navegador
Acceder a: http://localhost:8000/api/productos/
(La interfaz browsable de Django REST Framework estará disponible)

## 📝 Modelo Producto

```python
class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    precio = models.FloatField()
    cantidad = models.IntegerField()
```

### Campos:
- **id**: Identificador único (Auto-generado)
- **nombre**: Nombre del producto (máximo 255 caracteres)
- **precio**: Precio del producto (número flotante)
- **cantidad**: Cantidad en stock (número entero)

## 🐛 Solución de Problemas

### Error: "Can't connect to MySQL server"
- Asegúrate de que MySQL está ejecutándose
- Verifica las credenciales en `settings.py`
- Considera usar SQLite por defecto

### Error: "ModuleNotFoundError: No module named 'django'"
- Asegúrate de activar el entorno virtual
- Reinstala las dependencias: `pip install -r requirements.txt`

### Error: "Migration problems"
```bash
python manage.py migrate --fake-initial
```

## 📚 Recursos Útiles

- [Documentación Django](https://docs.djangoproject.com/)
- [Documentación Django REST Framework](https://www.django-rest-framework.org/)
- [Documentación MySQL Connector/Python](https://dev.mysql.com/doc/connector-python/en/)

## 👤 Autor

API REST desarrollada como proyecto educativo

## 📄 Licencia

Este proyecto está bajo licencia MIT

---

**Nota**: Recuerda cambiar la `SECRET_KEY` y `DEBUG=False` en producción.
