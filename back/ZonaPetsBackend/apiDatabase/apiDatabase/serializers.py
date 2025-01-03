from rest_framework import serializers
from .models import registroform, registroformularioempresarial, registrofinal2

from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError

UserModel = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserModel
		fields = '__all__'
		extra_kwargs = {
            'password': {'write_only': True},
        }
	def create(self, validated_data):
		user_obj = UserModel.objects.create_user(
            email=validated_data['email'], 
            password=validated_data['password'],
            username=validated_data['username'],
            nombre=validated_data.get('nombre', ''),
            telefono=validated_data.get('telefono', ''),
			foto=validated_data.get('foto', '')  
        )
		return user_obj


class UserLoginSerializer(serializers.Serializer):
	email = serializers.EmailField()
	password = serializers.CharField()

	def check_user(self, clean_data):
		user = authenticate(username=clean_data['email'], password=clean_data['password'])
		if not user:
			raise ValidationError('user not found')
		return user


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserModel
		fields = ("nombre",'email', 'username', "telefono", "ciudad", "foto")


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['email', 'username', 'nombre', 'ciudad', 'telefono']

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


