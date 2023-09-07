from django.urls import path
from .views import email

urlpatterns = [
    path('',
         email, name='email'),
]
