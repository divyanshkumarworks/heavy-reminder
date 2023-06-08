from django.db import models
from django.contrib.auth.models import AbstractUser

class TaskUser(AbstractUser):
	phone_no = models.CharField(max_length=20)

	def __str__(self):
		return f"{self.phone_no}"