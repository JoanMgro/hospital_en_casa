from django.db import models
from .user import Enfermeroproxy, User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Enfermero(models.Model):

    cedula_enfermero = models.BigIntegerField(primary_key=True, unique=True)
    nombres_enfermero = models.CharField(max_length=100)
    apellidos_enfermero = models.CharField(max_length=100)
    genero = models.CharField(max_length=5, null=True, blank=True)
    telefono_enfermero = models.CharField(max_length=15)      
     
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombres_enfermero + ' ' +self.apellidos_enfermero + ' - ' + str(self.cedula_enfermero)


# @receiver(post_save, sender = Enfermeroproxy)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created and instance.rol == 'ENFERMERO':
#         Enfermero.objects.create(user = instance)
