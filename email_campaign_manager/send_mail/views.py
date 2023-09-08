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
def resend_email(request, email_request_id):
    try:
        if request.method == 'POST':

            email_request = get_object_or_404(
                EmailRequest, pk=email_request_id)

            create_email_req_items(
                email_request, resend=True)

            # Create batches to handle load
            email_request_items = email_request.emailrequestitem_set.all()
            batches = create_batches(email_request_items)

            # Celery tasks to send emails concurrently
            for batch in batches:
                tasks = [send_email_task.s(email_request_item.email_request_item_id)
                         for email_request_item in batch]
                group(tasks)()

            return HttpResponse('Sending email campaign to Subscribers', status=200)
        else:
            return HttpResponse('Only available for POST requests', status=405)
    except Exception as error:
        return HttpResponse(error, status=500)


@user_passes_test(is_admin, login_url='http://127.0.0.1:8000/admin/')
def send_email(request, campaign_id):
    try:
        if request.method == 'POST':
            campaign = get_object_or_404(Campaign, pk=campaign_id)

            email_request = EmailRequest.objects.create(campaign_id=campaign)
            create_email_req_items(email_request)

            # Create batches to handle load
            email_request_items = email_request.emailrequestitem_set.all()
            batches = create_batches(email_request_items)

            # Celery tasks to send emails concurrently
            for batch in batches:
                tasks = [send_email_task.s(email_request_item.email_request_item_id)
                         for email_request_item in batch]
                group(tasks)()

            return HttpResponse('Sending email campaign to Subscribers', status=200)
        else:
            return HttpResponse('Only available for POST requests', status=405)
    except Exception as error:
        return HttpResponse(error, status=500)


def create_batches(email_request_items, size=10):
    return [email_request_items[i:i + size] for i in range(0, len(email_request_items), size)]


def create_email_req_items(email_request, resend=False):
    try:

        active_subscribers = Subscriber.objects.filter(is_active=True)
        # Create request items for each subscriber
        email_request_items = []
        for subscriber in active_subscribers:
            email_request_item = EmailRequestItem.objects.filter(
                email_request_id=email_request, subscriber_id=subscriber).first()

            if (email_request_item and resend):
                continue

            email_request_items.append(EmailRequestItem(
                email_request_id=email_request,
                subscriber_id=subscriber))
        EmailRequestItem.objects.bulk_create(email_request_items)

        return email_request
    except Exception as error:
        return error
