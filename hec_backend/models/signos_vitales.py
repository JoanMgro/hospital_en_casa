from datetime import datetime
from email.policy import default
from django.db import models
from .paciente import Paciente


class SignosVitales(models.Model):
    fecha_muestra = models.DateTimeField(default=datetime.now)
    oximetria = models.FloatField()
    freq_respiratoria = models.FloatField()
    freq_cardiaca = models.FloatField()
    temperatura = models.FloatField()
    presion_arterial = models.FloatField()
    glicemias = models.FloatField()

    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
