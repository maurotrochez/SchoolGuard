from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.show_map, name='show_map'),
    url(r'^routes$', views.list_routes, name='list_routes'),
    url(r'^routes/create/$', views.create_route, name='create_route'),
]
