from twilio.twiml.voice_response import VoiceResponse, Gather
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from mainapp.models import *
from datetime import datetime, timedelta
from django.db import transaction

import pytz

@csrf_exempt
def process_input(request, reminder_id):
    
    response = VoiceResponse()

    digit_pressed = request.POST.get('Digits', '')
    called_number = request.POST.get('To')
    reminder = Reminder.objects.get(id=reminder_id)
    priority = reminder.task.priority.id
    task = reminder.task
    max_priority = 0

    # Perform actions based on the received digit
    if digit_pressed:
        
        if digit_pressed == '1':

            # setting task to in progress
            response.say('your task is started now, setting status to in progress')
            task.status = 'IN_PROGRESS'
            task.save()
            reminder.status = 'DONE'
            reminder.save()

            return HttpResponse(str(response), content_type='text/xml')
        
        elif digit_pressed == '2':
            
            # settting new reminder 
            response.say('you have set your task on hold')
            response.say('setting reminder with new priority')

            kolkata_tz = pytz.timezone('Asia/Kolkata')
            new_time = datetime.now(kolkata_tz) + timedelta(minutes = 5)
            formatted_time = new_time.strftime('%Y-%m-%d %H:%M:%S')
            
            priority += 1
            max_priority = max(max_priority, priority)
            new_priority = Priority.objects.get(id=max_priority)

            with transaction.atomic():
                reminder = Reminder(time=formatted_time, task=task, priority=new_priority, status='PENDING')
                reminder.save()
            return HttpResponse(str(response), content_type='text/xml')
    

    # Add more conditions as needed
    response.say('Thank you for your input.')

    return HttpResponse(str(response), content_type='text/xml')