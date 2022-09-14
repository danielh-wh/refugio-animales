from __future__ import unicode_literals

from django.db import models

from app.adopcion.models import Persona


class Vacuna(models.Model):
	nombre = models.CharField(max_length=50)
	def __unicode__(self):
		return '{}'.format(self.nombre)

class Mascota(models.Model):
	#folio = models.CharField(max_length=10, primary_key=True)
	nombre = models.CharField(max_length=50)
	genero = models.CharField(max_length=10)
	edad_aproximada = models.IntegerField()
	fecha_rescate = models.DateField()

	persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
	vacuna = models.ManyToManyField(Vacuna, blank=True)