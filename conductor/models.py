from django.db import models

# Create your models here.
class Conductor(models.Model):
	idConductor = models.IntegerField(primary_key=True)
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	paseConduccion = models.CharField(max_length=10)

	def __str__(self):
		return self.nombre