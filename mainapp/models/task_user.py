from django.db import models

class TaskUser(models.Model):
	name = models.CharField(max_length=20)
	phone_no = models.IntegerField(unique=True)
	guardian1_no = models.IntegerField()
	guardian2_no = models.IntegerField()

	def __str__(self):
		return f"{self.name}"
