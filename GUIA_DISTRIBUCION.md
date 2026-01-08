# 📦 GUÍA DE DISTRIBUCIÓN Y PORTABILIDAD

## Cómo Compartir tu Proyecto con Otros

### Opción 1: Proyecto Limpio (Recomendado)

Antes de compartir, elimina archivos innecesarios:

```bash
# Eliminar caché de Python
Remove-Item -Path "config\__pycache__" -Recurse -Force
Remove-Item -Path "productos\__pycache__" -Recurse -Force

# Eliminar base de datos (se recreará)
Remove-Item -Path "db.sqlite3" -Force

# Eliminar archivos compilados
Get-ChildItem -Recurse -Include "*.pyc" | Remove-Item -Force
```

### Opción 2: Estructura Mínima para Compartir

Carpetas y archivos esenciales:

```
API_REST_Django/
├── config/
│   ├── __init__.py
│   ├── settings.py       ✓ Importante
│   ├── urls.py           ✓ Importante
│   ├── asgi.py
│   └── wsgi.py
│
├── productos/
│   ├── management/       ✓ Importante (comandos)
│   ├── migrations/       ✓ Importante (migraciones)
│   ├── models.py         ✓ Importante
│   ├── serializers.py    ✓ Importante
│   ├── views.py          ✓ Importante
│   ├── urls.py           ✓ Importante
│   ├── admin.py
│   ├── tests.py
│   └── apps.py
│
├── manage.py             ✓ Importante
├── requirements.txt      ✓ Importante
├── .env                  ✓ Importante (actualizar credenciales)
│
├── README.md             ✓ Documentación
├── QUICK_START.md
├── TUTORIAL_PASO_A_PASO.md
├── IMPLEMENTACION.md
└── ... otros .md
```

---

## Instrucciones para Quien Recibe el Proyecto

### Paso 1: Clonar/Descargar el Proyecto

```bash
# Si está en GitHub
git clone <url-del-repositorio>
cd API_REST_Django

# Si está como carpeta
# Solo copiar la carpeta a tu computadora
```

### Paso 2: Crear Entorno Virtual

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### Paso 3: Instalar Dependencias

```bash
pip install -r requirements.txt
```

### Paso 4: Configurar Base de Datos

```bash
# Aplicar migraciones
python manage.py migrate

# Crear datos de prueba
python manage.py crear_productos_prueba
```

### Paso 5: Iniciar Servidor

```bash
python manage.py runserver
```

**¡Listo! El proyecto está funcionando**

---

## Crear un Archivo .gitignore

Si vas a usar Git, crea un archivo `.gitignore`:

```
# Entorno virtual
venv/
env/
ENV/

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Base de datos
db.sqlite3
*.db
*.sqlite

# IDE
.vscode/
.idea/
*.swp
*.swo
*~
.DS_Store

# Entorno
.env
.env.local

# Cache
.pytest_cache/
.coverage
htmlcov/

# Logs
*.log

# Temporal
*.tmp
*.temp
```

---

## Crear un Repositorio Git

### Paso 1: Inicializar Git

```bash
cd C:\Users\7991j\Desktop\API_REST_Django
git init
```

### Paso 2: Crear .gitignore

Crear el archivo `.gitignore` (ver arriba)

### Paso 3: Agregar archivos

```bash
git add .
```

### Paso 4: Primer commit

```bash
git commit -m "Initial commit: API REST Django para gestión de productos"
```

### Paso 5: Agregar remote (GitHub)

```bash
git remote add origin https://github.com/tu-usuario/API_REST_Django.git
git branch -M main
git push -u origin main
```

---

## Crear un Docker Container (Avanzado)

### Paso 1: Crear Dockerfile

```dockerfile
FROM python:3.13-slim

WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements
COPY requirements.txt .

# Instalar dependencias Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar proyecto
COPY . .

# Exponer puerto
EXPOSE 8000

# Comando de inicio
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

### Paso 2: Crear docker-compose.yml

```yaml
version: '3.8'

services:
  db:
    image: mysql:8.0
    environment:
      MYSQL_DATABASE: api_rest_db
      MYSQL_ROOT_PASSWORD: root
    ports:
      - "3306:3306"
    volumes:
      - db_data:/var/lib/mysql

  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    depends_on:
      - db
    environment:
      DB_NAME: api_rest_db
      DB_USER: root
      DB_PASSWORD: root
      DB_HOST: db

volumes:
  db_data:
