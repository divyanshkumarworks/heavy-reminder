from mainapp.models.task_user import TaskUser
from django.http import JsonResponse

import jwt

def me_api(request):
	token = request.COOKIES.get('jwt_token')
		
	if token:	
		payload = jwt.decode(
			token,
			key="my_secret_key",
			algorithms=["HS256"]
			)

		user_number = payload["phone_no"]
		user = TaskUser.objects.get(phone_no=user_number)

		data = {
			"user": {
				"phone_no": user.phone_no
			}
		}

		return JsonResponse(data)
			