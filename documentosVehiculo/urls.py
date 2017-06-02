from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$',login_required(views.list_documentosVehiculos), name='list_documentosVehiculo'),
    url(r'^create/$',login_required(views.create_documentosVehiculo), name='create_documentosVehiculo'),
    url(r'^editar/(?P<id_documento>\d+)/$',login_required(views.documentosVehiculo_edit), name='documentosVehiculo_edit'),
    url(r'^eliminar/(?P<id_documento>\d+)/$',login_required(views.documentosVehiculo_delete), name='documentosVehiculo_delete'),
]
