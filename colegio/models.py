from django.db import models

# Create your models here.
class Colegio(models.Model):
	idColegio = models.IntegerField(primary_key=True)
	nombre = models.CharField(max_length=100)
	direccion = models.TextField()
	nit = models.CharField(max_length=10)