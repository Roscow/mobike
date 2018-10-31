# Generated by Django 2.1.2 on 2018-10-31 00:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idCargo', models.CharField(max_length=50, null=True)),
                ('Nombre', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=20)),
                ('contraseña', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Membresia',
            fields=[
                ('numero', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('fecha_vencimiento', models.DateTimeField()),
                ('fecha_inicio', models.DateTimeField()),
                ('estado', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='TarjetaBancaria',
            fields=[
                ('numero', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('banco', models.CharField(choices=[('be', 'Banco Estado'), ('bc', 'Banco de Chile')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TarjetaPrepago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=50, null=True)),
                ('saldo', models.CharField(max_length=50, null=True)),
                ('fecha_emision', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('run', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nombre1', models.CharField(max_length=50)),
                ('nombre2', models.CharField(max_length=50)),
                ('apellido1', models.CharField(max_length=50)),
                ('apellido2', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateTimeField(blank=True)),
                ('dv', models.CharField(max_length=1)),
                ('direccion', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=50)),
                ('telefono', models.CharField(max_length=50)),
                ('genero', models.CharField(choices=[('f', 'Femenino'), ('m', 'Masculino')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='usuarios.Usuario')),
                ('estado', models.CharField(max_length=50)),
                ('comunaTrabajo', models.CharField(max_length=50)),
                ('comunaDomicilio', models.CharField(max_length=50)),
                ('sanciones', models.IntegerField()),
            ],
            bases=('usuarios.usuario',),
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='usuarios.Usuario')),
                ('fecha_contratacion', models.DateTimeField()),
                ('idCargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Cargo')),
            ],
            bases=('usuarios.usuario',),
        ),
        migrations.AddField(
            model_name='cuenta',
            name='rut',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Usuario', unique=True),
        ),
        migrations.AddField(
            model_name='tarjetaprepago',
            name='rut',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Cliente'),
        ),
        migrations.AddField(
            model_name='tarjetabancaria',
            name='rut',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Cliente'),
        ),
        migrations.AddField(
            model_name='membresia',
            name='rut',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Cliente'),
        ),
    ]