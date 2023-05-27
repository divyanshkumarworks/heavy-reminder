from django.db import models

class Repeat(models.Model):
	label = models.CharField(max_length=10)

	def __str__(self):
		return f"{self.label}"
