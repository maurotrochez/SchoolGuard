from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.list_documentosVehiculos, name='list_documentosVehiculo'),
    url(r'^create/$', views.create_documentosVehiculo, name='create_documentosVehiculo'),
]
