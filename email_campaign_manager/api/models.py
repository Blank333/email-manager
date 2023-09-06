from django.db import models


class Subscriber(models.Model):
    subscriber_id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Campaign(models.Model):
    campaign_id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=255)
    preview_text = models.TextField()
    article_url = models.URLField()
    html_content = models.TextField()
    plain_text_content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject
