from django.contrib import admin
from .models import Subscriber
from .models import Campaign

admin.site.register(Subscriber)
admin.site.register(Campaign)
