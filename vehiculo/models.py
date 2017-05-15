from django.db import models
from conductor.models import Conductor


# Create your models here.
class Vehiculo(models.Model):
    idVehiculo = models.AutoField(primary_key=True)
    conductor = models.ForeignKey(Conductor, null=False, blank=False, on_delete=models.CASCADE)
    placa = models.CharField(max_length=10)
    marca = models.CharField(max_length=20)
    linea = models.CharField(max_length=20)
    modelo = models.IntegerField()
    cilindraje =models.IntegerField()
    color = models.CharField(max_length=20)
    clase = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)
    serie = models.CharField(max_length=20)
    nombre = models.CharField(max_length=50)
    cedula = models.CharField(max_length=20)


    def __str__(self):
        return self.placa
# Create your models here.
