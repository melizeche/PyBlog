from django.db import models

# Create your models here.
class Autor(models.Model):
	nombre 	= models.CharField(max_length=50)
	edad	= models.IntegerField(null=True, blank=True)
	email	= models.EmailField()

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name_plural = "Autores"


class Articulo(models.Model):
	autor 	= models.ForeignKey('Autor', null=True)
	titulo 	= models.CharField(max_length=100)	
	texto 	= models.TextField(blank=True, null=True)
	created	= models.DateTimeField('Agregado',auto_now_add=True, null=True, blank=True)

	def __unicode__(self):
		return self.titulo
