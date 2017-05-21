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

def colegio_edit(request, id_colegio):
    colegio = Colegio.objects.get(idColegio=id_colegio)
    if request.method == 'GET':
        form = ColegioForm(instance=colegio)
    else:
        form = ColegioForm(request.POST, instance=colegio)
        if form.is_valid():
            # new_user = form.save(commit=False)
            # new_user.set_password(form.cleaned_data['password'])
            form.save()
            messages.success(request, 'Colegio updated successfully')

            # return render(request, 'account/register_done.html', {'new_user': new_user})
            # return render(request, 'account/list.html', {'new_user': new_user})
            return redirect("list_colegios")
    return render(request, 'colegio/create.html', {'colegio_form': form})


def colegio_delete(request, id_colegio):
    colegio = Colegio.objects.get(idColegio=id_colegio)
    if request.method == 'POST':
        colegio.delete()
        return redirect("list_colegios")
    return render(request, 'colegio/delete.html', {'colegio': colegio})