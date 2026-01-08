from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Producto
from .serializers import ProductoSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    @action(detail=True, methods=['post'])
    def aumentar_cantidad(self, request, pk=None):
        """Aumentar la cantidad del producto"""
        producto = self.get_object()
        cantidad = request.data.get('cantidad', 1)
        producto.cantidad += int(cantidad)
        producto.save()
        serializer = self.get_serializer(producto)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def disminuir_cantidad(self, request, pk=None):
        """Disminuir la cantidad del producto"""
        producto = self.get_object()
        cantidad = request.data.get('cantidad', 1)
        producto.cantidad -= int(cantidad)
        if producto.cantidad < 0:
            producto.cantidad = 0
        producto.save()
        serializer = self.get_serializer(producto)
        return Response(serializer.data)
