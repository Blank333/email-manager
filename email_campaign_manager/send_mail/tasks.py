from celery import shared_task
from django.core.mail import send_mail
from django.http import HttpResponse


@shared_task
def send_email_task(subject, message, from_email, recipient):
    try:
        send_mail(subject, message, from_email, recipient)
        return f'Mail sent successfully to {recipient}'
    except Exception as error:
        return f'Mail un-successful to {recipient}. Error: {str(error)}'
