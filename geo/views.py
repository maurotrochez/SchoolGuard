from django.shortcuts import render, redirect
from .models import Route
from .forms import RouteForm
from django.contrib import messages

# Create your views here.


def list_routes(request):
    list_routes = Route.objects.all()
    return render(request, 'geo/routes/list.html', {'data': list_routes})


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


def show_map(request):
    return render(request, 'geo/map.html', {})
