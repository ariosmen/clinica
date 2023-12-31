# Generated by Django 4.2.4 on 2023-09-05 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especialidad', models.CharField(max_length=50, unique=True, verbose_name='Especialidad')),
                ('create', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'especialidad',
                'verbose_name_plural': 'especialidades',
                'db_table': 'especialidades',
                'ordering': ['especialidad'],
            },
        ),
    ]
