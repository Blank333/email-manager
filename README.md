# Django Email Campaign Manager

![Django Version](https://img.shields.io/badge/Django-4.2.5-blue.svg)
![Celery Version](https://img.shields.io/badge/Celery-5.3.4-blue.svg)
![Redis Version](https://img.shields.io/badge/Redis-5.0.0-blue.svg)

This is a Django application for managing email campaigns. It allows you to create, schedule, and send email campaigns to a list of subscribers.

## Features

- Create and manage campaigns
- Schedule campaigns for future delivery
- Send campaigns to a list of subscribers concurrently
- Track campaign delivery status for each user
- Resend campaign to users that did not receive it
- Tasks divided into batches over threads

## Installation

### Running through Docker

This repository contains a Dockerized setup for the web application. This allows you to easily deploy and run the application in a containerized environment.
Before you begin, make sure to install [Docker](https://www.docker.com/)

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Blank333/email-manager.git
   cd email-manager/email_campaign_manager
   ```

2. **Environment Variables**
   Create a `.env` file in the project root and configure the necessary environment variables. You can use the provided example as a template.

```.env
DJANGO_SECRET_KEY = ''
DEBUG = True
DJANGO_ALLOWED_HOSTS = 'localhost 127.0.0.1'
DB_NAME = 'campaign'
DB_USER = 'supuser'
DB_PASSWORD = 'root'
DB_HOST = 'db'
DB_PORT = '5432'
DATABASE = 'postgres'

EMAIL_HOST = ''
EMAIL_PORT = ''
EMAIL_USER = ''
EMAIL_PASSWORD = ''
EMAIL_EMAIL = ''

CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
```

3. **Build Docker Images**
   Build the Docker images for the web application and other services.

   ```bash
   docker-compose build
   ```

4. **Start Docker Compose**
   Start all the services using Docker Compose.

   ```bash
   docker-compose up
   ```

   This will start the Django web server, Celery workers, Redis, and Postgresql. Migrations will be carried out and an admin account will be created the first time you use it:

   ```
   username = admin
   password = password
   ```

5. **Restart the Docker app**
   This ensures migrations have been created properly. The application should now be accessible at [http://localhost:8000/admin](http://localhost:8000/admin) in your web browser.

### Manual

1. **Clone the repository**

```bash
git clone https://github.com/Blank333/email-manager.git
cd email-manager/email_campaign_manager
```

2. **Install the required packages**

```bash
pip install -r requirements.txt
```

3. **Apply migrations**
   Make sure you have PostgreSQL and Redis up and running.

```bash
python manage.py migrate
```

4. **Configure environment variables**
   Create a .env file with environment variables. You can also use an SMTP to send real emails. Use the following template.

```.env
DJANGO_SECRET_KEY = ''
DEBUG = True
DJANGO_ALLOWED_HOSTS = 'localhost 127.0.0.1'
DB_NAME = 'campaign'
DB_USER = 'supuser'
DB_PASSWORD = 'root'
DB_HOST = 'db'
DB_PORT = '5432'
DATABASE = 'postgres'

EMAIL_HOST = ''
EMAIL_PORT = ''
EMAIL_USER = ''
EMAIL_PASSWORD = ''
EMAIL_EMAIL = ''

CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
```

5. **Start the development server**

```bash
python manage.py runserver
```

6. **Start celery services**

```bash
celery -A email_campaign_manager worker -l info
celery -A email_campaign_manager beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
```

Access the application at [http://localhost:8000/admin](http://localhost:8000/admin)

## Usage

1. Log in to the Django admin interface.
2. Create campaigns with subject, preview text, article URL, and content.
3. Add subscribers to the list.
4. Schedule or send campaigns to the list of subscribers using API endpoints.
5. Track the status of sent campaigns using Email Requests.

## API Endpoints

`api/v1/subscribers/<subscriber_id>/unsubscribe`
Unsubscriber a user

`api/v1/campaign/<campaign_id>/send-email`
Send a campaign to all subscribers

`api/v1/email-request/<email_request_id>/resend-email`
Resend a created email request incase some users failed to receive the campaign

## Screenshots

![Campaign List](screenshots/campaign_list.png)

![Create Campaign](screenshots/add_campaign.png)

![Subscriber List](screenshots/subscriber_list.png)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
