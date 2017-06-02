from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$',login_required(views.list_users), name='list_users'),
    url(r'^register/$',login_required(views.register), name='register'),
    url(r'^editar/(?P<id_user>\d+)/$',login_required(views.user_edit), name='user_edit'),
    url(r'^eliminar/(?P<id_user>\d+)/$',login_required(views.user_delete), name='user_delete'),

]
