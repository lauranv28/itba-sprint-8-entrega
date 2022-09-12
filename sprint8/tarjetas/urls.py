from posixpath import basename
from django.urls import path, include
from .views import TarjetaViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tarjetas/(?P<id>\d+)', TarjetaViewSet, basename='cards')

urlpatterns = [
    path('tarjetas/', include(router.urls), name='tarjetas')
]