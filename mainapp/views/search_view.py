from django.http import JsonResponse
from mainapp.models import Task
import json
from django.views.decorators.csrf import csrf_exempt
import datetime

	

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