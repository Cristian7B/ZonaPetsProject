from django.urls import path
from .views import UbicacionList

urlpatterns = [
    path('ubicaciones/', UbicacionList.as_view(), name='ubicacion_list'),
]
