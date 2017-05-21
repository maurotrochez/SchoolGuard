from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.show_map, name='show_map'),
    url(r'^routes$', views.list_routes, name='list_routes'),
    url(r'^routes/create/$', views.create_route, name='create_route'),
    url(r'^routes/editar/(?P<id_route>\d+)/$', views.edit_route, name='edit_route'),
    url(r'^routes/eliminar/(?P<id_route>\d+)/$', views.delete_route, name='delete_route'),
    url(r'^devices$', views.list_devices, name='list_devices'),
    url(r'^devices/create/$', views.create_device, name='create_device'),
    url(r'^devices/editar/(?P<id_device>\d+)/$', views.edit_device, name='edit_device'),
    url(r'^devices/eliminar/(?P<id_device>\d+)/$', views.delete_device, name='delete_device'),
]
