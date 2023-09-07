from django.contrib import admin
from django.urls import path, include
from api import urls as apiUrl
from send_mail import urls as mailUrl

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(apiUrl)),
    path('mail/', include(mailUrl)),
]
