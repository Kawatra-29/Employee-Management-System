from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
import os

class Command(BaseCommand):
    help = 'Create superuser and token if not exists'

    def handle(self, *args, **options):
        User = get_user_model()
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'admin')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
        user, created = User.objects.get_or_create(username=username, defaults={'email': email})
        if created:
            user.set_password(password)
            user.is_superuser = True
            user.is_staff = True
            user.save()
            self.stdout.write(self.style.SUCCESS('Superuser created'))
        else:
            self.stdout.write(self.style.WARNING('Superuser already exists'))
        # Token creation
        token, _ = Token.objects.get_or_create(user=user)
        self.stdout.write(self.style.SUCCESS(f'Token for {username}: {token.key}'))