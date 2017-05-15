from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.list_estudiantes, name='list_estudiantes'),
    url(r'^create/$', views.create_estudiante, name='create_estudiante'),
]