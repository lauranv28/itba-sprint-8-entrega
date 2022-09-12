from posixpath import basename
from django.urls import path, include
from . import views
from .views import SucursalViewSet, PublicEndpoint
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'prestamos_de_sucursal/(?P<id>\d+)', SucursalViewSet, basename='loadsbybranch')

urlpatterns = [
    path('branches', views.sucursales, name='branch'),
    path('pps/', include(router.urls), name='pps'),
    path('sucursales/', PublicEndpoint.as_view()),
]