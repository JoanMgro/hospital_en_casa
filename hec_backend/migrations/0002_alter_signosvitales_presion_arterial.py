# Generated by Django 4.1.1 on 2022-09-28 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hec_backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signosvitales',
            name='presion_arterial',
            field=models.FloatField(),
        ),
    ]
