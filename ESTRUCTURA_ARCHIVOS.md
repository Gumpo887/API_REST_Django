# 📂 ESTRUCTURA DEL PROYECTO - GUÍA DE ARCHIVOS

## 📋 Archivos en Raíz

### Configuración y Gestión
- **`manage.py`** - Script principal de Django para gestionar el proyecto
- **`requirements.txt`** - Lista de dependencias del proyecto
- **`.env`** - Variables de entorno (configuración sensible)
- **`setup_database.sql`** - Script SQL para crear la base de datos en MySQL

### Documentación
- **`README.md`** - Documentación completa del proyecto
- **`QUICK_START.md`** - Guía rápida de inicio
- **`IMPLEMENTACION.md`** - Resumen de la implementación
- **`ESTE_ARCHIVO.md`** - Guía de estructura de archivos

### Datos y Configuración de Herramientas
- **`Postman_Collection.json`** - Colección lista para importar en Postman
- **`EJEMPLOS_JSON.json`** - Ejemplos de JSON para las solicitudes
- **`db.sqlite3`** - Base de datos SQLite (generada automáticamente)

### Scripts Auxiliares
- **`start_server.bat`** - Script para iniciar el servidor (Windows)
- **`test_api.py`** - Script para crear datos de prueba
- **`test_curl_examples.bat`** - Ejemplos de uso con curl

---

## 📁 Carpeta `config/`
Configuración principal del proyecto Django

### Archivos Principales
- **`settings.py`** ⭐ - Configuración central del proyecto
  - Aplicaciones instaladas (Django, DRF, productos)
  - Configuración de base de datos (MySQL/SQLite)
  - Middlewares
  - Configuración de REST Framework

- **`urls.py`** ⭐ - Rutas principales del proyecto
  - Incluye `/admin/` para el panel de administración
  - Incluye `/api/productos/` para la API

- **`wsgi.py`** - Configuración WSGI para producción
- **`asgi.py`** - Configuración ASGI para WebSockets (si se necesita)
- **`__init__.py`** - Marca la carpeta como paquete Python

---

## 📁 Carpeta `productos/`
Aplicación para gestión de productos

### Archivos Principales

#### **`models.py`** ⭐
Define el modelo `Producto` con campos:
- `id` - Clave primaria (auto-generada)
- `nombre` - Nombre del producto (máx. 255 caracteres)
- `precio` - Precio (número flotante)
- `cantidad` - Cantidad en stock (entero)

#### **`serializers.py`** ⭐
- `ProductoSerializer` - Serializador para convertir Producto a JSON y viceversa
- Define qué campos se incluyen en la API

#### **`views.py`** ⭐
- `ProductoViewSet` - ViewSet que maneja todas las operaciones CRUD
- Acciones personalizadas:
  - `aumentar_cantidad` - POST para agregar stock
  - `disminuir_cantidad` - POST para quitar stock

#### **`urls.py`** ⭐
- Configuración del router de DRF
- Rutas automáticas para todas las operaciones CRUD

#### **`admin.py`** 
- Configuración del panel de administración de Django
- Permite gestionar productos desde `/admin/`

#### **`tests.py`** ⭐
- 15 pruebas unitarias automatizadas
- Pruebas del modelo y de la API
- Verifican CRUD, validaciones y acciones personalizadas

#### **`apps.py`**
- Configuración de la aplicación

#### **`__init__.py`**
- Marca la carpeta como paquete Python

### Subcarpeta `migrations/`
Historial de cambios en la base de datos

- **`0001_initial.py`** - Primera migración (crea tabla Producto)
- **`__init__.py`** - Marca como paquete

### Subcarpeta `management/commands/`
Comandos personalizados de Django

- **`crear_productos_prueba.py`** - Comando para crear productos de prueba
  - Uso: `python manage.py crear_productos_prueba`

---

## 📊 Flujo de Trabajo

```
USUARIO
   ↓
Postman / Curl / Navegador
   ↓
URLs (urls.py) → Enrutamiento
   ↓
Views (views.py) → ProductoViewSet (Lógica)
   ↓
Serializers (serializers.py) → Conversión JSON
   ↓
Models (models.py) → Base de Datos
   ↓
Respuesta JSON
```

---

## 🔑 Archivos Clave a Modificar

Para personalizar el proyecto, estos son los archivos más importantes:

