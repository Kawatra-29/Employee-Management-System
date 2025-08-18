from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
import os

class Command(BaseCommand):
    help = 'Create token for superuser'

    def handle(self, *args, **options):
        User = get_user_model()
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
        user = User.objects.filter(username=username).first()
        if user:
            token, created = Token.objects.get_or_create(user=user)
            self.stdout.write(self.style.SUCCESS(f'Token for {username}: {token.key}'))
        else:
            self.stdout.write(self.style.ERROR('Superuser not found'))