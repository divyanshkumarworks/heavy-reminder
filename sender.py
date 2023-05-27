from twilio.rest import Client
from heavy_reminder.wsgi import *
from mainapp.models import Task, Reminder
from datetime import datetime
from secrets import *

account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN

twilio_number = TWILIO_NUMBER
my_number = MY_NUMBER

client = Client(account_sid, auth_token)

tasks = Task.objects.all()
reminders = Reminder.objects.all()

current_datetime = datetime.now().strftime("%m/%d/%Y %H:%M")

say_text = "<Response><Say>Hello there this is a test call</Say></Response>"

for reminder in reminders:
	time = reminder.time.strftime("%m/%d/%Y %H:%M")
	print(time)
	if time == current_datetime:
		message = client.calls.create(
			twiml=say_text,	
			from_=twilio_number,
			to=my_number
		)

print(current_datetime)
