from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.list_colegios, name='list_colegios'),
    url(r'^create/$', views.create_colegio, name='create_colegio'),
    url(r'^editar/(?P<id_colegio>\d+)/$', views.colegio_edit, name='colegio_edit'),
    url(r'^eliminar/(?P<id_colegio>\d+)/$', views.colegio_delete, name='colegio_delete'),
]
