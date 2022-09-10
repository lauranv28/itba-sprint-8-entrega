"""homebanking URL Configuration

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
from re import template
from django.contrib import admin
from django.urls import path, include
from clientes.views import clientes
from cuentas.views import cuentas
from prestamos.views import prestamos
from tarjetas.views import tarjetas
from login.views import homebanking, register
from paginas.views import atencion_clientes, home, beneficios, preguntas_frecuentes, turnos
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', home, name='home'),
    path('homebanking/', homebanking, name='homebanking'),
    path('clientes/', clientes, name='clientes'),
    path('cuentas/', cuentas, name='cuentas'),
    path('prestamos/', prestamos, name='prestamos'),
    path('tarjetas/', tarjetas, name='tarjetas'),
    path('login/', LoginView.as_view(template_name='login/registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='login/registration/login.html'), name='logout'),
    path('register/', register, name='register'),
    path('atencionclientes/', atencion_clientes, name='atencionclientes'),
    path('beneficios/', beneficios, name='beneficios'),
    path('preguntasfrecuentes/', preguntas_frecuentes, name='preguntasfrecuentes'),
    path('turnos/', turnos, name='turnos'),
    path('admin/', admin.site.urls),
]

