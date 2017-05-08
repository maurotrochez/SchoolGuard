from django.shortcuts import render, redirect
from .models import Colegio
from .forms import ColegioForm
from django.contrib import messages

# Create your views here.
def list_colegios(request):
    list_colegios = Colegio.objects.all()
    return render(request, 'colegio/list.html', {'data': list_colegios})


def create_colegio(request):
    if request.POST:
        colegio_form = ColegioForm(request.POST)
        if colegio_form.is_valid():
            colegio_form.save()
            messages.success(request, 'Colegio created successfully')
            return redirect('list_colegios')
    else:
        colegio_form = ColegioForm()
    return render(request, 'colegio/create.html', {'colegio_form': colegio_form})
