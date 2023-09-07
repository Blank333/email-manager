from django.http import HttpResponse
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
import os


def email(request):
    try:
        if request.method == 'POST':

            subject = 'Hello, Mailgun!'
            message = 'This is a test email sent via Mailgun.'
            from_email = os.environ.get('EMAIL_EMAIL')
            recipient_list = ['ceelxx@gmail.com']

            send_mail(subject, message, from_email, recipient_list)
            return HttpResponse("success", status=200)
        else:
            return HttpResponse('Only available for POST requests', status=405)
    except Exception as error:
        return HttpResponse(error, status=500)
