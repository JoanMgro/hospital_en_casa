# Generated by Django 4.1.1 on 2022-09-23 15:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=250)),
                ('tipo_usuario', models.CharField(choices=[('PACIENTE', 'Paciente'), ('FAMILIAR', 'Familiar'), ('MEDICO', 'Medico'), ('ENFERMERO', 'Enfermero'), ('AUXILIAR', 'Auxiliar')], max_length=10)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Enfermero',
            fields=[
                ('cedula_enfermero', models.BigIntegerField(primary_key=True, serialize=False, unique=True)),
                ('nombres_enfermero', models.CharField(max_length=100)),
                ('apellidos_enfermero', models.CharField(max_length=100)),
                ('genero', models.CharField(blank=True, max_length=5, null=True)),
                ('telefono_enfermero', models.CharField(max_length=15)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('cedula_medico', models.BigIntegerField(primary_key=True, serialize=False, unique=True)),
                ('nombres_medico', models.CharField(max_length=100)),
                ('apellidos_medico', models.CharField(max_length=100)),
                ('genero', models.CharField(blank=True, max_length=5, null=True)),
                ('telefono_medico', models.CharField(max_length=15)),
                ('especialidad', models.CharField(max_length=20)),
                ('registro_medico', models.BigIntegerField(unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('cedula_paciente', models.BigIntegerField(primary_key=True, serialize=False, unique=True)),
                ('nombres_paciente', models.CharField(max_length=100)),
                ('apellidos_paciente', models.CharField(max_length=100)),
                ('genero', models.CharField(blank=True, max_length=5, null=True)),
                ('telefono_paciente', models.CharField(max_length=15)),
                ('fecha_de_nacimiento', models.CharField(max_length=45)),
                ('ciudad', models.CharField(max_length=45)),
                ('direccion', models.CharField(max_length=100)),
                ('latitud', models.CharField(blank=True, max_length=45, null=True)),
                ('longitud', models.CharField(blank=True, max_length=45, null=True)),
                ('id_enfermero', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hec_backend.enfermero')),
                ('id_medico', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hec_backend.medico')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SugerenciasCuidado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_sugerencia', models.DateField()),
                ('sugerencia', models.TextField(max_length=500)),
                ('id_paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hec_backend.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='SignosVitales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_muestra', models.DateField()),
                ('oximetria', models.FloatField()),
                ('freq_respiratoria', models.FloatField()),
                ('freq_cardiaca', models.FloatField()),
                ('temperatura', models.FloatField()),
                ('presion_arterial', models.CharField(max_length=10)),
                ('glicemias', models.FloatField()),
                ('id_paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hec_backend.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('cedula_familiar', models.BigIntegerField(primary_key=True, serialize=False, unique=True)),
                ('nombres_familiar', models.CharField(max_length=100)),
                ('apellidos_familiar', models.CharField(max_length=100)),
                ('genero', models.CharField(blank=True, max_length=5, null=True)),
                ('telefono_familiar', models.CharField(max_length=15)),
                ('parentesco', models.CharField(max_length=20)),
                ('id_paciente', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hec_backend.paciente')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Diagnostico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_diagnostico', models.DateField()),
                ('diagnostico', models.TextField(max_length=500)),
                ('id_paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hec_backend.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Enfermeroproxy',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('hec_backend.user',),
            managers=[
                ('enfermero', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Familiarproxy',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('hec_backend.user',),
            managers=[
                ('familiar', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Medicoproxy',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('hec_backend.user',),
            managers=[
                ('medico', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Pacienteproxy',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('hec_backend.user',),
            managers=[
                ('paciente', django.db.models.manager.Manager()),
            ],
        ),
    ]
