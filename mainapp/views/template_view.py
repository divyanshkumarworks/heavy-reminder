from django.shortcuts import render, get_object_or_404
from mainapp.models.task import Task
from mainapp.models.task_user import TaskUser
from datetime import datetime
from django.http import HttpResponseRedirect

import pytz

def home(request):	

	token = request.COOKIES.get('jwt_token')

	if token:

		tz_kt = pytz.timezone('Asia/Kolkata')
		current_date = datetime.now(tz_kt).strftime("%#d")
		current_month = datetime.now(tz_kt).strftime("%b").upper()

		context = {
			"date": current_date,
			"month": current_month
		}

		return render(request,"mainapp/home.html", context)
	else:
		return HttpResponseRedirect('/login')

def add_task(request):
	return render(request, "mainapp/add_task.html")

def update_task(request, task_id):
	obj = get_object_or_404(Task, id=task_id)
	return render(request, "mainapp/update_task.html", {'obj': obj})

def profile(request):
	token = request.COOKIES.get('jwt_token')

	if token:
		return render(request, "mainapp/profile.html")
	else:
		return HttpResponseRedirect('/login')

def login(request):
	return render(request, "mainapp/login.html")