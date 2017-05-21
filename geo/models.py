from django.db import models
from vehiculo.models import Vehiculo
# Create your models here.


class Device(models.Model):
    code = models.CharField(unique=True, max_length=50)
    name = models.CharField(max_length=200)
    vehicle = models.ForeignKey(Vehiculo, null=False, blank=False)

    def __str__(self):
        return "{} {}".format(self.code, self.name)


class Route(models.Model):
    name = models.CharField(max_length=200)
    lat = models.CharField(max_length=200)
    long = models.CharField(max_length=200)
    lat_start = models.CharField(max_length=200)
    long_end = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Trace(models.Model):
    long = models.CharField(max_length=200)
    lat = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True)
    device = models.ForeignKey(Device, blank=False, null=False)

    def __str__(self):
        return "{} {} / {}".format(self.lat, self.long, self.device.name)