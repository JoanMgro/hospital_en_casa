# Generated by Django 4.1.1 on 2022-09-30 21:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hec_backend', '0003_alter_signosvitales_fecha_muestra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sugerenciascuidado',
            name='fecha_sugerencia',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
