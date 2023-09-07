from django.contrib import admin
from .models import Subscriber, Campaign


class CampaignAdmin(admin.ModelAdmin):
    list_display = ['campaign_id', 'subject']


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['subscriber_id', 'email', 'first_name']


admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(Campaign, CampaignAdmin)
