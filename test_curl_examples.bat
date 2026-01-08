@echo off
REM Script de ejemplos de uso de la API REST con curl
REM Cambiar 'localhost:8000' si la API está en otra dirección

echo.
echo ===== EJEMPLOS DE USO DE LA API REST =====
echo.

echo 1. LISTAR TODOS LOS PRODUCTOS
echo Command: curl http://localhost:8000/api/productos/
echo.

echo 2. OBTENER UN PRODUCTO ESPECÍFICO (ID=1)
echo Command: curl http://localhost:8000/api/productos/1/
echo.

echo 3. CREAR UN NUEVO PRODUCTO
echo Command: curl -X POST http://localhost:8000/api/productos/ ^
echo   -H "Content-Type: application/json" ^
echo   -d "{\"nombre\": \"Monitor Samsung 27\", \"precio\": 299.99, \"cantidad\": 10}"
echo.

echo 4. ACTUALIZAR UN PRODUCTO (PUT)
echo Command: curl -X PUT http://localhost:8000/api/productos/1/ ^
echo   -H "Content-Type: application/json" ^
echo   -d "{\"nombre\": \"Laptop Actualizada\", \"precio\": 1300.00, \"cantidad\": 4}"
echo.

echo 5. ACTUALIZACIÓN PARCIAL (PATCH)
echo Command: curl -X PATCH http://localhost:8000/api/productos/1/ ^
echo   -H "Content-Type: application/json" ^
echo   -d "{\"precio\": 1250.00}"
echo.

echo 6. ELIMINAR UN PRODUCTO
echo Command: curl -X DELETE http://localhost:8000/api/productos/1/
echo.

echo 7. AUMENTAR CANTIDAD DE UN PRODUCTO
echo Command: curl -X POST http://localhost:8000/api/productos/1/aumentar_cantidad/ ^
echo   -H "Content-Type: application/json" ^
echo   -d "{\"cantidad\": 5}"
echo.

echo 8. DISMINUIR CANTIDAD DE UN PRODUCTO
echo Command: curl -X POST http://localhost:8000/api/productos/1/disminuir_cantidad/ ^
echo   -H "Content-Type: application/json" ^
echo   -d "{\"cantidad\": 3}"
echo.

echo ===== FIN DE EJEMPLOS =====
