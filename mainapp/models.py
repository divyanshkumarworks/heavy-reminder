from django.db import models
from django.contrib.auth.models import User
from django.db import transaction
# Create your models here.

class TaskUser(models.Model):
	name = models.CharField(max_length=20)
	phone_no = models.IntegerField(unique=True)
	guardian1_no = models.IntegerField()
	guardian2_no = models.IntegerField()

	def __str__(self):
		return f"{self.name}"
 
class Priority(models.Model):
	label = models.CharField(max_length=10)

	def __str__(self):
		return f"{self.label}"

class Repeat(models.Model):
	label = models.CharField(max_length=10)

	def __str__(self):
		return f"{self.label}"

class Task(models.Model):
	name = models.CharField(max_length=20)
	user = models.ForeignKey(TaskUser, on_delete=models.CASCADE)
	priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
	start_time = models.DateTimeField()
	duration = models.TimeField()
	status = models.CharField(max_length=20)
	repeat = models.ForeignKey(Repeat, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return f"{self.name}"

class Reminder(models.Model):
	time = models.DateTimeField()
	task = models.ForeignKey(Task, on_delete=models.CASCADE)
	priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
	status = models.CharField(max_length=20)

	def __str__(self):
		return f"{self.time}"
