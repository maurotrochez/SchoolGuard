from django import forms
from django.forms import DateInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import (PrependedText, PrependedAppendedText, FormActions)

from .models import DocumentosVehiculo

# Create the form class.
class DocumentosVehiculoForm(forms.ModelForm):
    #fechaExpedicion = forms.CharField(label='fecha de expediciónn', widget=forms.TextInput(attrs={'type': 'date'}))
    #fechaVencimiento = forms.CharField(label='fecha de vencimiento', widget=forms.TextInput(attrs={'type': 'date'}))

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
            'fechaExpedicion': 'fecha de expedició',
            'fechaVencimiento': 'fecha de vencimiento',
        }
        widgets = {
            'fechaExpedicion': forms.TextInput(attrs={'type': 'date'}),
            'fechaVencimiento': forms.TextInput(attrs={'type': 'date'})
        }

    #valida las fechas que se ingresan en el formulario
    def clean_fechaVencimiento(self):
        vf = self.cleaned_data
        fechaE = vf.get('fechaExpedicion')
        fechaV = vf.get('fechaVencimiento')
        if fechaE >= fechaV:
            raise forms.ValidationError('La fecha de vencimiento no puede ser inferior a la de la fecha de expedidcón')
        return fechaV