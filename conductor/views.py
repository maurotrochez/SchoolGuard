from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Conductor
from django.contrib.auth import get_user_model
from .forms import ConductorForm
from django.contrib import messages


# Create your views here.


def create_conductor(request):
    if request.method == 'POST':
        conductor_form = ConductorForm(request.POST)

        if conductor_form.is_valid():
            new_conductor = conductor_form.save(commit=False)
            new_conductor.save()
            messages.success(request, 'Conductor created successfully')
            return redirect('list_conductors')
    else:
        conductor_form = ConductorForm()
    return render(request, 'conductor/create.html', {'conductor_form': conductor_form})


def list_conductors(request):
    list_conductors = Conductor.objects.all()
    return render(request, 'conductor/list.html', {'data': list_conductors})


def conductor_edit(request, id_conductor):
    conductor = Conductor.objects.get(idConductor=id_conductor)
    if request.method == 'GET':
        form = ConductorForm(instance=conductor)
    else:
        form = ConductorForm(request.POST, instance=conductor)
        if form.is_valid():
            form.save()
            messages.success(request, 'conductor updated successfully')
            return redirect("list_conductors")
    return render(request, 'conductor/create.html', {'conductor_form': form})


def conductor_delete(request, id_conductor):
    conductor = Conductor.objects.get(idConductor=id_conductor)
    if request.method == 'POST':
        conductor.delete()
        return redirect("list_conductors")
    return render(request, 'conductor/delete.html', {'conductor': conductor})


def home(request):
    return render(request, 'home.html', context={'a': 1})
