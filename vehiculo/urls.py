from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.list_vehiculos, name='list_vehiculo'),
    url(r'^create/$', views.create_vehiculo, name='create_vehiculo'),
]