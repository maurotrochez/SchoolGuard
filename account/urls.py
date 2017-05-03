from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.list_users, name='list_users'),
    url(r'^register/$', views.register, name='register'),
]
