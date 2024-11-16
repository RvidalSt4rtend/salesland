# myapp/tasks.py
from celery import shared_task
import requests
from django.utils import timezone

@shared_task
def reportar_duracion_llamada(idoportunidad, duracion, id_operador):
    json_data = {
        "id_oportunidad": idoportunidad,
        "duracion": duracion,
        "id_operador": id_operador,
        "fecha": timezone.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    # Api externa dummy de ejemplo
    uri = "https://proveedor.com/api/reportar_duracion_llamada"
    try:
        response = requests.post(uri, json=json_data)
        if response.status_code == 200:
            return response.json()  # Suponiendo que la respuesta es JSON
        else:
            return {"error": "Error al reportar la duración de la llamada."}
    except requests.exceptions.RequestException as e:
        return {"error": f"Error al contactar con la API del proveedor: {str(e)}"}
