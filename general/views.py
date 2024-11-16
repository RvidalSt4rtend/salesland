from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import WsLeadsSerializer
from .functions import request_to_external_api, reportar_estado_cerrado

class WsLeadsAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        uri = "https://webapp.salesland.net:8095/WS_SALESLAND_LEADS/SALESLAND_LEADSCmb.svc/AltaLead"

        external_response_data, external_status = request_to_external_api(uri, data)

        if external_status != status.HTTP_200_OK:
            return Response(external_response_data, status=external_status)
        
        serializer = WsLeadsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(external_response_data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CerrarRegistroAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        idoportunidad = data.get('id_oportunidad')
        descripcion = data.get('descripcion')

        if not idoportunidad or not descripcion:
            return Response({"error": "El campo 'id_oportunidad' y 'descripcion' son requeridos."}, status=status.HTTP_400_BAD_REQUEST)
        #Api externa dummy de ejemplo
        uri = "https://proveedor.com/api/reportar_estado_cerrado"
        response_data, response_status = reportar_estado_cerrado(uri, idoportunidad, descripcion)

        return Response(response_data, status=response_status)
