# heavy-reminder

## About
This is webbase refernce app built in Django and Javascript demonstrates how to leverage [Twilio Programmable Voice](https://www.twilio.com/voice) and [Twilio SDKs](https://www.twilio.com/docs/libraries) to create a Task reminder system to remind people about the tasks by calling to your customers to deliver time-sensitive messages. This app is helpful for people who need to be reminding about the tasks.

### How it works
This fully functional webapp allows you to create tasks and set a reminder for it. Users can sign-up via mobile number, create tasks and set a reminder for a specified date and time, the app then calls the user on their phone to remind about the task. 

### Technology stack

- [Python](https://www.python.org/)
- [](https://www.typescriptlang.org/)
- [Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
- [NestJS](https://nestjs.com/)
- [PostgreSQL](https://www.postgresql.org/)


## Getting Started: 🚀

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites 📋

1. Clone this repository
2. Install dependencies
   
   ```bash
   pip3 install -r requirements.txt
   ```

Additionally, you'll need a [Supabase](https://supabase.com/) account for:

- Creating a new Supabase project
- Supabase Project API key
- Supabase Project URL

### Local Development
1. Clone the repository
   ```bash
   
   ```

2. Install Dependencies
$ npm install

This application uses Twilio credentials to create the Call resources. It also requires a PostgreSQL database for storing the notifications and related call data. Add the following parameters to your .env file (use .env.example as a reference):

PASSCODE=XXXXXX
DATABASE_URL=postgres://username:password@hostname:port/dbname
ACCOUNT_SID=ACXXXXXXXXXXXXXXXXXXXXXXX
AUTH_TOKEN=XXXXXXXXXXXXXXXXXXXXXXXXXX
Please note that you may need to install PostgreSQL and start it up or leverage some DBaaS provider to create a free cloud database (such as https://www.elephantsql.com)

3. Install Dependencies
$ npm start

The first time you run the app, it will create the database schemas, tables and relationships. In addition, this command will run the NodeJS server and will expose the ReactJS application via ngrok. An ngrok server is required so that Twilio can locate your server and invoke the webhooks on every call status update.

Alternatively, you can start UI and Server separately for a more granular development experience:

$ npm run start:ui $ npm run start:server
