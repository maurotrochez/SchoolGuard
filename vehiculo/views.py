from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Vehiculo
from django.contrib.auth import get_user_model
from .forms import VehiculoForm
from django.contrib import messages

# Create your views here.

def create_vehiculo(request):
    if request.method == 'POST':
        vehiculo_form = VehiculoForm(request.POST)


        if vehiculo_form.is_valid():
            new_vehiculo = vehiculo_form.save(commit=False)
            new_vehiculo.save()
            messages.success(request, 'Vehiculo creado satisfactoriamente')
            return redirect('list_vehiculo')
    else:
        vehiculo_form = VehiculoForm()
    return render(request, 'vehiculo/create.html', {'vehiculo_form': vehiculo_form})


def list_vehiculos(request):
    list_vehiculos = Vehiculo.objects.all()
    return render(request, 'vehiculo/list.html', {'data': list_vehiculos})

def vehiculo_edit(request, id_vehiculo):
    vehiculo = Vehiculo.objects.get(idVehiculo=id_vehiculo)
    if request.method == 'GET':
        form = VehiculoForm(instance=vehiculo)
    else:
        form = VehiculoForm(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vehiculo actualizado satisfatoriamente')
            return redirect("list_vehiculo")
    return render(request, 'vehiculo/create.html', {'vehiculo_form': form})


def vehiculo_delete(request, id_vehiculo):
    vehiculo = Vehiculo.objects.get(idVehiculo=id_vehiculo)
    if request.method == 'POST':
        vehiculo.delete()
        return redirect("list_vehiculo")
    return render(request, 'vehiculo/delete.html', {'vehiculo': vehiculo})


def home(request):
    return render(request, 'home.html', context={'a': 1})

