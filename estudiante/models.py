from django.db import models
from colegio.models import Colegio

# Create your models here.
class Estudiante(models.Model):
	idEstudiante = models.IntegerField(primary_key=True)
	colegio = models.ForeignKey(Colegio, null=False, blank=False, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=50)
	telefono = models.CharField(max_length=20)


def __str__(self):
	return self.colegio.nombre

