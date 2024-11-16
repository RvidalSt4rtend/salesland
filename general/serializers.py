from rest_framework import serializers
from .models import WsLeads
from datetime import datetime

class WsLeadsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WsLeads
        fields = [
            "id_lead", "campana", "cod_proveedor", "fecha_captacion", "nombre", "ape1", "ape2",
            "nif", "telefono", "email", "direccion", "codigo_postal", "poblacion", "provincia",
            "acepta1", "acepta2", "acepta3", "num1", "num2", "num3", "dual1", "dual2", "dual3",
            "variable1", "variable2", "variable3", "memo", "fecha", "hora", "foto1", "foto2",
            "comercial", "centro"
        ]

