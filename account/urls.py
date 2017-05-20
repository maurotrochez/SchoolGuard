from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.list_users, name='list_users'),
    url(r'^register/$', views.register, name='register'),
    url(r'^editar/(?P<id_user>\d+)/$', views.user_edit, name='user_edit'),
    url(r'^eliminar/(?P<id_user>\d+)/$', views.user_delete, name='user_delete'),
]
