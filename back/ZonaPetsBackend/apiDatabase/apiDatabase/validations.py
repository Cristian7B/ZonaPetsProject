from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

UserModel = get_user_model()

def custom_validation(data):
    email = data['email'].strip()
    username = data['username'].strip()
    password = data['password'].strip()
    
    if not email or UserModel.objects.filter(email=email).exists():
        raise ValidationError("Escribe un email diferente.")
    if not password or len(password) < 8:
        raise ValidationError('La contraseña debe tener al menos 8 caracteres.')
    if not username:
        raise ValidationError('Escribe un nombre de usuario diferente.')
    return data


def validate_email(data):
    email = data['email'].strip()
    if not email:
        raise ValidationError('Es necesario un email')
    return True

def validate_username(data):
    username = data['username'].strip()
    if not username:
        raise ValidationError('Escribe un nombre de usuario diferente.')
    return True

def validate_password(data):
    password = data['password'].strip()
    if not password:
        raise ValidationError('Es necesaria una contraseña')
    return True