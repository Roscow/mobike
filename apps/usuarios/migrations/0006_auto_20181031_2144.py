# Generated by Django 2.1.2 on 2018-10-31 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_auto_20181031_2127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membresia',
            name='rut',
        ),
        migrations.RemoveField(
            model_name='tarjetabancaria',
            name='rut',
        ),
        migrations.RemoveField(
            model_name='tarjetaprepago',
            name='rut',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='genero',
            field=models.CharField(choices=[('m', 'Masculino'), ('f', 'Femenino')], max_length=20),
        ),
        migrations.DeleteModel(
            name='Membresia',
        ),
        migrations.DeleteModel(
            name='TarjetaBancaria',
        ),
        migrations.DeleteModel(
            name='TarjetaPrepago',
        ),
    ]
