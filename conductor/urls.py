from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$',login_required(views.list_conductors), name='list_conductors'),
    url(r'^create/$',login_required(views.create_conductor), name='create_conductor'),
    url(r'^editar/(?P<id_conductor>\d+)/$',login_required(views.conductor_edit), name='conductor_edit'),
    url(r'^eliminar/(?P<id_conductor>\d+)/$',login_required(views.conductor_delete), name='conductor_delete'),
]
