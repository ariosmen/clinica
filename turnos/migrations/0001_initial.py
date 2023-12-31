# Generated by Django 4.2.4 on 2023-09-05 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('especialidades', '0001_initial'),
        ('pacientes', '0001_initial'),
        ('medicos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('hora', models.TimeField(verbose_name='Hora')),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('especialidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='especialidades.especialidad', verbose_name='Especialidad')),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicos.medico', verbose_name='Medico')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.paciente', verbose_name='Paciente')),
            ],
            options={
                'verbose_name': 'Turno',
                'verbose_name_plural': 'Turnos',
                'db_table': 'Turnos',
            },
        ),
    ]
