from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Producto


class ProductoModelTest(TestCase):
    """Pruebas para el modelo Producto"""

    def setUp(self):
        """Crear un producto de prueba"""
        self.producto = Producto.objects.create(
            nombre="Test Product",
            precio=99.99,
            cantidad=10
        )

    def test_crear_producto(self):
        """Prueba que se puede crear un producto"""
        self.assertEqual(self.producto.nombre, "Test Product")
        self.assertEqual(self.producto.precio, 99.99)
        self.assertEqual(self.producto.cantidad, 10)

    def test_str_producto(self):
        """Prueba la representación en string del producto"""
        self.assertEqual(str(self.producto), "Test Product - $99.99")

    def test_actualizar_producto(self):
        """Prueba que se puede actualizar un producto"""
        self.producto.precio = 149.99
        self.producto.save()
        producto_actualizado = Producto.objects.get(id=self.producto.id)
        self.assertEqual(producto_actualizado.precio, 149.99)

    def test_eliminar_producto(self):
        """Prueba que se puede eliminar un producto"""
        producto_id = self.producto.id
        self.producto.delete()
        with self.assertRaises(Producto.DoesNotExist):
            Producto.objects.get(id=producto_id)


class ProductoAPITest(APITestCase):
    """Pruebas para los endpoints de la API"""

    def setUp(self):
        """Configurar cliente API y datos de prueba"""
        self.client = APIClient()
        self.producto1 = Producto.objects.create(
            nombre="Laptop",
            precio=1200.00,
            cantidad=5
        )
        self.producto2 = Producto.objects.create(
            nombre="Mouse",
            precio=99.99,
            cantidad=15
        )
        self.list_url = reverse('producto-list')
        self.detail_url = reverse('producto-detail', kwargs={'pk': self.producto1.id})

    def test_listar_productos(self):
        """Prueba el endpoint GET para listar todos los productos"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_obtener_producto(self):
        """Prueba el endpoint GET para obtener un producto específico"""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nombre'], 'Laptop')
        self.assertEqual(response.data['precio'], 1200.0)

    def test_crear_producto(self):
        """Prueba el endpoint POST para crear un nuevo producto"""
        data = {
            'nombre': 'Teclado',
            'precio': 199.99,
            'cantidad': 8
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['nombre'], 'Teclado')
        self.assertEqual(Producto.objects.count(), 3)

    def test_actualizar_producto_put(self):
        """Prueba el endpoint PUT para actualizar completamente un producto"""
        data = {
            'nombre': 'Laptop Actualizada',
            'precio': 1300.00,
            'cantidad': 4
        }
        response = self.client.put(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nombre'], 'Laptop Actualizada')
        self.assertEqual(response.data['precio'], 1300.0)

    def test_actualizar_producto_patch(self):
        """Prueba el endpoint PATCH para actualizar parcialmente un producto"""
        data = {'precio': 1250.00}
        response = self.client.patch(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['precio'], 1250.0)
        self.assertEqual(response.data['nombre'], 'Laptop')

    def test_eliminar_producto(self):
        """Prueba el endpoint DELETE para eliminar un producto"""
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Producto.objects.count(), 1)

    def test_aumentar_cantidad(self):
        """Prueba la acción personalizada para aumentar cantidad"""
        url = reverse('producto-aumentar-cantidad', kwargs={'pk': self.producto1.id})
        data = {'cantidad': 5}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['cantidad'], 10)  # 5 + 5

    def test_disminuir_cantidad(self):
        """Prueba la acción personalizada para disminuir cantidad"""
        url = reverse('producto-disminuir-cantidad', kwargs={'pk': self.producto1.id})
        data = {'cantidad': 2}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['cantidad'], 3)  # 5 - 2

    def test_disminuir_cantidad_no_negativa(self):
        """Prueba que la cantidad no sea negativa"""
        url = reverse('producto-disminuir-cantidad', kwargs={'pk': self.producto1.id})
        data = {'cantidad': 10}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['cantidad'], 0)  # Mínimo es 0

    def test_crear_producto_sin_datos(self):
        """Prueba que se valide la creación sin datos"""
        response = self.client.post(self.list_url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_obtener_producto_inexistente(self):
        """Prueba que se devuelva 404 para un producto inexistente"""
        url = reverse('producto-detail', kwargs={'pk': 999})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
