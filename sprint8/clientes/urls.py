from posixpath import basename
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'datos_cliente', views.ClienteViewSet, basename='clientdata')

#Las URL de la API ahora las determina automáticamente el enrutador
urlpatterns = [
    path('clientes/', include(router.urls), name='clientes'),
]