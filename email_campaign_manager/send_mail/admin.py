from django.contrib import admin
from .models import EmailRequest, EmailRequestItem

admin.site.register(EmailRequest)
admin.site.register(EmailRequestItem)
