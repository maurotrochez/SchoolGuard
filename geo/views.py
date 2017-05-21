from django.shortcuts import render, redirect
from .models import Route, Device
from .forms import RouteForm, DeviceForm
from django.contrib import messages

# Create your views here.


def list_routes(request):
    list_route = Route.objects.all()
    return render(request, 'geo/routes/list.html', {'data': list_route})


def list_devices(request):
    list_device = Device.objects.all()
    return render(request, 'geo/devices/list.html', {'data': list_device})


def create_route(request):
    if request.POST:
        route_form = RouteForm(request.POST)
        if route_form.is_valid():
            route_form.save()
            messages.success(request, 'Route created successfully')
            return redirect('list_routes')
    else:
        route_form = RouteForm()
    return render(request, 'geo/routes/create.html', {'route_form': route_form})


def create_device(request):
    if request.POST:
        device_form = DeviceForm(request.POST)
        if device_form.is_valid():
            device_form.save()
            messages.success(request, 'Device created successfully')
            return redirect('list_devices')
    else:
        device_form = DeviceForm()
    return render(request, 'geo/devices/create.html', {'device_form': device_form})


def edit_route(request, id_route):
    route = Route.objects.get(id=id_route)
    if request.method == 'GET':
        form = RouteForm(instance=route)
    else:
        form = RouteForm(request.POST, instance=route)
        if form.is_valid():
            form.save()
            messages.success(request, 'Route modified successfully')
            return redirect('list_routes')
    return render(request, 'geo/routes/create.html', {'route_form': form})


def edit_device(request, id_device):
    device = Device.objects.get(id=id_device)
    if request.method == 'GET':
        form = DeviceForm(instance=device)
    else:
        form = DeviceForm(request.POST, instance=device)
        if form.is_valid():
            form.save()
            messages.success(request, 'Device modified successfully')
            return redirect('list_devices')
    return render(request, 'geo/devices/create.html', {'device_form': form})


def delete_route(request, id_route):
    route = Route.objects.get(id=id_route)
    if request.method == 'POST':
        route.delete()
        return redirect('list_routes')
    return render(request, 'geo/routes/delete.html', {'route': route})


def delete_device(request, id_device):
    device = Device.objects.get(id=id_device)
    if request.method == 'POST':
        device.delete()
        return redirect('list_devices')
    return render(request, 'geo/devices/delete.html', {'device': device})


def show_map(request):
    return render(request, 'geo/map.html', {})
