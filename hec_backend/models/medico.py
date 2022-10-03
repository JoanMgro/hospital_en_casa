from django.db import models
from .user import Medicoproxy, User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Medico(models.Model):

    cedula_medico = models.BigIntegerField(primary_key=True, unique=True)
    nombres_medico = models.CharField(max_length=100)
    apellidos_medico = models.CharField(max_length=100)
    genero = models.CharField(max_length=5, null=True, blank=True)
    telefono_medico = models.CharField(max_length=15)
    
    especialidad = models.CharField(max_length= 20)
    registro_medico = models.BigIntegerField(unique=True) 
   
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.nombres_medico + ' ' + self.apellidos_medico + ' - ' + str(self.cedula_medico)



# @receiver(post_save, sender = Medicoproxy)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created and instance.rol == 'MEDICO':
#         Medico.objects.create(user = instance)
    
