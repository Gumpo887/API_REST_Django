# 🎓 TUTORIAL PASO A PASO - Primeros Pasos con la API

## Parte 1: Preparación del Ambiente

### Paso 1: Activar el Entorno Virtual

```powershell
# En Windows PowerShell
cd C:\Users\7991j\Desktop\API_REST_Django
.\venv\Scripts\Activate.ps1
```

**Deberías ver el prefix `(venv)` en tu terminal**

### Paso 2: Verificar que Django está instalado

```bash
python manage.py --version
```

**Resultado esperado**: `Django 6.0.1`

### Paso 3: Aplicar migraciones

```bash
python manage.py migrate
```

**Resultado esperado**: 
```
Operations to perform:
  Apply all migrations
Running migrations:
  Applying ... OK
  ...
```

---

## Parte 2: Crear y Probar Datos

### Paso 4: Crear Productos de Prueba

```bash
python manage.py crear_productos_prueba
```

**Resultado esperado**:
```
============================================================
CREANDO PRODUCTOS DE PRUEBA
============================================================
✓ Creado: Laptop Dell XPS 13 - $1200.0 (Cantidad: 5)
✓ Creado: Mouse Logitech MX Master 3 - $99.99 (Cantidad: 15)
... más productos
```

### Paso 5: Iniciar el Servidor

```bash
python manage.py runserver
```

**Resultado esperado**:
```
Starting development server at http://127.0.0.1:8000/
```

**NO cierres esta ventana terminal. Es necesaria para que la API funcione.**

---

## Parte 3: Probar la API desde el Navegador

### Paso 6: Ver todos los productos (en el navegador)

Abre tu navegador y ve a:

```
http://localhost:8000/api/productos/
```

**Verás una interfaz amigable de Django REST Framework mostrando los productos en formato JSON.**

### Paso 7: Ver un producto específico

```
http://localhost:8000/api/productos/1/
```

**Verás los detalles del primer producto**

---

## Parte 4: Probar con Postman

### Paso 8: Importar la Colección Postman

1. Abre Postman
2. Ve a File → Import
3. Selecciona: `Postman_Collection.json`
4. ¡Listo! Ya tienes todos los endpoints configurados

### Paso 9: Probar cada endpoint

#### 📋 Listar todos los productos
- Selecciona la solicitud "Listar todos los productos"
- Click en "Send"
- Verás todos los 5 productos en JSON

#### 📌 Obtener un producto específico
- Selecciona "Obtener un producto específico"
- Click en "Send"
- Verás los detalles del producto con ID=1

#### ➕ Crear un nuevo producto
- Selecciona "Crear un nuevo producto"
- Verás el JSON en Body:
```json
{
  "nombre": "Monitor Samsung 27",
  "precio": 299.99,
  "cantidad": 10
}
```
- Click en "Send"
- Verás el nuevo producto creado con ID=6

#### ✏️ Actualizar un producto (PUT)
- Selecciona "Actualizar un producto (PUT)"
- Cambia los valores en el body si quieres
- Click en "Send"
- El producto será actualizado completamente

#### 📝 Actualización parcial (PATCH)
- Selecciona "Actualización parcial (PATCH)"
- Solo actualiza el campo "precio"
- El nombre se mantiene igual

#### ❌ Eliminar un producto
- Selecciona "Eliminar un producto"
- Click en "Send"
- El producto será eliminado (respuesta 204)

#### 📦 Aumentar cantidad
- Selecciona "Aumentar cantidad"
- El JSON en body es:
```json
{
  "cantidad": 5
}
```
- La cantidad se suma a la actual

#### 📦 Disminuir cantidad
- Selecciona "Disminuir cantidad"
- El JSON en body es:
```json
{
  "cantidad": 3
}
```
- La cantidad se resta de la actual

---

## Parte 5: Probar con Curl (Windows)

### Paso 10: Abrir PowerShell

Abre una nueva ventana PowerShell (no cierres la anterior con el servidor)

### Paso 11: Listar productos

```powershell
curl http://localhost:8000/api/productos/
```

**Verás el JSON con todos los productos**

### Paso 12: Crear un producto con Curl

