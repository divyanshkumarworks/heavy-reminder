from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .variables import OTPS
from mainapp.models import *
from .otp_generate import get_otp
from django.db import transaction

import json
import jwt
import random

@csrf_exempt
def login_api(request):
	data = json.loads(request.body)
	otp = data["otp"]

	if otp in OTPS.values():
		user_number = 0
		for key, value in OTPS.items():
			user_number += int(key)

		if not TaskUser.objects.filter(phone_no=user_number).exists():
			with transaction.atomic():
				user = TaskUser(phone_no=user_number, username=user_number)
				user.save()
				print("user created")

		payload_data = {  
		  "sub": "1",  
		  "phone_no": user_number,  
		  "otp": otp 
		}  
		
		token = jwt.encode(
			payload=payload_data,
			key = "my_secret_key"  
			)

		response = JsonResponse({"token": token})   
		response.set_cookie("jwt_token", token)
		print("this is ", response.__dict__)
		return response
	else:
		return JsonResponse({"mesage": "not in OTPS"})

		



