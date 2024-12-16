from django.db import models

tipos_de_negocio = [
    ("Hoteles", "Hoteles"), 
    ("Restaurantes ", "Restaurantes "),
    ("Tiendas de mascotas", "Tiendas de mascotas"),
    ("Parques para mascotas", "Parques para mascotas"),
    ("Servicios de paseo de perros", "Servicios de paseo de perros"),
    ("Destinos Turisticos", "Destinos Turisticos"),
    ("Centros Comerciales", "Otros")
]

class Pagina(models.Model):
    nombre = models.CharField(max_length=255)
    contenido = models.TextField()

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

class registrofinal2(models.Model):
    nombre_compañia = models.CharField(max_length=150)
    latitud = models.CharField(max_length=150)
    longitud = models.CharField(max_length=150)
    correo_electronico = models.CharField(max_length=150, null=True)
    telefono_usuario = models.CharField(max_length=12, blank=True, null=True,)
    tipo_de_negocio = models.CharField(blank=True, null=True, max_length=75)


