from django.contrib import admin
from mainapp.models import *


admin.site.register(Priority)
admin.site.register(Task)
admin.site.register(Reminder)
admin.site.register(Repeat)
admin.site.register(TaskUser)
