from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now

# Create your models here.

class User(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pictures', null=True, blank=True)

class AuxCampanas(models.Model):
    servidor = models.CharField(max_length=50)
    bbdd_report = models.CharField(max_length=50, null=True)
    id_campana = models.IntegerField()
    sistema = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50, null=True)
    activo = models.SmallIntegerField(null=True)
    spcarga_ws_salesland_leads = models.CharField(max_length=50, null=True)
    admite_duplicado = models.SmallIntegerField(null=True)

    class Meta:
        db_table = 'AUX_CAMPANAS'

class AuxDisociar(models.Model):
    campo = models.CharField(max_length=50)

    class Meta:
        db_table = 'AUX_DISOCIAR'


class AuxCampanaDisociar(models.Model):
    campana = models.ForeignKey(AuxCampanas, on_delete=models.RESTRICT)
    campo = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = 'AUX_CAMPANA_DISOCIAR'

class AuxProveedores(models.Model):
    cod_proveedor = models.CharField(max_length=5, null=True)
    proveedor = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = 'AUX_PROVEEDORES'


class LogWs(models.Model):
    cuerpo = models.TextField(null=True)
    error = models.TextField(null=True)
    fecha = models.DateTimeField(null=True)

    class Meta:
        db_table = 'LOG_WS'

class LogsCarga(models.Model):
    id_lead = models.CharField(max_length=50, null=True)
    campana = models.IntegerField(null=True)
    proveedor = models.CharField(max_length=50, null=True)
    log_texto = models.TextField(null=True)
    comando = models.TextField(null=True)
    fecha = models.DateTimeField(null=True)

    class Meta:
        db_table = 'LOGS_CARGA'

class WsLeads(models.Model):
    idtimestamp = models.CharField(max_length=50, null=True)
    fecha_entrada = models.DateTimeField(null=True)
    duplicado = models.SmallIntegerField(null=True)
    cargado = models.SmallIntegerField(null=True)
    fecha_carga = models.DateTimeField(null=True)
    cod_proveedor = models.CharField(max_length=5, null=True)
    id_lead = models.CharField(max_length=50, null=True)
    campana = models.CharField(max_length=50, null=True)
    fecha_captacion = models.DateTimeField(null=True)
    nombre = models.CharField(max_length=50, null=True)
    ape1 = models.CharField(max_length=50, null=True)
    ape2 = models.CharField(max_length=50, null=True)
    telefono = models.CharField(max_length=9, null=True)
    telefono_md5 = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=150, null=True)
    acepta1 = models.CharField(max_length=2, null=True)
    acepta2 = models.CharField(max_length=2, null=True)
    acepta3 = models.CharField(max_length=2, null=True)
    num1 = models.IntegerField(null=True)
    num2 = models.IntegerField(null=True)
    num3 = models.IntegerField(null=True)
    dual1 = models.CharField(max_length=2, null=True)
    dual2 = models.CharField(max_length=2, null=True)
    dual3 = models.CharField(max_length=2, null=True)
    variable1 = models.CharField(max_length=50, null=True)
    variable2 = models.CharField(max_length=50, null=True)
    variable3 = models.CharField(max_length=50, null=True)
    memo = models.TextField(null=True, blank=True)
    fecha = models.DateField(null=True)
    hora = models.TimeField(null=True, blank=True)
    foto1 = models.CharField(max_length=500, null=True)
    foto2 = models.CharField(max_length=500, null=True)
    comercial = models.CharField(max_length=50, null=True)
    centro = models.CharField(max_length=50, null=True)
    codigo_postal = models.CharField(max_length=5, null=True)
    direccion = models.CharField(max_length=50, null=True)
    poblacion = models.CharField(max_length=50, null=True)
    provincia = models.CharField(max_length=50, null=True)
    nif = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = 'WS_LEADS'

class WsLeadsDisociados(models.Model):
    ident_ori = models.IntegerField(null=True)
    idtimestamp = models.CharField(max_length=50, null=True)
    id_unico = models.CharField(max_length=50, null=True)
    fecha_entrada = models.DateTimeField(null=True)
    duplicado = models.SmallIntegerField(null=True)
    cod_proveedor = models.CharField(max_length=5, null=True)
    id_lead = models.CharField(max_length=50, null=True)
    campana = models.CharField(max_length=50, null=True)
    fecha_captacion = models.DateTimeField(null=True)
    nombre = models.CharField(max_length=50, null=True)
    ape1 = models.CharField(max_length=50, null=True)
    ape2 = models.CharField(max_length=50, null=True)
    telefono = models.CharField(max_length=9, null=True)
    telefono_md5 = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=150, null=True)
    acepta1 = models.CharField(max_length=2, null=True)
    acepta2 = models.CharField(max_length=2, null=True)
    acepta3 = models.CharField(max_length=2, null=True)
    num1 = models.IntegerField(null=True)
    num2 = models.IntegerField(null=True)
    num3 = models.IntegerField(null=True)
    dual1 = models.CharField(max_length=2, null=True)
    dual2 = models.CharField(max_length=2, null=True)
    dual3 = models.CharField(max_length=2, null=True)
    variable1 = models.CharField(max_length=50, null=True)
    variable2 = models.CharField(max_length=50, null=True)
    variable3 = models.CharField(max_length=50, null=True)
    memo = models.TextField(null=True)
    fecha = models.DateField(null=True)
    hora = models.TimeField(null=True)
    foto1 = models.CharField(max_length=500, null=True)
    foto2 = models.CharField(max_length=500, null=True)
    comercial = models.CharField(max_length=50, null=True)
    centro = models.CharField(max_length=50, null=True)
    codigo_postal = models.CharField(max_length=5, null=True)
    direccion = models.CharField(max_length=50, null=True)
    poblacion = models.CharField(max_length=50, null=True)
    provincia = models.CharField(max_length=50, null=True)
    nif = models.CharField(max_length=50, null=True)
    cargado = models.SmallIntegerField(null=True)
    fecha_carga = models.DateTimeField(null=True)
    fecha_disociado = models.DateTimeField(null=True)
    nombre_enc = models.BinaryField(null=True)
    ape1_enc = models.BinaryField(null=True)
    ape2_enc = models.BinaryField(null=True)
    telefono_enc = models.BinaryField(null=True)
    email_enc = models.BinaryField(null=True)
    variable1_enc = models.BinaryField(null=True)
    variable2_enc = models.BinaryField(null=True)
    variable3_enc = models.BinaryField(null=True)
    memo_enc = models.BinaryField(null=True)
    foto1_enc = models.BinaryField(null=True)
    foto2_enc = models.BinaryField(null=True)
    codigo_postal_enc = models.BinaryField(null=True)
    direccion_enc = models.BinaryField(null=True)
    poblacion_enc = models.BinaryField(null=True)
    provincia_enc = models.BinaryField(null=True)
    nif_enc = models.BinaryField(null=True)

    class Meta:
        db_table = 'WS_LEADS_DISOCIADOS'
