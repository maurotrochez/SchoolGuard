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


def estudiante_edit(request, id_estudiante):
    estudiante = Estudiante.objects.get(idEstudiante=id_estudiante)
    if request.method == 'GET':
        form = EstudianteForm(instance=estudiante)
    else:
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            # new_user = form.save(commit=False)
            # new_user.set_password(form.cleaned_data['password'])
            form.save()
            messages.success(request, 'Estudiante updated successfully')

            # return render(request, 'account/register_done.html', {'new_user': new_user})
            # return render(request, 'account/list.html', {'new_user': new_user})
            return redirect("list_estudiantes")
    return render(request, 'estudiante/create.html', {'estudiante_form': form})


def estudiante_delete(request, id_estudiante):
    estudiante = Estudiante.objects.get(idEstudiante=id_estudiante)
    if request.method == 'POST':
        estudiante.delete()
        return redirect("list_estudiantes")
    return render(request, 'estudiante/delete.html', {'estudiante': estudiante})