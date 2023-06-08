from twilio.rest import Client
from heavy_reminder.wsgi import *
from mainapp.models import Task, Reminder
from datetime import datetime
from heavy_reminder.secrets import *

import pytz

print(f"starting reminder script at {datetime.now()}")

account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN

twilio_number = TWILIO_NUMBER
my_number = MY_NUMBER

client = Client(account_sid, auth_token)

reminders = Reminder.objects.filter(status="PENDING")
tz_kt = pytz.timezone('Asia/Kolkata')
current_datetime = datetime.now(tz_kt).strftime("%m/%d/%Y %H:%M")

for reminder in reminders:
	time = reminder.time.strftime("%m/%d/%Y %H:%M")
	print(f"reminder_date = {time}")
	if current_datetime == time:
		message = client.calls.create(
			url=f"https://0007-2401-4900-1c33-9bf-912c-1a69-2518-17b8.ngrok-free.app/twilio/voice/{reminder.id}",	
			from_=twilio_number,
			to=my_number,
			method="POST"
		)

print(f"current_date = {current_datetime}")

print(f"finished reminder script at {datetime.now()}")
