from django.db import models

# Create your models here.

class Cliente(models.Model):
    id_cliente=models.CharField(primary_key=True, max_length=5)
    nombre=models.CharField( max_length=100)
    edad=models.PositiveIntegerField()
    intrumento=models.CharField( max_length=50)
    direccion=models.CharField(max_length=250)
    experiencia=models.CharField( max_length=50)
    
    def __str__(self):
        return self.nombre