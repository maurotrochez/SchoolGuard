from django.db import models

# Create your models here.
class Colegio(models.Model):
	idColegio = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=100)
	direccion = models.CharField(max_length=100)
	nit = models.CharField(max_length=10)

	def __str__(self):
		return self.nombre