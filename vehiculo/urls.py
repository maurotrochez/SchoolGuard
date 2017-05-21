from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.list_vehiculos, name='list_vehiculo'),
    url(r'^create/$', views.create_vehiculo, name='create_vehiculo'),
    url(r'^editar/(?P<id_vehiculo>\d+)/$', views.vehiculo_edit, name='vehiculo_edit'),
    url(r'^eliminar/(?P<id_vehiculo>\d+)/$', views.vehiculo_delete, name='vehiculo_delete'),
]