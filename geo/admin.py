from django.db import models
from django.contrib import admin
from .models import Route

# Register your models here.


class RouteAdmin(admin.ModelAdmin):
    list_display = ['name', 'lat', 'long']

admin.site.register(Route, RouteAdmin)
