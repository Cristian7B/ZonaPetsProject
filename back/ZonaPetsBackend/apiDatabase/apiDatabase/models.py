from django.db import models, IntegrityError

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager

from django.core.validators import validate_email
from django.core.exceptions import ValidationError

class AppUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        if not password:
            raise ValueError('The password must be set')
        
        email = self.normalize_email(email)

        try:
            validate_email(email)
        except ValidationError:
            raise ValueError('The Email is not valid')
        
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)

        try:
            user.save()
        except IntegrityError:
            raise ValueError('A user with this email already exists')

        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Credenciales inválidas')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Credenciales inválidas')

        return self.create_user(email, username, password, **extra_fields)


class AppUser(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=50, unique=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    username = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    ciudad = models.CharField(max_length=50, blank=True, null=True)
    foto = models.CharField(blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    objects = AppUserManager()

    class Meta:
        db_table = "user_api_appuser"

    def __str__(self):
    	return self.username



tipos_de_negocio = [
    ("Hoteles", "Hoteles"), 
    ("Restaurantes ", "Restaurantes "),
    ("Tiendas de mascotas", "Tiendas de mascotas"),
    ("Parques para mascotas", "Parques para mascotas"),
    ("Servicios de paseo de perros", "Servicios de paseo de perros"),
    ("Destinos Turisticos", "Destinos Turisticos"),
    ("Centros Comerciales", "Otros")
]

class registroform(models.Model):
    nombre_compañia = models.CharField(max_length=75)
    telefono_usuario = models.CharField(max_length=12, blank=True, null=True,)
    tipo_de_negocio = models.CharField(
        null=True,
        max_length=75,
        choices = tipos_de_negocio, 
        default="Hoteles"
    )
    latitud = models.CharField(max_length=100)
    longitud = models.CharField(max_length=75)
    fecha_hora_registro = models.DateTimeField(null=True, auto_now_add = True)

    class Meta:
        db_table = "PetSearch_registroform"
    
class registroformularioempresarial(models.Model):
    nombre_de_quien_registra = models.CharField(max_length=100, blank=True, null=True,)
    telefono_usuario = models.CharField(max_length=12, blank=True, null=True,)
    correo_electronico = models.CharField(max_length=100)
    tipo_de_negocio = models.CharField(
        null=True,
        max_length=75,
        choices = tipos_de_negocio, 
        default="Hoteles"
    )
    nombre_compañia = models.CharField(max_length=75)
    latitud = models.CharField(max_length=100)
    longitud = models.CharField(max_length=100)
    fecha_hora_registro = models.DateTimeField(null = True, auto_now_add = True)

    class Meta:
        db_table = "PetSearch_registroformularioempresarial"

class registrofinal2(models.Model):
    nombre_compañia = models.CharField(max_length=150)
    latitud = models.CharField(max_length=150)
    longitud = models.CharField(max_length=150)
    correo_electronico = models.CharField(max_length=150, null=True)
    telefono_usuario = models.CharField(max_length=12, blank=True, null=True,)
    tipo_de_negocio = models.CharField(blank=True, null=True, max_length=75)

    class Meta:
        db_table = "PetSearch_registrofinal2"


