from django.db import models
from .task_user import TaskUser
from .priority import Priority
from .repeat import Repeat

class Task(models.Model):
	name = models.CharField(max_length=20)
	user = models.ForeignKey(TaskUser, on_delete=models.CASCADE)
	priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
	start_time = models.DateTimeField()
	status = models.CharField(max_length=20)
	repeat = models.ForeignKey(Repeat, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return f"{self.name}"
