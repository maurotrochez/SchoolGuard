from django import forms
from .models import Estudiante

# Create the form class.
class EstudianteForm(forms.ModelForm):

    class Meta:
        model = Estudiante

        fields = [
            'idEstudiante',
            'colegio',
            'nombre',
            'telefono',
        ]
        labels = {
            'idEstudiante': 'Codigo',
        }