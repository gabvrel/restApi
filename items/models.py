from django.db import models
from multiselectfield import MultiSelectField
from rest_framework import fields
from django.conf import settings

user = settings.AUTH_USER_MODEL

Tecnologia = 'Tec'
Muebles = 'Mue'
Trabajo = 'Tbr'
Vehiculos = 'Veh'
Alimentos = 'Alm'
Ropa = 'Rop'
Salud = 'Sld'
Mascotas = 'Mac'
Hogar = 'Hog'
Deportivos = 'Dep'
Otros = 'Otr'

Nuevo = 'Nv'
Seminuevo = 'Sn'
Usado = 'Us'

ITEM_TYPES = [
    (Tecnologia, 'Tecnologia'),
    (Muebles, 'Muebles'),
    (Trabajo, 'Trabajo'),
    (Vehiculos, 'Vehiculos'),
    (Alimentos, 'Alimentos'),
    (Ropa, 'Ropa'),
    (Salud, 'Salud'),
    (Mascotas, 'Mascotas'),
    (Hogar, 'Hogar'),
    (Deportivos, 'Deportivos'),
    (Otros, 'Otros'),
]

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'pictures/user_{0}/{1}'.format(instance.user.id, filename)

class Item(models.Model):

    STATE_TYPES = [
        (Nuevo, 'Nuevo'),
        (Seminuevo, 'Seminuevo'),
        (Usado, 'Usado'),
    ]

    title = models.CharField(max_length=300)
    quant = models.IntegerField(blank=True, default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=True)
    details = models.TextField(max_length=500)
    image = models.ImageField(
        upload_to = user_directory_path, max_length=255, null=True, blank=True)
    itemType = models.CharField(
        max_length=20,
        choices=ITEM_TYPES,
        default=Tecnologia,
    )
    date = models.DateTimeField(auto_now_add=True)
    interest = MultiSelectField(choices=ITEM_TYPES,
                                max_length=20)                            
    state = models.CharField(
        max_length=150, choices=STATE_TYPES, default=Nuevo, blank=True)
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name="user")

    def __str__(self):
        return self.title

