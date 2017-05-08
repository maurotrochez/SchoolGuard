from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.list_colegios, name='list_colegios'),
    url(r'^create/$', views.create_colegio, name='create_colegio'),
]
