from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.list_estudiantes, name='list_estudiantes'),
    url(r'^create/$', views.create_estudiante, name='create_estudiante'),
    url(r'^editar/(?P<id_estudiante>\d+)/$', views.estudiante_edit, name='estudiante_edit'),
    url(r'^eliminar/(?P<id_estudiante>\d+)/$', views.estudiante_delete, name='estudiante_delete'),
]
