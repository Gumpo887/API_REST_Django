"""
Script para probar los endpoints de la API REST
Ejecutar con: python manage.py shell < test_api.py
O manualmente copiar y pegar los comandos en el shell de Django
"""

import os
import django

# Configurar Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from productos.models import Producto

# Crear algunos productos de prueba
print("=" * 60)
print("CREANDO PRODUCTOS DE PRUEBA")
print("=" * 60)

productos_data = [
    {"nombre": "Laptop Dell XPS 13", "precio": 1200.00, "cantidad": 5},
    {"nombre": "Mouse Logitech MX Master 3", "precio": 99.99, "cantidad": 15},
    {"nombre": "Teclado Mecánico Corsair K95", "precio": 199.99, "cantidad": 8},
    {"nombre": "Monitor LG 4K 27 pulgadas", "precio": 399.99, "cantidad": 3},
    {"nombre": "Webcam Razer Kiyo Pro", "precio": 199.99, "cantidad": 7},
]

for data in productos_data:
    producto = Producto.objects.create(**data)
    print(f"✓ Creado: {producto.nombre} - ${producto.precio} (Cantidad: {producto.cantidad})")

print("\n" + "=" * 60)
print("LISTANDO TODOS LOS PRODUCTOS")
print("=" * 60)

for producto in Producto.objects.all():
    print(f"ID: {producto.id} | Nombre: {producto.nombre} | Precio: ${producto.precio} | Cantidad: {producto.cantidad}")

print("\n" + "=" * 60)
print("PRUEBA COMPLETADA")
print("=" * 60)
print("\nAhora puedes probar los endpoints con:")
print("  - GET    http://localhost:8000/api/productos/")
print("  - GET    http://localhost:8000/api/productos/{id}/")
print("  - POST   http://localhost:8000/api/productos/")
print("  - PUT    http://localhost:8000/api/productos/{id}/")
print("  - PATCH  http://localhost:8000/api/productos/{id}/")
print("  - DELETE http://localhost:8000/api/productos/{id}/")
print("\nAcciones personalizadas:")
print("  - POST   http://localhost:8000/api/productos/{id}/aumentar_cantidad/")
print("  - POST   http://localhost:8000/api/productos/{id}/disminuir_cantidad/")
