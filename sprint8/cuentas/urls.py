from posixpath import basename
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CuentaViewSet

router = DefaultRouter()
router.register(r'datos_cuenta', CuentaViewSet, basename='accountdata')

#Las URL de la API ahora las determina automáticamente el enrutador
urlpatterns = [
    path('cuentas/', include(router.urls), name='cuentas'),
]