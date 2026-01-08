from django.core.management.base import BaseCommand
from productos.models import Producto


class Command(BaseCommand):
    help = 'Crea productos de prueba en la base de datos'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('=' * 60))
        self.stdout.write(self.style.SUCCESS('CREANDO PRODUCTOS DE PRUEBA'))
        self.stdout.write(self.style.SUCCESS('=' * 60))

        # Eliminar productos existentes para empezar de cero
        Producto.objects.all().delete()
        self.stdout.write(self.style.WARNING('Productos anteriores eliminados'))

        productos_data = [
            {"nombre": "Laptop Dell XPS 13", "precio": 1200.00, "cantidad": 5},
            {"nombre": "Mouse Logitech MX Master 3", "precio": 99.99, "cantidad": 15},
            {"nombre": "Teclado Mecánico Corsair K95", "precio": 199.99, "cantidad": 8},
            {"nombre": "Monitor LG 4K 27 pulgadas", "precio": 399.99, "cantidad": 3},
            {"nombre": "Webcam Razer Kiyo Pro", "precio": 199.99, "cantidad": 7},
        ]

        for data in productos_data:
            producto = Producto.objects.create(**data)
            self.stdout.write(
                self.style.SUCCESS(
                    f"✓ Creado: {producto.nombre} - ${producto.precio} (Cantidad: {producto.cantidad})"
                )
            )

        self.stdout.write(self.style.SUCCESS('\n' + '=' * 60))
        self.stdout.write(self.style.SUCCESS('LISTANDO TODOS LOS PRODUCTOS'))
        self.stdout.write(self.style.SUCCESS('=' * 60))

        for producto in Producto.objects.all():
            self.stdout.write(
                f"ID: {producto.id} | Nombre: {producto.nombre} | Precio: ${producto.precio} | Cantidad: {producto.cantidad}"
            )

        self.stdout.write(self.style.SUCCESS('\n' + '=' * 60))
        self.stdout.write(self.style.SUCCESS('PRUEBA COMPLETADA'))
        self.stdout.write(self.style.SUCCESS('=' * 60))
        self.stdout.write('\nAhora puedes probar los endpoints con:')
        self.stdout.write('  - GET    http://localhost:8000/api/productos/')
        self.stdout.write('  - GET    http://localhost:8000/api/productos/{id}/')
        self.stdout.write('  - POST   http://localhost:8000/api/productos/')
        self.stdout.write('  - PUT    http://localhost:8000/api/productos/{id}/')
        self.stdout.write('  - PATCH  http://localhost:8000/api/productos/{id}/')
        self.stdout.write('  - DELETE http://localhost:8000/api/productos/{id}/')
        self.stdout.write('\nAcciones personalizadas:')
        self.stdout.write('  - POST   http://localhost:8000/api/productos/{id}/aumentar_cantidad/')
        self.stdout.write('  - POST   http://localhost:8000/api/productos/{id}/disminuir_cantidad/')
