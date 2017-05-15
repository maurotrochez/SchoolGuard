from django import forms
from .models import Vehiculo

# Create the form class.
class VehiculoForm(forms.ModelForm):

    class Meta:
        model = Vehiculo

        fields = [
            'idVehiculo',
            'conductor',
            'placa',
            'marca',
            'linea',
            'modelo',
            'cilindraje',
            'color',
            'clase',
            'tipo',
            'serie',
            'nombre',
            'cedula',
        ]
