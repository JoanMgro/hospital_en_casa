from django.db import models
from .user import User, Pacienteproxy

from .medico import Medico
from .enfermero import Enfermero


from django.db.models.signals import post_save
from django.dispatch import receiver

class Paciente (models.Model):



    cedula_paciente = models.BigIntegerField(primary_key=True, unique=True)
    nombres_paciente = models.CharField(max_length=100)
    apellidos_paciente = models.CharField(max_length=100)
    genero = models.CharField(max_length=5, null=True, blank=True)
    telefono_paciente = models.CharField(max_length=15)
    

    fecha_de_nacimiento = models.CharField (max_length = 45)
    ciudad = models.CharField (max_length = 45)
    direccion = models.CharField (max_length = 100)
    latitud = models.CharField (max_length = 45, null=True, blank=True)
    longitud = models.CharField (max_length = 45, null=True, blank=True)
    

    
    id_medico = models.ForeignKey(Medico, null= True, blank=True, on_delete=models.CASCADE )
    id_enfermero = models.ForeignKey(Enfermero, null= True, blank=True, on_delete=models.CASCADE )

    # id_personal_medico = models.OneToOneField(PersonalMedico, null = True, blank = True, on_delete=models.CASCADE)
    #el atributo blank = true hace que sea null en el DB. y no sea requerido en la form.


    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'CC: ' + str(self.cedula_paciente) + ' ' + self.nombres_paciente + ' ' + self.apellidos_paciente



# @receiver(post_save, sender = Pacienteproxy)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created and instance.rol == 'PACIENTE':
#         Paciente.objects.create(user = instance)
    
