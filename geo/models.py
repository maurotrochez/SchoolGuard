from django.db import models

# Create your models here.


class Route(models.Model):
    name = models.CharField(max_length=200)
    # coordinates = models.CharField(max_length=300)
    lat = models.CharField(max_length=200)
    long = models.CharField(max_length=200)
    lat_start = models.CharField(max_length=200)
    long_end = models.CharField(max_length=200)

    def __str__(self):
        return self.name
