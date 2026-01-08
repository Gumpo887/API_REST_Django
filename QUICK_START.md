# 🚀 GUÍA RÁPIDA DE INICIO

## 1. Activar el Entorno Virtual

### Windows PowerShell:
```powershell
.\venv\Scripts\Activate.ps1
```

### Windows CMD:
```cmd
.\venv\Scripts\activate.bat
```

## 2. Instalar Dependencias (si no están ya instaladas)

```bash
pip install -r requirements.txt
```

## 3. Crear la Base de Datos

### SQLite (por defecto, sin configuración):
```bash
python manage.py migrate
```

### MySQL (configurar primero en settings.py):
1. Crear base de datos en MySQL:
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

3. Aplicar migraciones:
```bash
python manage.py migrate
```

## 4. Crear Datos de Prueba

```bash
python manage.py crear_productos_prueba
```

## 5. Iniciar el Servidor

```bash
python manage.py runserver
```

El servidor estará disponible en: **http://localhost:8000**

## 6. Probar la API

### Opción 1: Navegador
Abre: http://localhost:8000/api/productos/

### Opción 2: Postman
1. Importar `Postman_Collection.json`
2. Usar las solicitudes preconfiguradas

### Opción 3: Curl
```bash
# Listar productos
curl http://localhost:8000/api/productos/

# Crear producto
curl -X POST http://localhost:8000/api/productos/ \
  -H "Content-Type: application/json" \
  -d '{"nombre": "Monitor", "precio": 299.99, "cantidad": 5}'
```

### Opción 4: Panel de Administración
http://localhost:8000/admin/

## 📊 Estructura del Proyecto

```
API_REST_Django/
├── config/              # Configuración del proyecto
├── productos/           # App de productos
├── manage.py
├── db.sqlite3           # Base de datos (SQLite)
├── requirements.txt
├── README.md
├── Postman_Collection.json
└── test_curl_examples.bat
```

## 🧪 Ejecutar Pruebas

```bash
python manage.py test productos -v 2
```

## 📝 Endpoints Disponibles

| Método | URL | Descripción |
|--------|-----|-------------|
| GET | `/api/productos/` | Listar todos |
| GET | `/api/productos/{id}/` | Obtener uno |
| POST | `/api/productos/` | Crear |
| PUT | `/api/productos/{id}/` | Actualizar (completo) |
| PATCH | `/api/productos/{id}/` | Actualizar (parcial) |
| DELETE | `/api/productos/{id}/` | Eliminar |
| POST | `/api/productos/{id}/aumentar_cantidad/` | Aumentar stock |
| POST | `/api/productos/{id}/disminuir_cantidad/` | Disminuir stock |

## 🔧 Troubleshooting

### Error: "Django not found"
- Asegúrate de tener el entorno virtual activado
- Instala las dependencias: `pip install -r requirements.txt`

### Error: "MySQL connection failed"
- Verifica que MySQL está ejecutándose
- Comprueba las credenciales en `settings.py`
- Para pruebas rápidas, usa SQLite (configuración por defecto)

### Error: "Port 8000 already in use"
```bash
python manage.py runserver 8001
```

## 📞 Contacto y Soporte

Para más información, consulta:
- [Documentación Django](https://docs.djangoproject.com/)
- [Documentación Django REST Framework](https://www.django-rest-framework.org/)
- [README.md](README.md) - Documentación completa

---

**¡Listo para comenzar! 🎉**
