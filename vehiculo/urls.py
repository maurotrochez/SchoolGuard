from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$',login_required(views.list_vehiculos), name='list_vehiculo'),
    url(r'^create/$', login_required(views.create_vehiculo), name='create_vehiculo'),
    url(r'^editar/(?P<id_vehiculo>\d+)/$',login_required(views.vehiculo_edit), name='vehiculo_edit'),
    url(r'^eliminar/(?P<id_vehiculo>\d+)/$',login_required(views.vehiculo_delete), name='vehiculo_delete'),
]