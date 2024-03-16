from django.db import models

# Create your models here.
class Product(models.Model):
    PRODUCT_TYPES = [
        ("INSTRUMENTOS", "INSTRUMENTOS"),
        ("ACCESORIOS", "ACCESORIOS")
    ]
    nombre= models.CharField(max_length=150)
    marca= models.CharField(max_length=100)
    modelo= models.CharField(max_length=100, null=True, blank=True)
    descripcion= models.TextField(blank=True, default="", null=True)
    tipo= models.CharField(max_length=50, choices=PRODUCT_TYPES )
    categoria= models.CharField(max_length=150)
    precio= models.FloatField(max_length=150)
    imagen= models.ImageField(upload_to="uploads/%Y/%m")
    