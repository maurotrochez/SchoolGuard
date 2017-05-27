"""schoolguard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from account.views import home
from django.contrib.auth.views import login
from django.contrib.auth.views import logout_then_login

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home', home, name='home'),
    url(r'^account/', include('account.urls'), name='account'),
    url(r'^geo/', include('geo.urls'), name='geo'),
    # url(r'^account/hello', hello, name='hello'),
    url(r'^conductor/', include('conductor.urls'), name='conductor'),
    url(r'^colegio/', include('colegio.urls'), name='colegio'),
    url(r'^estudiante/', include('estudiante.urls'), name='estudiante'),
    url(r'^vehiculo/', include('vehiculo.urls'), name='vehiculo'),
    url(r'^documentosVehiculo/', include('documentosVehiculo.urls'), name='documentosVehiculo'),
    url(r'^api/', include('geo.api.urls'), name='api'),
    url(r'^$', login,{'template_name':'index.html'}, name='login'),
    url(r'^cerrar/$', logout_then_login, name='logout'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL)


