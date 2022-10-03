from django.db import models
from .paciente import Paciente
import datetime

class SugerenciasCuidado(models.Model):
    fecha_sugerencia = models.DateField(default= datetime.date.today)
    sugerencia = models.TextField(max_length=500)

    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
