from django.db import models


class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    precio = models.FloatField()
    cantidad = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre} - ${self.precio}"
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['id']
