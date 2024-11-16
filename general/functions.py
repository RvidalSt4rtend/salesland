import requests
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from .models import LogWs

def request_to_external_api(uri, data):
    try:
        external_response = requests.post(uri, json=data)
        external_response_data = external_response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Error al contactar la API externa: {str(e)}"}, status.HTTP_500_INTERNAL_SERVER_ERROR
    
    if external_response_data.get("RESULTADO") != "OK":
        LogWs(cuerpo=data, error=external_response_data, fecha=datetime.now()).save()
        return external_response_data, status.HTTP_500_INTERNAL_SERVER_ERROR

    return external_response_data, status.HTTP_200_OK


def reportar_estado_cerrado(uri, idoportunidad, descripcion):
    json_data = {
        "id_oportunidad": idoportunidad,
        "descripcion": descripcion
    }
    try:
        response = requests.post(uri, json=json_data)
        if response.status_code == 200:
            return {"message": "Estado cerrado reportado exitosamente."}, status.HTTP_200_OK
        else:
            return {"error": "Error al reportar el estado cerrado."}, status.HTTP_500_INTERNAL_SERVER_ERROR
    except requests.exceptions.RequestException as e:
        return {"error": f"Error al contactar la API del proveedor: {str(e)}"}, status.HTTP_500_INTERNAL_SERVER_ERROR