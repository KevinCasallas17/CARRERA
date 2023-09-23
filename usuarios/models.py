from django.db import models
from django.contrib.auth.models import  AbstractUser, PermissionsMixin

class Cliente(AbstractUser, PermissionsMixin):
    num_identificacion = models.CharField(max_length=15,primary_key=True, unique=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    correo = models.EmailField()
    telefono = models.CharField(max_length=10)
    telefono_emergencia = models.CharField(max_length=10)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=4)
    pais = models.CharField(max_length=15)
    ciudad = models.CharField(max_length=22)
    eps = models.CharField(max_length=15)
    sangre = models.CharField(max_length=3)
    talla_camisa = models.CharField(max_length=3)
    inscripcion = models.DateField(auto_now_add=True)


    username=None
    last_name= None
    first_name = None
    email = None
    date_joined = None


    USERNAME_FIELD = 'num_identificacion'

    REQUIRED_FIELDS = ['nombre', 'apellido', 'telefono', 'telefono_emergencia']

    class Meta:
        db_table = 'Cliente'


class Inscripcion(models.Model):

    categoria = models.CharField(max_length=20)
    nivel =models.CharField(max_length=20)
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)
    usuario = models.CharField(max_length=15)
    
    class Meta:
        db_table = 'Inscripcion'