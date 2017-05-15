from django import forms
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
