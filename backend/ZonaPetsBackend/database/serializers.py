from rest_framework import serializers
from .models import registroform, registroformularioempresarial, registrofinal2

class RegistroFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = registroform
        fields = ['nombre_compañia', 'telefono_usuario', 'tipo_de_negocio', 'latitud', 'longitud', 'fecha_hora_registro']

class RegistroFormularioEmpresarialSerializer(serializers.ModelSerializer):
    class Meta:
        model = registroformularioempresarial
        fields = [
            'nombre_de_quien_registra', 'telefono_usuario', 'correo_electronico', 
            'tipo_de_negocio', 'nombre_compañia', 'latitud', 'longitud', 'fecha_hora_registro'
        ]

class UbicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = registrofinal2
        fields = '__all__'
