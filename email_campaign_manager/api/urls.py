from django.urls import path
from .views import Subscribers
from send_mail.views import send_email, resend_email

urlpatterns = [
    path('subscribers/<int:subscriber_id>',
         Subscribers.update_subscriber, name='update_subscriber'),
    path('campaign/<int:campaign_id>/send-email',
         send_email, name='send-email'),
    path('email-request/<int:email_request_id>/resend-email',
         resend_email, name='resend-email'),
]
