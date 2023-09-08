from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Create a superuser for the admin interface'

    def handle(self, *args, **kwargs):
        if User.objects.filter(username='admin').exists():
            return
        User.objects.create_superuser(
            'admin', 'admin@example.com', 'password')
        self.stdout.write(self.style.SUCCESS(
            'Superuser created successfully'))
