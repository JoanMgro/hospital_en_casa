from django.db import models
from .user import User
from .paciente import Paciente
from django.db.models.signals import post_save
from django.dispatch import receiver

class Familiar(models.Model):

    
    cedula_familiar = models.BigIntegerField(primary_key=True, unique=True)
    nombres_familiar = models.CharField(max_length=100)
    apellidos_familiar = models.CharField(max_length=100)
    genero = models.CharField(max_length=5, null=True, blank=True)
    telefono_familiar = models.CharField(max_length=15)
    parentesco = models.CharField(max_length= 20)

    id_paciente = models.OneToOneField(Paciente, null = True, blank = True, on_delete=models.CASCADE )

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombres_familiar + ' ' + self.apellidos_familiar + ' - ' + str(self.cedula_familiar)

# @receiver(post_save, sender = Familiarproxy)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created and instance.rol == 'FAMILIAR':
#         Familiar.objects.create(user = instance)
    
    





