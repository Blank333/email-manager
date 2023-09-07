from django.urls import path
from .views import Subscribers

urlpatterns = [
    path('subscribers/<int:subscriber_id>',
         Subscribers.update_subscriber, name='update_subscriber'),

]
