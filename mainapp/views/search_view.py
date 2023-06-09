from django.http import JsonResponse
from mainapp.models import Task
from django.views.decorators.csrf import csrf_exempt

import datetime
import json
import jwt
	

@csrf_exempt
def search_task_api(request):
	if request.method == "POST":
		data = json.loads(request.body)
		task_name = data["task_name"]

		token = request.COOKIES.get('jwt_token')

		if token:	
			payload = jwt.decode(
				token,
				key="my_secret_key",
				algorithms=["HS256"]
				)

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
							"status": task.status,
							"priority": str(task.priority),
							"repeat": str(task.repeat)
						}
					)
			print("enter this loop")


			return JsonResponse(data)
		else:
			return JsonResponse({'error': 'not found'}, status=404)