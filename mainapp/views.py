from django.shortcuts import render 
from django.http import JsonResponse
from .models import Task, Priority, Repeat, TaskUser, Reminder
import json
from django.views.decorators.csrf import csrf_exempt
import datetime
from rest_framework.decorators import api_view
from django.db import transaction

# Create your views here.
		

@csrf_exempt
def get_create_task_api(request):
	if request.method == "GET":
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

	if request.method == "POST":
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


@csrf_exempt
def update_delete_task_api(request, id):
	if request.method == "PUT":
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

		task = Task.objects.get(id=id)

		task.name = name
		task.status = status
		task.duration = duration
		task.priority = priority
		task.repeat = repeat
		task.user = task_user
		task.start_time = start_time
		task.save()

		return JsonResponse({"message": "success"})

	if request.method == "DELETE":
		task = Task.objects.get(id=id)

		task.delete()
		return JsonResponse({"message": "task deleted"})
	

@csrf_exempt
def search_task_api(request):
	if request.method == "POST":
		data = json.loads(request.body)
		task_name = data["task_name"]
		tasks = Task.objects.filter(name__icontains=task_name)

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
						"priority": str(task.priority),
						"repeat": str(task.repeat)
					}
				)

		return JsonResponse(data)