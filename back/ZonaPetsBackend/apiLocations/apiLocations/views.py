import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

DATABASE_SERVICE_URL = 'http://localhost:8080/' 

class UbicacionList(APIView):
    def get(self, request):
        response = requests.get(f'{DATABASE_SERVICE_URL}ubicaciones/')
        
        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        return Response({"error": "Error al obtener las ubicaciones desde el servicio de base de datos"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
