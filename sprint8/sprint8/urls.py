"""sprint8 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
import clientes.urls
import cuentas.urls
import tarjetas.urls
import empleados.urls
import prestamos.urls
from empleados.urls import PublicEndpoint
from login.views import homebanking, register
from paginas.views import atencion_clientes, home, beneficios, preguntas_frecuentes, turnos


urlpatterns = [
    path('', home, name='home'),
    path('homebanking/', homebanking, name='homebanking'),
    path('clientes/', include(clientes.urls), name='clientes'),
    path('cuentas/', include(cuentas.urls), name='cuentas'),
    path('prestamos/', include(prestamos.urls), name='prestamos'),
    path('tarjetas/', include(tarjetas.urls), name='tarjetas'),
    path('login/', LoginView.as_view(template_name='login/registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='login/registration/login.html'), name='logout'),
    path('register/', register, name='register'),
    path('atencionclientes/', atencion_clientes, name='atencionclientes'),
    path('beneficios/', beneficios, name='beneficios'),
    path('preguntasfrecuentes/', preguntas_frecuentes, name='preguntasfrecuentes'),
    path('turnos/', turnos, name='turnos'),
    path('admin/', admin.site.urls),
    path('pps/', include(empleados.urls), name='pps'),
    path('sucursales/', PublicEndpoint.as_view()),
]
