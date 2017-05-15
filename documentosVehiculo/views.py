from django.shortcuts import render, redirect
from .models import DocumentosVehiculo
from .forms import DocumentosVehiculoForm
from django.contrib import messages

# Create your views here.


def list_documentosVehiculos(request):
    list_documentosVehiculos = DocumentosVehiculo.objects.all()
    return render(request, 'documentosVehiculo/list.html', {'data': list_documentosVehiculos})


def create_documentosVehiculo(request):
    if request.POST:
        documentosVehiculo_form = DocumentosVehiculoForm(request.POST)
        if documentosVehiculo_form.is_valid():
            documentosVehiculo_form.save()
            messages.success(request, 'Documento created successfully')
            return redirect('list_documentosVehiculo')
    else:
        documentosVehiculo_form = DocumentosVehiculoForm()
    return render(request, 'documentosVehiculo/create.html', {'documentosVehiculo_form': documentosVehiculo_form})
