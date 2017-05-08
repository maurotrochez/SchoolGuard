from django import forms
from .models import Route


class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ('name', 'lat', 'long', 'lat_start', 'long_end')
