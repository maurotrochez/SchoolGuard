from django.shortcuts import render, redirect
from .models import Conductor
from .forms import ConductorForm
from django.contrib import messages

# Create your views here.


def list_conductors(request):
    list_conductors = Conductor.objects.all()
    return render(request, 'conductor/list.html', {'data': list_conductors})


def create_conductor(request):
    if request.POST:
        conductor_form = ConductorForm(request.POST)
        if conductor_form.is_valid():
            conductor_form.save()
            messages.success(request, 'Conductor created successfully')
            return redirect('list_conductors')
    else:
        conductor_form = ConductorForm()
    return render(request, 'conductor/create.html', {'conductor_form': conductor_form})
