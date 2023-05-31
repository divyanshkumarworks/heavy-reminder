"""heavy_reminder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mainapp.views.task_view import TaskView
from mainapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/task', TaskView.as_view(), name="create-task-api"),
    path('api/task/<int:task_id>', TaskView.as_view(), name="update-delete-task-api"),
    path('api/search', views.search_task_api, name="search-task-api"),
    path('twilio/voice/<int:reminder_id>', views.voice, name="twilio-voice"),
    path('twilio/process_input/<int:reminder_id>', views.process_input, name="twilio-process-input")
]


