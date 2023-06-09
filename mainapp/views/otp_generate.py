import random
import json

from .variables import OTPS
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.rest import Client
from heavy_reminder.secrets import *

account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN

twilio_number = TWILIO_NUMBER
my_number = MY_NUMBER

client = Client(account_sid, auth_token)

@csrf_exempt
def get_otp(request):	
	print("requesting otp")
	if request.method == "POST":
		data = json.loads(request.body)
		number = random.randint(0, 9999)

		user_number = data["phone_number"]
		print("entered number: ", user_number)
		otp = str(number).zfill(4)
		OTPS[user_number] = otp
		print(otp)
		
		message = client.messages.create(
			body=f"you otp for heavy reminder is {otp}",
			from_=twilio_number,
			to=my_number,
		)
		print("otp sent to user")
		return JsonResponse({"OTPS": OTPS})