| Archivo | Descripción | Cuándo Modificar |
|---------|------------|------------------|
| `config/settings.py` | Configuración central | Cambiar BD, agregar apps, seguridad |
| `productos/models.py` | Definición de datos | Agregar/modificar campos del producto |
| `productos/serializers.py` | API responses | Cambiar qué datos se devuelven |
| `productos/views.py` | Lógica de la API | Agregar validaciones o funcionalidades |
| `productos/urls.py` | Rutas de API | Cambiar estructura de endpoints |
| `test_api.py` | Datos de prueba | Crear diferentes productos demo |

---

## 🗂️ Estructura Completa del Proyecto

```
API_REST_Django/
│
├── config/                           # 🔧 Configuración Django
│   ├── __init__.py
│   ├── __pycache__/
│   ├── settings.py                   # ⭐ Configuración principal
│   ├── urls.py                       # ⭐ Rutas principales
│   ├── asgi.py
│   └── wsgi.py
│
├── productos/                        # 🛒 Aplicación de productos
│   ├── management/
│   │   ├── __init__.py
│   │   └── commands/
│   │       ├── __init__.py
│   │       └── crear_productos_prueba.py  # 📝 Comando personalizado
│   │
│   ├── migrations/
│   │   ├── __init__.py
│   │   ├── __pycache__/
│   │   └── 0001_initial.py          # 📋 Primera migración
│   │
│   ├── __init__.py
│   ├── __pycache__/
│   ├── admin.py                      # 🔐 Panel admin
│   ├── apps.py
│   ├── models.py                     # ⭐ Modelo Producto
│   ├── serializers.py                # ⭐ Serializador
│   ├── tests.py                      # ⭐ Pruebas (15 tests)
│   ├── urls.py                       # ⭐ Rutas API
│   └── views.py                      # ⭐ ViewSet y vistas
│
├── venv/                             # 🐍 Entorno virtual
│
├── .env                              # 🔑 Variables de entorno
├── db.sqlite3                        # 💾 Base de datos SQLite
├── manage.py                         # 🎮 Gestor de Django
│
├── 📄 ARCHIVOS DE DOCUMENTACIÓN
├── README.md                         # 📚 Documentación completa
├── QUICK_START.md                    # ⚡ Inicio rápido
├── IMPLEMENTACION.md                 # ✅ Resumen implementación
├── ESTE_ARCHIVO.md                   # 🗂️ Estructura (TÚ ESTÁS AQUÍ)
│
├── 📄 ARCHIVOS DE CONFIGURACIÓN
├── requirements.txt                  # 📦 Dependencias
├── setup_database.sql                # 🗄️ Script MySQL
│
├── 📄 ARCHIVOS DE PRUEBAS Y EJEMPLOS
├── Postman_Collection.json           # 🚀 Colección Postman
├── EJEMPLOS_JSON.json                # 📋 Ejemplos de JSON
├── test_api.py                       # 🧪 Script pruebas
├── test_curl_examples.bat            # 🌐 Ejemplos curl
└── start_server.bat                  # ▶️ Iniciar servidor
```

---

## 💡 Consejos de Uso

### Para Agregar Nuevos Campos al Producto
1. Edita `productos/models.py`
2. Crea la migración: `python manage.py makemigrations`
3. Aplica: `python manage.py migrate`
4. Actualiza `productos/serializers.py` si es necesario

### Para Cambiar de SQLite a MySQL
1. Edita `config/settings.py` → Sección `DATABASES`
2. Crea la BD en MySQL
3. Ejecuta: `python manage.py migrate`

### Para Agregar Validaciones
- Edita `productos/models.py` (a nivel de modelo)
- O edita `productos/serializers.py` (a nivel de validación)

### Para Agregar Nuevos Endpoints
- Agrega métodos con @action en `productos/views.py`
- Las rutas se generan automáticamente

---

## 🚀 Resumen Rápido

| Tarea | Archivo | Comando |
|-------|---------|---------|
| Iniciar servidor | - | `python manage.py runserver` |
| Crear BD | `config/settings.py` | `python manage.py migrate` |
| Crear datos prueba | `manage.py` | `python manage.py crear_productos_prueba` |
| Acceder API | `productos/urls.py` | http://localhost:8000/api/productos/ |
| Admin panel | `productos/admin.py` | http://localhost:8000/admin/ |
| Ejecutar tests | `productos/tests.py` | `python manage.py test productos` |

---

**¡Todos los archivos están listos y funcionando correctamente! 🎉**

