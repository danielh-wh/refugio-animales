from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Persona(models.Model):
	nombre = models.CharField(max_length=60)
	apellidos = models.CharField(max_length=70)
	edad = models.IntegerField()
	telefono = models.CharField(max_length=12)
	email = models.EmailField()
	domicilio = models.TextField()
	imagen_perfil = models.ImageField(null=True, blank=True)


	def __unicode__(self):
		return '{} {}'.format(self.nombre, self.apellidos)

class Solicitud(models.Model):
	persona = models.ForeignKey(Persona, null=True, blank=True)
	numero_mascotas = models.IntegerField()
	razones = models.TextField()