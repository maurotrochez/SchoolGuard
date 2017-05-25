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
            new_doc_vehiculo = documentosVehiculo_form.save(commit=False)
            #new_doc_vehiculo.documentosVehiculo_form.cleaned_data['fechaVencimiento']
            new_doc_vehiculo.save()
            #documentosVehiculo_form.save()
            messages.success(request, 'Documento created successfully')
            return redirect('list_documentosVehiculo')
    else:
        documentosVehiculo_form = DocumentosVehiculoForm()
    return render(request, 'documentosVehiculo/create.html', {'documentosVehiculo_form': documentosVehiculo_form})


def documentosVehiculo_edit(request, id_documento):
    documento = DocumentosVehiculo.objects.get(idDocumentosVehiculo=id_documento)
    if request.method == 'GET':
        form = DocumentosVehiculoForm(instance=documento)
    else:
        form = DocumentosVehiculoForm(request.POST, instance=documento)
        if form.is_valid():
            # new_user = form.save(commit=False)
            # new_user.set_password(form.cleaned_data['password'])
            form.save()
            messages.success(request, 'Documento updated successfully')

            # return render(request, 'account/register_done.html', {'new_user': new_user})
            # return render(request, 'account/list.html', {'new_user': new_user})
            return redirect("list_documentosVehiculo")
    return render(request, 'documentosVehiculo/create.html', {'documentosVehiculo_form': form})


def documentosVehiculo_delete(request, id_documento):
    documento = DocumentosVehiculo.objects.get(idDocumentosVehiculo=id_documento)
    if request.method == 'POST':
        documento.delete()
        return redirect("list_documentosVehiculo")
    return render(request, 'documentosVehiculo/delete.html', {'documento': documento})