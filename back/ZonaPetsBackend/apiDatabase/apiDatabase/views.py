from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import RegistroFormSerializer, RegistroFormularioEmpresarialSerializer, UbicacionSerializer, UserModel, UserUpdateSerializer, UserRegisterSerializer
from .models import registrofinal2

class ProcesarFormularioView(APIView):
    def post(self, request):
        serializer = RegistroFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje": "¡La empresa ha sido registrada!"}, status=status.HTTP_201_CREATED)
        return Response({"error": "No se ha podido registrar la empresa"}, status=status.HTTP_400_BAD_REQUEST)

class ProcesarFormularioEmpresaView(APIView):
    def post(self, request):
        serializer = RegistroFormularioEmpresarialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje": "¡La empresa ha sido registrada!"}, status=status.HTTP_201_CREATED)
        return Response({"error": "No se ha podido registrar la empresa"}, status=status.HTTP_400_BAD_REQUEST)

class UbicacionListView(APIView):
    def get(self, request):
        queryset = registrofinal2.objects.all()
        serializer = UbicacionSerializer(queryset, many=True)
        return Response(serializer.data)

class GetUserInfo(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        try:
            userInfo = UserModel.objects.get(email=user.email)
            userData = {
                'email': userInfo.email,
                'username': userInfo.username,
                'nombre': userInfo.nombre,
                'telefono': userInfo.telefono,
                'foto': userInfo.foto,
            }
            return Response(userData, status=status.HTTP_200_OK)
        except UserModel.DoesNotExist:
            return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
class UpdateUserInfo(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        user = request.user
        serializer = UserUpdateSerializer(user, data=request.data)
        
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Error validando los datos de actualización."}, status=status.HTTP_400_BAD_REQUEST)
    
class RegisterUser(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()   
            return Response({
                'message': 'Usuario registrado exitosamente',
                'user': UserRegisterSerializer(user).data
            }, status=status.HTTP_201_CREATED)
        return Response({"error": "Error registrando el usuario."}, status=status.HTTP_400_BAD_REQUEST)
    
class LoginUser(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        
        user = authenticate(username=email, password=password)
        
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': UserRegisterSerializer(user).data
            }, status=status.HTTP_200_OK)
        return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_400_BAD_REQUEST)
    

class CheckUserExists(APIView):
    def get(self, request):
        email = request.query_params.get('email')
        
        try:
            user = UserModel.objects.get(email=email)
            return Response({'exists': True, 'user': UserRegisterSerializer(user).data}, status=status.HTTP_200_OK)
        except UserModel.DoesNotExist:
            return Response({'exists': False}, status=status.HTTP_200_OK)