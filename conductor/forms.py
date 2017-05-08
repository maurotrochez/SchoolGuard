from django import forms
from .models import Conductor

# Create the form class.
class ConductorForm(forms.ModelForm):

    class Meta:
        model = Conductor

        fields = [
            'idConductor',
            'nombre',
            'apellido',
            'paseConduccion',
        ]
        labels = {
            'idConductor': 'Cedula',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'paseConducción': 'Pase Conduccion',
        }