from django.shortcuts import render, get_object_or_404
from mainapp.models.task import Task
from mainapp.models.task_user import TaskUser
from datetime import datetime

import pytz

def home(request):	
	tz_kt = pytz.timezone('Asia/Kolkata')
	current_date = datetime.now(tz_kt).strftime("%#d")
	current_month = datetime.now(tz_kt).strftime("%b").upper()

	context = {
		"date": current_date,
		"month": current_month
	}

	return render(request,"mainapp/home.html", context)

def add_task(request):
	return render(request, "mainapp/add_task.html")

def update_task(request, task_id):
	obj = get_object_or_404(Task, id=task_id)
	return render(request, "mainapp/update_task.html", {'obj': obj})

def register(request):
	return render(request, "mainapp/register.html")

def profile(request):
	return render(request, "mainapp/profile.html")

def login(request):
	return render(request, "mainapp/login.html")