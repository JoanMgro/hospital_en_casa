from email.policy import default
from django.db import models
from .paciente import Paciente
import datetime


class Diagnostico(models.Model):
    fecha_diagnostico = models.DateField(default= datetime.date.today)
    diagnostico = models.TextField(max_length=500)
    
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
