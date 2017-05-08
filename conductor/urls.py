from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.list_conductors, name='list_conductors'),
    url(r'^create/$', views.create_conductor, name='create_conductor'),
]
