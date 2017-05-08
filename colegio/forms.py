from django import forms
from .models import Colegio

# Create the form class.
class ColegioForm(forms.ModelForm):

    class Meta:
        model = Colegio

        fields = [
            'idColegio',
            'nombre',
            'direccion',
            'nit',
        ]
        labels = {
            'idColegio': 'Numero Colegio',
        }