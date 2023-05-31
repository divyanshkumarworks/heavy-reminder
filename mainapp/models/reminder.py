from django.db import models
from .task import Task
from .priority import Priority

class Reminder(models.Model):
	time = models.DateTimeField()
	task = models.ForeignKey(Task, on_delete=models.CASCADE)
	priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
	status = models.CharField(max_length=20) # PENDING, IN_PROGRESS, DONE

	def __str__(self):
		return f"{self.time}"
