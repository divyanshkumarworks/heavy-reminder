from mainapp.models import *
from twilio.twiml.voice_response import VoiceResponse, Gather
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from datetime import datetime

@csrf_exempt
def voice(request, reminder_id):
    print(request.POST)
    called_number = request.POST.get('To')

    reminder = Reminder.objects.get(id=reminder_id)
    reminder.status = 'IN_PROGRESS'
    reminder.save()

    gather = Gather(num_digits=1, action=f'/twilio/process_input/{reminder_id}', method='POST')
    gather.say('Press 1 to start your task')
    gather.say('Press 2 to set your task on hold')
    print(gather)

    response = VoiceResponse()
    response.append(gather)

    return HttpResponse(str(response), content_type='text/xml')