from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.list_documentosVehiculos, name='list_documentosVehiculo'),
    url(r'^create/$', views.create_documentosVehiculo, name='create_documentosVehiculo'),
    url(r'^editar/(?P<id_documento>\d+)/$', views.documentosVehiculo_edit, name='documentosVehiculo_edit'),
    url(r'^eliminar/(?P<id_documento>\d+)/$', views.documentosVehiculo_delete, name='documentosVehiculo_delete'),
]
