from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class Rol(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_rol')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class MyUser(AbstractUser):
    rol = models.ForeignKey(Rol, related_name='user_rol', default=None, blank=True, null=True)
    # example = models.CharField(max_length=200)

    class Meta:
        db_table = 'auth_user'
