import os
from celery import shared_task
from django.core.mail import send_mail
from .models import EmailRequestItem
from .exceptions import SuccessException


@shared_task
def send_email_task(email_request_item_id):
    try:

        email_request_item = EmailRequestItem.objects.get(
            email_request_item_id=email_request_item_id)
        email_id = email_request_item.subscriber_id.email

        if email_request_item.status == 'SUCCESS':
            raise SuccessException(f'Campaign already Sent to user')

        print(email_id)

        subject = email_request_item.email_request_id.campaign_id.subject

        # Email body template?
        message = f'{email_request_item.email_request_id.campaign_id.plain_text_content} \
                    \n\nPublished at: {email_request_item.email_request_id.campaign_id.published_date} by {email_request_item.email_request_id.campaign_id.article_url}'
        from_email = os.environ.get('EMAIL_EMAIL')

        # send_mail(subject, message, from_email, recipient)

        email_request_item.status = 'SUCCESS'
        email_request_item.save()

        return f'Mail sent successfully to {email_id}'

    except SuccessException as error:
        return f'Error: {str(error)}. Mail un-successful to {email_id}.'

    except Exception as error:
        email_request_item.status = 'FAILED'
        email_request_item.save()
        return f'Error: {str(error)}. Mail un-successful to {email_id}.'
