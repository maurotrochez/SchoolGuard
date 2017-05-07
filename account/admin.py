from django.contrib import admin
from .models import Rol, MyUser
from django.contrib.auth.admin import UserAdmin


class RolAdmin(admin.ModelAdmin):
    list_display = ['name']

# Register your models here.
admin.site.register(Rol, RolAdmin)
admin.site.register(MyUser, UserAdmin)
