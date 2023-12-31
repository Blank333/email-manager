from django.contrib import admin
from django.urls import path, include
from api import urls as apiUrl

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(apiUrl)),
]