```powershell
$body = @{
    nombre = "Auriculares Sony"
    precio = 349.99
    cantidad = 8
} | ConvertTo-Json

curl -X POST http://localhost:8000/api/productos/ `
  -H "Content-Type: application/json" `
  -Body $body
```

**Verás el nuevo producto creado**

### Paso 13: Actualizar un producto

```powershell
$body = @{
    precio = 1299.99
} | ConvertTo-Json

curl -X PATCH http://localhost:8000/api/productos/1/ `
  -H "Content-Type: application/json" `
  -Body $body
```

---

## Parte 6: Panel de Administración

### Paso 14: Crear un superusuario (Opcional)

```bash
python manage.py createsuperuser
```

Sigue las instrucciones (username, email, password)

### Paso 15: Acceder al admin

Abre en tu navegador:

```
http://localhost:8000/admin/
```

Inicia sesión y podrás:
- Ver todos los productos
- Crear nuevos productos
- Editar productos existentes
- Eliminar productos

---

## Parte 7: Ejecutar Pruebas Unitarias

### Paso 16: En una nueva terminal

```bash
cd C:\Users\7991j\Desktop\API_REST_Django
.\venv\Scripts\Activate.ps1
python manage.py test productos -v 2
```

**Verás los 15 tests ejecutándose y todos deben pasar: OK**

---

## Parte 8: Cambiar a MySQL (Opcional)

### Paso 17: Crear la base de datos en MySQL

```sql
CREATE DATABASE api_rest_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### Paso 18: Modificar settings.py

Abre `config/settings.py` y reemplaza:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'api_rest_db',
        'USER': 'root',
        'PASSWORD': '',  # Tu contraseña de MySQL
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### Paso 19: Aplicar migraciones a MySQL

```bash
python manage.py migrate
```

### Paso 20: Crear datos nuevamente

```bash
python manage.py crear_productos_prueba
```

---

## 🎯 Flujo Completo (Resumen)

1. ✅ Activar venv: `.\venv\Scripts\Activate.ps1`
2. ✅ Migraciones: `python manage.py migrate`
3. ✅ Datos prueba: `python manage.py crear_productos_prueba`
4. ✅ Iniciar servidor: `python manage.py runserver`
5. ✅ Probar en navegador: `http://localhost:8000/api/productos/`
6. ✅ Probar en Postman: Importar `Postman_Collection.json`
7. ✅ Ejecutar tests: `python manage.py test productos`

---

## 📚 Endpoints Disponibles

| Método | URL | Descripción |
|--------|-----|------------|
| GET | `/api/productos/` | 📋 Listar todos |
| GET | `/api/productos/1/` | 📌 Ver uno |
| POST | `/api/productos/` | ➕ Crear |
| PUT | `/api/productos/1/` | ✏️ Actualizar completo |
| PATCH | `/api/productos/1/` | 📝 Actualizar parcial |
| DELETE | `/api/productos/1/` | ❌ Eliminar |
| POST | `/api/productos/1/aumentar_cantidad/` | 📦 Aumentar stock |
| POST | `/api/productos/1/disminuir_cantidad/` | 📦 Disminuir stock |

---

## ⚠️ Problemas Comunes

### ❌ "ModuleNotFoundError: No module named 'django'"
**Solución**: Activa el entorno virtual
```bash
.\venv\Scripts\Activate.ps1
```

### ❌ "Port 8000 is already in use"
**Solución**: Cambia el puerto
```bash
python manage.py runserver 8001
```

### ❌ "Connection refused" en MySQL
**Solución**: 
- Verifica que MySQL está ejecutándose
- Comprueba las credenciales en `settings.py`
- Usa SQLite por defecto (no requiere instalación)

### ❌ "Migration problems"
**Solución**: Reinicia las migraciones
```bash
python manage.py migrate --fake-initial
```

---

## ✨ Felicitaciones

¡Has completado el tutorial! Ahora puedes:

✅ Crear productos  
✅ Leer productos  
✅ Actualizar productos  
✅ Eliminar productos  
✅ Gestionar stock  
✅ Ejecutar pruebas  
✅ Usar el panel admin  

---

**¡Listo para empezar! 🚀**

Para más detalles, consulta:
- `README.md` - Documentación completa
- `QUICK_START.md` - Inicio rápido
- `IMPLEMENTACION.md` - Detalles técnicos

