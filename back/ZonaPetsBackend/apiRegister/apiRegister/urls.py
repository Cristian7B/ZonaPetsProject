from django.urls import path
from .views import ProcesarFormularioView, ProcesarFormularioEmpresaView

urlpatterns = [
    path('registrar/', ProcesarFormularioView.as_view(), name='procesar_formulario'),
    path('registrar/empresa/', ProcesarFormularioEmpresaView.as_view(), name='procesar_formulario_empresa'),
]