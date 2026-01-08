@echo off
REM Script para iniciar el servidor Django

echo ========================================
echo  Iniciando servidor Django...
echo ========================================
echo.

REM Activar el entorno virtual
call .\venv\Scripts\activate.bat

REM Aplicar migraciones si es necesario
echo Aplicando migraciones...
python manage.py migrate

REM Crear datos de prueba
echo.
echo Deseas crear datos de prueba? (s/n)
set /p choice=
if /i "%choice%"=="s" (
    echo Creando productos de prueba...
    python manage.py shell < test_api.py
)

REM Iniciar el servidor
echo.
echo ========================================
echo  Servidor ejecutándose en:
echo  http://localhost:8000
echo  Admin: http://localhost:8000/admin
echo  API: http://localhost:8000/api/productos/
echo ========================================
echo.

python manage.py runserver

pause
