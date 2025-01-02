from django.contrib.auth import get_user_model, login, logout
from django.core.exceptions import ValidationError

import environ
from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))



from google.oauth2 import id_token
from google.auth.transport import requests

from rest_framework import permissions, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import AppUser
from .serializers import UserRegisterSerializer, UserLoginSerializer, UserSerializer, UserUpdateSerializer
from .validations import custom_validation, validate_email, validate_password

import requests

User = get_user_model()

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_info(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)



@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def update_user_info(request):
    user = request.user
    serializer = UserUpdateSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response("Error actualizando tus datos.", status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def google_login_token(request):
    token = request.data.get('token')

    response = requests.get('https://www.googleapis.com/oauth2/v3/userinfo', headers={
        'Authorization': f'Bearer {token}'
    })

    if response.status_code != 200:
        return Response({"error": "Invalid Google token"}, status=400)

	
    user_data = response.json()
    email = user_data['email']
    
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({"error": "User not registered"}, status=300)
    
    refresh = RefreshToken.for_user(user)

    return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'user': UserSerializer(user).data
    }, status=200)


import jwt
@api_view(['POST'])
def google_login_credential(request):
    token = request.data.get('token')
    client_id = env('GOOGLE_CLIENT_ID') 
    
    try:
        idinfo = id_token.verify_oauth2_token(
            token, requests.Request(), client_id
        )


        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            return Response({"error": "Token no emitido por Google"}, status=400)

        email = idinfo.get('email')

        try:
            user = AppUser.objects.get(email=email)
        except AppUser.DoesNotExist:
            return Response({"error": "Usuario no registrado"}, status=400)

        refresh = RefreshToken.for_user(user)

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': UserSerializer(user).data
        }, status=200)

    except ValueError as e:
        return Response({"error": "Error actualizando el token."}, status=400)

class UserRegister(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        clean_data = custom_validation(request.data)
        serializer = UserRegisterSerializer(data=clean_data)

        try:
            serializer.is_valid(raise_exception=True)
            user = serializer.create(clean_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({'error_message': "Error registrando nuevo usuario."}, status=status.HTTP_504_GATEWAY_TIMEOUT)


class UserLogin(APIView):
	permission_classes = (permissions.AllowAny,)
	authentication_classes = (SessionAuthentication,)
	##
	def post(self, request):
		data = request.data
		assert validate_email(data)
		assert validate_password(data)
		serializer = UserLoginSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			user = serializer.check_user(data)
			refresh = RefreshToken.for_user(user)
			login(request, user)
			return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': UserSerializer(user).data,
            }, status=status.HTTP_200_OK)


class UserLogout(APIView):
	permission_classes = (permissions.AllowAny,)
	authentication_classes = ()
	def post(self, request):
		logout(request)
		return Response(status=status.HTTP_200_OK)


class UserView(APIView):
	permission_classes = (permissions.IsAuthenticated,)
	authentication_classes = (JWTAuthentication,)
	##
	def get(self, request):
		user_data = {
			"email": request.user.email,
			'username': request.user.username,
		}
		serializer = UserSerializer(request.user)
		return Response({'user': serializer.data}, status=status.HTTP_200_OK)
