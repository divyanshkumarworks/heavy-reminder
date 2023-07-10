# heavy-reminder

## About
This is webbase refernce app built in Django and Javascript demonstrates how to leverage [Twilio Programmable Voice](https://www.twilio.com/voice) and [Twilio SDKs](https://www.twilio.com/docs/libraries) to create a Task reminder system to remind people about the tasks by calling to your customers to deliver time-sensitive messages. This app is helpful for people who need to be reminding about the tasks.

### How it works
This fully functional webapp allows you to create tasks and set a reminder for it. Users can sign-up via mobile number, create tasks and set a reminder for a specified date and time, the app then calls the user on their phone to remind about the task. 

### Technology stack

- [Python](https://www.python.org/)
- [Twilio](https://www.twilio.com/docs/voice)
- [Django](https://www.djangoproject.com/start/)
- [Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/)

Please note that using the application will incur in charges for Programmable Voice minutes.

## Screenshots

📌 Login Page

![Screenshot (40)](https://github.com/divyanshkumarworks/watch-with-me/assets/134360630/9b6fd51a-c978-4c7a-bca3-fb7d98481b5c)

📌 Home Page

![Screenshot (39)](https://github.com/divyanshkumarworks/HowWeLookTogether/assets/134360630/abacbc48-8846-4e07-9ded-bde3c3acec77)

📌 Add Task Page

![Screenshot (42)](https://github.com/divyanshkumarworks/watch-with-me/assets/134360630/71b977f7-52f0-49cb-af99-72b088bc4479)


## Getting Started: 🚀

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites 📋
1. first of all, You need to install python for running pip command
2. create a project folder  

### Local Development
1. Clone the repository inside this folder
```bash
https://github.com/divyanshkumarworks/heavy-reminder.git
```

2. Install Dependencies
```bash
pip3 install -r requirements.txt
```
3. This application uses Twilio credentials to create the Call resources. you'll need a [Twilio](https://www.twilio.com/en-us) account for:
- account sid
- auth token
- twilio number

4. After creating an account in twilio create a secret.py file inside folder heavy reminder and add following credentials: 

```bash
ACCOUNT_SID = XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
AUTH_TOKEN = XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

TWILIO_NUMBER = XXXXXXXXXX
MY_NUMBER = XXXXXXXXXXX

(your secret key stored inside settings.py)
DJANGO_SECRET_KEY = XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```
5. Run database migrations using:
```bash
python manage.py makemigrations

python manage.py migrate
```
it will create the database schemas, tables and relationships. 

6. And then run:
```bash
python manage.py runserver
```
this command will run the local server. 

In addition, An ngrok server is required so that Twilio can locate your server and invoke the webhooks on every call status update.

### Other

- For local development the application uses an [ngrok server](https://ngrok.com/). Without it, Twilio cannot invoke the call-status-update webhook that runs from your local server. Ngrok [enforces a limit of 40 connections per minute](https://ngrok.com/pricing#:~:text=Per%20user%20limits%3A,-5%20reserved%20domains&text=2%20online%20ngrok%20processes,120%20connections%2Fminute) so be mindful about this limitation.
