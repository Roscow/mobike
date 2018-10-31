from django.db import models




estado_choices={('A','Abierto'),('C','Cerrado')}

class Zona(models.Model):
    id_zona = models.CharField(primary_key=True,max_length=50)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    capacidad = models.IntegerField()
    stock = models.IntegerField()
    def __str__(self):
                return str(self.nombre)




class Candado(models.Model):
	numero_candado = models.CharField(primary_key=True, max_length=15)
	zona = models.ForeignKey(Zona,on_delete=models.CASCADE )
	estado = models.CharField(choices=estado_choices,max_length=20)

	def __str__(self):
                return 'nº '+ self.numero




class Bicicleta(models.Model):
    numero_bicicleta = models.CharField(null=True,max_length=50)
    año = models.IntegerField(null=True)
    gps = models.CharField(null=True,max_length=50)
    numero_candado = models.ForeignKey(Candado,on_delete=models.CASCADE)
    def __str__(self):
                return self.numero
	




class Arriendo(models.Model):
    numero_arriendo = models.CharField(primary_key=True,max_length=50)
    valor = models.IntegerField(null=True)
    iva = models.IntegerField(null=True)
    calificacion = models.IntegerField(null=True)
    comentario = models.CharField(max_length=50)
    numero_bicicleta = models.ForeignKey(Bicicleta,on_delete=models.CASCADE )
    id_zona = models.ForeignKey(Zona,on_delete=models.CASCADE )
    def __str__(self):
                return str(self.rut)

