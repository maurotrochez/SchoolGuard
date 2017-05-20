from django.shortcuts import render, redirect
from .models import Vehiculo
from .forms import VehiculoForm
from django.contrib import messages

# Create your views here.


def list_vehiculos(request):
    list_vehiculos = Vehiculo.objects.all()
    return render(request, 'vehiculo/list.html', {'data': list_vehiculos})


def create_vehiculo(request):
    if request.POST:
        vehiculo_form = VehiculoForm(request.POST)
        if vehiculo_form.is_valid():
            vehiculo_form.save()
            messages.success(request, 'Vehiculo created successfully')
            return redirect('list_vehiculo')
    else:
        vehiculo_form = VehiculoForm()
    return render(request, 'vehiculo/create.html', {'vehiculo_form': vehiculo_form})

