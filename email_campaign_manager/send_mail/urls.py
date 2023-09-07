from django.urls import path
from .views import email

urlpatterns = [
    path('<int:campaign_id>',
         email, name='email'),
]
