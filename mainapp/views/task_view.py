import datetime
import json

from django.http import JsonResponse
from mainapp.models import *
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from django.views import View


from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class TaskView(View):
	def get(self, request):
		tasks = Task.objects.all()

		data = {
			"tasks": []
		}

		for task in tasks:
			data["tasks"].append(
					{
						"name": task.name,
						"id": task.id,
						"start_time": task.start_time,
						"duration": task.duration,
						"status": task.status,
						"priority": str(task.priority)
					}
				)

		return JsonResponse(data)

	def post(self, request):
		data = json.loads(request.body)
		name = data["name"]
		start_time = data["start_time"]
		duration = data["duration"]
		status = data["status"]
		priority = data["priority"]
		user_id = data["user"]
		repeat = data["repeat"]
		
		task_user = TaskUser.objects.get(id=user_id)

		priority = Priority.objects.get(label=priority)
		
		repeat = Repeat.objects.get(label=repeat)
		
		with transaction.atomic():
			task = Task(name=name, start_time=start_time, duration=duration, status=status, priority=priority, user=task_user, repeat=repeat)
			task.save()
			reminder = Reminder(time=start_time, task=task, priority=priority, status=status)
			reminder.save()

		return JsonResponse({"message":"success"})

	def put(self, request, task_id):
		data = json.loads(request.body)
		name = data["name"]
		start_time = data["start_time"]
		duration = data["duration"]
		status = data["status"]
		priority = data["priority"]
		user_id = data["user"]
		repeat = data["repeat"]

		priority = Priority.objects.get(label=priority)
		repeat = Repeat.objects.get(label=repeat)
		task_user = TaskUser.objects.get(id=user_id)

		task = Task.objects.get(id=task_id)

		task.name = name
		task.status = status
		task.duration = duration
		task.priority = priority
		task.repeat = repeat
		task.user = task_user
		task.start_time = start_time
		task.save()

		return JsonResponse({"message": "success"})

	def delete(self, request, task_id):
		task = Task.objects.get(id=task_id)

		task.delete()
		return JsonResponse({"message": "task deleted"})
