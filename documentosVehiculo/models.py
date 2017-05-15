from django.db import models
from vehiculo.models import Vehiculo

# Create your models here.
class DocumentosVehiculo(models.Model):
    idDocumentosVehiculo = models.AutoField(primary_key=True)
    vehiculo = models.ForeignKey(Vehiculo, null=False, blank=False, on_delete=models.CASCADE)
    tipoDocumento = models.CharField(max_length=50)
    fechaExpedicion = models.DateField()
    fechaVencimiento = models.DateField()

