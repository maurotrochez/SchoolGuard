from django.shortcuts import render, redirect
from .models import Estudiante
from .forms import EstudianteForm
from django.contrib import messages

# Create your views here.


def list_estudiantes(request):
    list_estudiantes = Estudiante.objects.all()
    return render(request, 'estudiante/list.html', {'data': list_estudiantes})


def create_estudiante(request):
    if request.POST:
        estudiante_form = EstudianteForm(request.POST)
        if estudiante_form.is_valid():
            estudiante_form.save()
            messages.success(request, 'Estudiante created successfully')
            return redirect('list_estudiantes')
    else:
        estudiante_form = EstudianteForm()
    return render(request, 'estudiante/create.html', {'estudiante_form': estudiante_form})
