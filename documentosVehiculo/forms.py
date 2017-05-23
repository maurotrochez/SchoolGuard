from django import forms
from django.forms import DateInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import (PrependedText, PrependedAppendedText, FormActions)

from .models import DocumentosVehiculo

# Create the form class.
class DocumentosVehiculoForm(forms.ModelForm):

    class Meta:
        model = DocumentosVehiculo

        fields = [
            'vehiculo',
            'tipoDocumento',
            'fechaExpedicion',
            'fechaVencimiento',
        ]
        labels = {
            'vehiculo': 'Placa del vehiculo',
            'tipoDocumento': 'tipo de documento',
            'fechaExpedicion': 'fecha de expedición',
            'fechaVencimiento': 'fecha de vencimiento',
        }
        widgets = {
            'fechaExpedicion': forms.TextInput(attrs={'type': 'date'}),
            'fechaVencimiento': forms.TextInput(attrs={'type': 'date'})
        }
