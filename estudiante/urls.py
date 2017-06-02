from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$',login_required(views.list_estudiantes), name='list_estudiantes'),
    url(r'^create/$',login_required(views.create_estudiante), name='create_estudiante'),
    url(r'^editar/(?P<id_estudiante>\d+)/$',login_required(views.estudiante_edit), name='estudiante_edit'),
    url(r'^eliminar/(?P<id_estudiante>\d+)/$',login_required(views.estudiante_delete), name='estudiante_delete'),
]
