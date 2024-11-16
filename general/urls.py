from django.urls import path
from .views import WsLeadsAPIView,CerrarRegistroAPIView

urlpatterns = [
    path('altaLead/', WsLeadsAPIView.as_view(), name='alta-lead'),
    path('cerrarRegistro/', CerrarRegistroAPIView.as_view(), name='cerrar-registro'),
]
