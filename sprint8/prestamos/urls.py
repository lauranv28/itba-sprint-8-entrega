from posixpath import basename
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import PrestamoViewSet, ModificaPrestamoViewSet

router = DefaultRouter()
router.register(r'prestamos_cliente', PrestamoViewSet, basename='clientloans')
router.register(r'prestamos', ModificaPrestamoViewSet, basename='modifyloan')

#Las URL de la API ahora las determina automáticamente el enrutador
urlpatterns = [
    path('prestamos', views.prestamos, name='loans'),
    path('/api/prestamos/', include(router.urls), name='prestamos'),
]