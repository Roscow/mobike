from django.db import models
from django.utils import timezone


genero_choices= {('m','Masculino'),('f','Femenino')}
banco_choices= {('be','Banco Estado'),('bc','Banco de Chile')}
comunas_choices = {('lr','La Reina'),('Lc','Las Condes'),('ññ','Ñuñoa')}

class Usuario(models.Model):
	run = models.CharField(primary_key=True, max_length=50)
	nombre1 = models.CharField(max_length=50)
	nombre2 = models.CharField(max_length=50)
	apellido1 = models.CharField(max_length=50)
	apellido2 = models.CharField(max_length=50)	
	fecha_nacimiento = models.DateTimeField(blank=True, null=False)
	dv = models.CharField(max_length=1)
	direccion = models.CharField(max_length=50)
	correo = models.EmailField(max_length=50)
	telefono = models.CharField(max_length=50)
	genero = models.CharField(choices=genero_choices, max_length=20)
		
	def publish(self):
                self.save()
        
	def __str__(self):
                return self.run
                   
class Cliente(Usuario):
	estado =models.CharField(max_length=50)
	comuna_trabajo = models.CharField(max_length=50,choices=comunas_choices)
	comuna_domicilio = models.CharField(max_length=50,choices=comunas_choices)
	sanciones = models.IntegerField()
	
	def __str__(self):
                return self.run

class Cargo(models.Model):
	idCargo = models.CharField(null=True,max_length=50)
	nombre = models.CharField(null=True,max_length=50);

	def __str__(self):
                return self.nombre

class Empleado(Usuario):
	fecha_contratacion = models.DateTimeField()
	idCargo = models.ForeignKey(Cargo,on_delete=models.CASCADE)
	def __str__(self):
                return self.nombre1 + ' ' +self.apellido1   

class Cuenta(models.Model):	
	rut = models.ForeignKey(Usuario,unique=True,on_delete=models.CASCADE)
	usuario = models.CharField(null=False,max_length=20)
	contraseña = models.CharField(null=False, max_length=20)	
        
	def __str__(self):
                return self.usuario     
