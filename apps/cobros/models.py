from django.db import models
from apps.usuarios.models import Cliente, banco_choices


class TarjetaBancaria(models.Model):
	numero = models.CharField(primary_key=True,max_length=50)
	rut = models.ForeignKey(Cliente, on_delete=models.CASCADE)
	banco = models.CharField(max_length=50, choices=banco_choices)

	def __str__(self):
                return str(self.rut)

class TarjetaPrepago(models.Model):	
	rut = models.ForeignKey(Cliente, on_delete=models.CASCADE)
	numero = models.CharField(null=True,max_length=50)
	saldo = models.CharField(null=True,max_length=50)
	fecha_emision = models.DateTimeField(null=True)
        
	def __str__(self):
                return self.numero
	
                   


class Membresia(models.Model):
	numero = models.CharField(primary_key=True, max_length=15)
	fecha_vencimiento = models.DateTimeField()
	fecha_inicio = models.DateTimeField()
	estado = models.CharField(max_length=15)
	rut = models.ForeignKey(Cliente, on_delete=models.CASCADE)

	def __str__(self):
                return 'nº '+ self.numero



