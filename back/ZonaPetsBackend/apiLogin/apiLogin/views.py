import environ
import os
import requests

from google.oauth2 import id_token
from google.auth.transport import requests

from .serializers import UserRegisterSerializer, UserUpdateSerializer
from .validations import custom_validation, validate_email, validate_password

from rest_framework import permissions, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication

from django.contrib.auth import get_user_model, logout
from django.core.exceptions import ValidationError
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))



User = get_user_model()


class GetUserInfo(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    def get(self, request):
        user = request.user
        
        databaseUrl = env('DATABASE_SERVICE_URL')
        response = requests.get(f'{databaseUrl}/get_user_info', params=user)

        if response.status_code != 200:
            return Response({'error': 'Error obteniendo la información del usuario.'}, status=status.HTTP_504_GATEWAY_TIMEOUT)

        return Response(response.json(), status=status.HTTP_200_OK)

class UpdateUserInfo(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    def post(self, request):
        serializer = UserUpdateSerializer(request.user, data=request.data)

        if serializer.is_valid():
            databaseUrl = env('DATABASE_SERVICE_URL') 
            response = requests.post(f'{databaseUrl}/update_user_info', data=request.data)

            if response.status_code != 200:
                return Response({"error": "Error actualizando los datos del usuario."}, status=status.HTTP_504_GATEWAY_TIMEOUT)

            return Response(response.json(), status=status.HTTP_200_OK)

        return Response({"error": "Error validando los datos de actualización."}, status=status.HTTP_400_BAD_REQUEST)


class GoogleLoginToken(APIView):
    def post(self, request):
        databaseUrl = env('DATABASE_SERVICE_URL')  
        token = request.data.get('token')

        response = requests.get('https://www.googleapis.com/oauth2/v3/userinfo', headers={
            'Authorization': f'Bearer {token}'
        })

        if response.status_code != 200:
            return Response({"error": "Invalid Google token"}, status=400)
        
        userData = response.json()
        email = userData['email']

        databaseResponse = requests.get(f'{databaseUrl}/check_user_exists', params={'email': email})

        if databaseResponse.status_code != 200:
            return Response({"error": "User not registered"}, status=300)

        user = databaseResponse.json()
        refresh = RefreshToken.for_user(user)

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': user  
        }, status=200)


class GoogleLoginCredential(APIView):
     def post(self, request):
        token = request.data.get('token')
        client_id = env('GOOGLE_CLIENT_ID') 

        try:
            databaseUrl = env('DATABASE_SERVICE_URL')  
            idinfo = id_token.verify_oauth2_token(
                token, requests.Request(), client_id
            )

            if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                return Response({"error": "Token no emitido por Google"}, status=400)

            email = idinfo.get('email')
            databaseResponse = requests.get(f'{databaseUrl}/check_user_exists', params={'email': email})

            if databaseResponse.status_code != 200:
                return Response({"error": "Usuario no registrado"}, status=400)

            user = databaseResponse.json()
            refresh = RefreshToken.for_user(user)

            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': user  
            }, status=200)

        except ValueError as e:
            return Response({"error": "Error actualizando el token."}, status=400)


class UserRegister(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        cleanData = custom_validation(request.data)
        serializer = UserRegisterSerializer(data=cleanData)

        try:
            serializer.is_valid(raise_exception=True)
            database_url = env('DATABASE_SERVICE_URL')  
            response = requests.post(f'{database_url}/register_user', data=cleanData)

            if response.status_code != 201:
                return Response({'error_message': "Error registrando nuevo usuario."}, status=status.HTTP_504_GATEWAY_TIMEOUT)

            return Response(response.json(), status=status.HTTP_201_CREATED)

        except ValidationError as e:
            return Response({'error_message': "Error registrando nuevo usuario."}, status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)

    def post(self, request):
        data = request.data
        assert validate_email(data)
        assert validate_password(data)
        
        databaseUrl = env('DATABASE_SERVICE_URL')
        response = requests.post(f'{databaseUrl}/login_user', data=data)

        if response.status_code != 200:
            return Response({'error_message': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        
        userData = response.json()
        user = userData['user']
        
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': user,
        }, status=status.HTTP_200_OK)



class UserView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    def get(self, request):
        user_data = {
            "email": request.user.email,
            'username': request.user.username,
        }

        databaseUrl = env('DATABASE_SERVICE_URL')
        response = requests.get(f'{databaseUrl}/get_user_info', params=user_data)

        if response.status_code != 200:
            return Response({'error': 'Error obteniendo la información del usuario.'}, status=status.HTTP_504_GATEWAY_TIMEOUT)
     
        return Response(response.json(), status=status.HTTP_200_OK)

class UserLogout(APIView):
	permission_classes = (permissions.AllowAny,)
	authentication_classes = ()
	def post(self, request):
		logout(request)
		return Response(status=status.HTTP_200_OK)