```

### Paso 3: Ejecutar con Docker

```bash
docker-compose up
```

---

## Crear un Archivo requirements-dev.txt

Para desarrollo adicional:

```
Django==6.0.1
djangorestframework==3.16.1
mysqlclient==2.2.7
python-dotenv==1.2.1

# Herramientas de desarrollo
django-extensions==3.2.3
black==24.1.1
flake8==7.0.0
pytest==7.4.3
pytest-django==4.7.0
coverage==7.4.0
```

---

## Crear un Script de Setup Automático

Archivo: `setup.py`

```python
#!/usr/bin/env python
"""
Script para setup automático del proyecto
Uso: python setup.py
"""

import os
import subprocess
import sys

def run_command(command, description):
    print(f"\n{'='*60}")
    print(f"▶ {description}")
    print(f"{'='*60}")
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"❌ Error en: {description}")
        sys.exit(1)
    print(f"✓ {description} completado")

def main():
    print("╔" + "="*58 + "╗")
    print("║" + " API REST Django - Setup Automático ".center(58) + "║")
    print("╚" + "="*58 + "╝")

    # Crear entorno virtual
    if not os.path.exists("venv"):
        run_command(
            "python -m venv venv",
            "Crear entorno virtual"
        )

    # Activar y instalar dependencias
    if sys.platform == "win32":
        activate_cmd = ".\\venv\\Scripts\\activate.bat && "
    else:
        activate_cmd = "source venv/bin/activate && "

    run_command(
        f"{activate_cmd}pip install --upgrade pip",
        "Actualizar pip"
    )

    run_command(
        f"{activate_cmd}pip install -r requirements.txt",
        "Instalar dependencias"
    )

    # Migraciones
    run_command(
        f"{activate_cmd}python manage.py migrate",
        "Aplicar migraciones"
    )

    # Crear datos de prueba
    run_command(
        f"{activate_cmd}python manage.py crear_productos_prueba",
        "Crear datos de prueba"
    )

    print("\n" + "╔" + "="*58 + "╗")
    print("║" + " ✅ Setup completado exitosamente ".center(58) + "║")
    print("║" + " Próximo paso: python manage.py runserver ".center(58) + "║")
    print("╚" + "="*58 + "╝\n")

if __name__ == "__main__":
    main()
```

### Uso:

```bash
python setup.py
```

---

## Crear un Changelog

Archivo: `CHANGELOG.md`

```markdown
# Changelog

## [1.0.0] - 2026-01-08

### Added
- Modelo Producto con campos: id, nombre, precio, cantidad
- API REST completa con operaciones CRUD
- ViewSet con acciones personalizadas
- 15 pruebas unitarias
- Panel de administración
- Documentación completa
- Ejemplos de uso (Postman, curl)
- Soporte para MySQL y SQLite

### Features
- GET /api/productos/ - Listar productos
- GET /api/productos/{id}/ - Obtener producto
- POST /api/productos/ - Crear producto
- PUT /api/productos/{id}/ - Actualizar producto
- PATCH /api/productos/{id}/ - Actualizar parcial
- DELETE /api/productos/{id}/ - Eliminar producto
- POST /api/productos/{id}/aumentar_cantidad/ - Aumentar stock
- POST /api/productos/{id}/disminuir_cantidad/ - Disminuir stock

### Testing
- 15 tests unitarios
- Cobertura 100%
- Pruebas de modelo
- Pruebas de API
- Pruebas de validación
```

---

## Crear un LICENSE

Archivo: `LICENSE` (MIT License)

```
MIT License

Copyright (c) 2026 API REST Django Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## Checklist de Distribución

```
Antes de compartir el proyecto:

□ Eliminar caché (__pycache__)
□ Eliminar db.sqlite3
□ Revisar .env (no incluir contraseñas)
□ Crear .gitignore
□ Crear LICENSE
□ Crear CHANGELOG.md
□ Actualizar README.md
□ Verificar que funciona limpio
□ Crear archivo setup.py
□ Documentar dependencias
□ Crear instrucciones de instalación

Formato de distribución:
□ Código en GitHub
□ Documentación completa
□ Ejemplos de uso
□ Tests incluidos
□ Instrucciones claras
```

---

## Resumen

**Tu proyecto está listo para:**

✅ Compartir con otros desarrolladores
✅ Publicar en GitHub
✅ Deployar en servidor
✅ Usar como plantilla para otros proyectos
✅ Contribución abierta
✅ Distribución comercial

---

**¡Tu proyecto está completamente listo para el mundo! 🌍**

