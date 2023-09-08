from django.db import models
from api.models import Campaign, Subscriber


class EmailRequest(models.Model):
    email_request_id = models.AutoField(primary_key=True)
    campaign_id = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.email_request_id)


class EmailRequestItem(models.Model):
    email_request_item_id = models.AutoField(primary_key=True)
    email_request_id = models.ForeignKey(
        EmailRequest, on_delete=models.CASCADE)
    subscriber_id = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20, default='IN_PROGRESS')  # Initial status
    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.email_request_item_id)
