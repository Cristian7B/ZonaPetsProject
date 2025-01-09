import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

DATABASE_SERVICE_URL = 'http://localhost:8080/' 

class ProcesarFormularioView(APIView):
    def post(self, request):
        response = requests.post(f'{DATABASE_SERVICE_URL}procesar/', json=request.data)
        
        if response.status_code == 201:
            return Response({"mensaje": "¡La empresa ha sido registrada!"}, status=status.HTTP_201_CREATED)
        return Response({"error": "Error al procesar el registro en el servicio de base de datos"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ProcesarFormularioEmpresaView(APIView):
    def post(self, request):
        response = requests.post(f'{DATABASE_SERVICE_URL}procesar/empresa/', json=request.data)
        
        if response.status_code == 201:
            return Response({"mensaje": "¡La empresa ha sido registrada!"}, status=status.HTTP_201_CREATED)
        return Response({"error": "Error al procesar el registro empresarial en el servicio de base de datos"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
