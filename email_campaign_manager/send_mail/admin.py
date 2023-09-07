from django.contrib import admin
from .models import EmailRequest, EmailRequestItem


class EmailRequestAdmin(admin.ModelAdmin):
    list_display = ['email_request_id', 'campaign_id']
    list_filter = ['campaign_id']


class EmailRequestItemAdmin(admin.ModelAdmin):
    list_display = ['email_request_item_id',
                    'email_request_id', 'subscriber_id']
    list_filter = ['email_request_id']


admin.site.register(EmailRequest, EmailRequestAdmin)
admin.site.register(EmailRequestItem, EmailRequestItemAdmin)
