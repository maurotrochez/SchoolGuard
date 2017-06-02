from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$',login_required(views.show_map), name='show_map'),
    url(r'^routes$',login_required(views.list_routes), name='list_routes'),
    url(r'^routes/create/$',login_required(views.create_route), name='create_route'),
    url(r'^routes/editar/(?P<id_route>\d+)/$',login_required(views.edit_route), name='edit_route'),
    url(r'^routes/eliminar/(?P<id_route>\d+)/$',login_required(views.delete_route), name='delete_route'),
    url(r'^devices$',login_required(views.list_devices), name='list_devices'),
    url(r'^devices/create/$',login_required(views.create_device), name='create_device'),
    url(r'^devices/editar/(?P<id_device>\d+)/$',login_required(views.edit_device), name='edit_device'),
    url(r'^devices/eliminar/(?P<id_device>\d+)/$',login_required(views.delete_device), name='delete_device'),
]
