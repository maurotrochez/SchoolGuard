from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.list_conductors, name='list_conductors'),
    url(r'^create/$', views.create_conductor, name='create_conductor'),
    url(r'^editar/(?P<id_conductor>\d+)/$', views.conductor_edit, name='conductor_edit'),
    url(r'^eliminar/(?P<id_conductor>\d+)/$', views.conductor_delete, name='conductor_delete'),
]
