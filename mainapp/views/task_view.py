from django.http import JsonResponse
from mainapp.models import *
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from django.views import View

import datetime
import json
import jwt

from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class TaskView(View):
	def get(self, request):		
		token = request.COOKIES.get('jwt_token')
		print("OK")	
		print("this is token :", token)
		if token:	
			payload = jwt.decode(
				token,
				key="my_secret_key",
				algorithms=["HS256"]
				)
			
			user_number = payload["phone_no"]
			print(user_number)
			user = TaskUser.objects.get(phone_no=user_number)
			print(user.id)
			user_id = user.id

			try:
				tasks = Task.objects.filter(user=user_id)
			except Task.DoesNotExist:
				tasks = None

			data = {
				"tasks": []
			}

			for task in tasks:
				data["tasks"].append(
						{
							"name": task.name,
							"id": task.id,
							"start_time": task.start_time,
							"status": task.status,
							"priority": str(task.priority),
							"repeat": str(task.repeat)
						}
					)

			return JsonResponse(data)
		else:
			return JsonResponse({'error': 'not found'}, status=404)
		

	def post(self, request):
		
		data = json.loads(request.body)

		name = data["task_name"]
		start_time = data["start_time"]
		priority = data["priority"]
		repeat = data["repeat"]


		token = request.COOKIES.get('jwt_token')
		print(token)
		print("OK")

		if token:	
			payload = jwt.decode(
				token,
				key="my_secret_key",
				algorithms=["HS256"]
				)
			
			user_number = payload["phone_no"]
			task_user = TaskUser.objects.get(phone_no=user_number)

			priority = Priority.objects.get(label=priority)
			
			repeat = Repeat.objects.get(label=repeat)
			
			with transaction.atomic():
				task = Task(name=name, start_time=start_time, status="NOT STARTED", priority=priority, user=task_user, repeat=repeat)
				task.save()
				reminder = Reminder(time=start_time, task=task, priority=priority, status="PENDING")
				reminder.save()

			return JsonResponse({"message":"success"})
		else:
			return JsonResponse({'error': 'not found'}, status=404)


	def put(self, request, task_id):
		data = json.loads(request.body)
		name = data["task_name"]
		start_time = data["start_time"]
		priority = data["priority"]
		repeat = data["repeat"]

		token = request.COOKIES.get('jwt_token')

		if token:	
			payload = jwt.decode(
				token,
				key="my_secret_key",
				algorithms=["HS256"]
				)
			
			user_number = payload["phone_no"]
			task_user = TaskUser.objects.get(phone_no=user_number)


			priority = Priority.objects.get(label=priority)
			repeat = Repeat.objects.get(label=repeat)

			task = Task.objects.get(id=task_id)

			task.name = name
			task.priority = priority
			task.repeat = repeat
			task.user = task_user
			task.start_time = start_time
			task.save()

			return JsonResponse({"message": "success"})
		else:
			return JsonResponse({'error': 'not found'}, status=404)

	def delete(self, request, task_id):

		token = request.COOKIES.get('jwt_token')

		if token:	
			payload = jwt.decode(
				token,
				key="my_secret_key",
				algorithms=["HS256"]
				)

			task = Task.objects.get(id=task_id)

			task.delete()
			return JsonResponse({"message": "task deleted"})

		else:
			return JsonResponse({'error': 'not found'}, status=404)