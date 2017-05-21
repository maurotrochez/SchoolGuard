from django import forms
from .models import Route, Device


class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ('name', 'lat', 'long', 'lat_start', 'long_end')


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ('code', 'name', 'vehicle')
        labels = {
            'code': 'Codigo',
            'name': 'Nombre',
            'vehicle': 'Vehiculo',
        }
