from django.http import HttpResponse
from django.core.mail import send_mail
import os
from api.models import Campaign, Subscriber
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .tasks import send_email_task
from celery import group


def is_admin(user):
    return user.is_authenticated and user.is_superuser


@user_passes_test(is_admin, login_url='http://127.0.0.1:8000/admin/')
def email(request, campaign_id):
    try:
        if request.method == 'POST':
            campaign = get_object_or_404(Campaign, pk=campaign_id)

            subject = campaign.subject

            # Email body
            message = f'{campaign.plain_text_content} \
                        \n\nPublished at: {campaign.published_date} by {campaign.article_url}'
            from_email = os.environ.get('EMAIL_EMAIL')

            # Filter only the subscribed users
            active_subscribers = Subscriber.objects.filter(is_active=True)
            recipient_list = [
                subscriber.email for subscriber in active_subscribers
            ]

            # Celery tasks to send emails concurrently
            tasks = [send_email_task.s(subject, message, from_email, [
                                       recipient]) for recipient in recipient_list]
            group(tasks)()

            return HttpResponse('Sending email campaign to Subscribers', status=200)
        else:
            return HttpResponse('Only available for POST requests', status=405)
    except Exception as error:
        return HttpResponse(error, status=500)
