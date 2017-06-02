from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$',login_required(views.list_colegios), name='list_colegios'),
    url(r'^create/$',login_required(views.create_colegio), name='create_colegio'),
    url(r'^editar/(?P<id_colegio>\d+)/$',login_required(views.colegio_edit), name='colegio_edit'),
    url(r'^eliminar/(?P<id_colegio>\d+)/$',login_required(views.colegio_delete), name='colegio_delete'),
]
