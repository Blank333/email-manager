from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .tasks import send_email_task
from celery import group
from api.models import Campaign, Subscriber
from .models import EmailRequest, EmailRequestItem


def is_admin(user):
    return user.is_authenticated and user.is_superuser


@user_passes_test(is_admin, login_url='http://127.0.0.1:8000/admin/')
def email(request, campaign_id):
    try:
        if request.method == 'POST':
            campaign = get_object_or_404(Campaign, pk=campaign_id)

            # Filter only the subscribed users
            active_subscribers = Subscriber.objects.filter(is_active=True)

            email_request = create_email_req(campaign, active_subscribers)

            # Celery tasks to send emails concurrently
            tasks = [send_email_task.s(email_request_item.email_request_item_id)
                     for email_request_item in email_request.emailrequestitem_set.all()]

            group(tasks)()

            return HttpResponse('Sending email campaign to Subscribers', status=200)
        else:
            return HttpResponse('Only available for POST requests', status=405)
    except Exception as error:
        return HttpResponse(error, status=500)


def create_email_req(campaign, active_subscribers):
    try:
        email_request = EmailRequest.objects.filter(
            campaign_id=campaign).first()
        if not email_request:
            email_request = EmailRequest.objects.create(
                campaign_id=campaign)

        # Create request items for each subscriber
        email_request_items = []
        for subscriber in active_subscribers:
            if (EmailRequestItem.objects.filter(email_request_id=email_request, subscriber_id=subscriber).first()):
                continue

            email_request_items.append(EmailRequestItem(
                email_request_id=email_request,
                subscriber_id=subscriber))
        EmailRequestItem.objects.bulk_create(email_request_items)

        return email_request
    except Exception as error:
        return error
