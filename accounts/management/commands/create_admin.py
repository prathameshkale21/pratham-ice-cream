import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    Creates (or updates the password of) a superuser from environment
    variables. Safe to run on every deploy — it will not error out if
    the user already exists, unlike Django's built-in createsuperuser
    --noinput.

    Required env vars on Render:
        DJANGO_SUPERUSER_USERNAME
        DJANGO_SUPERUSER_EMAIL
        DJANGO_SUPERUSER_PASSWORD
    """

    help = "Create or update the admin superuser from environment variables."

    def handle(self, *args, **options):

        username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
        email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "")
        password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

        if not username or not password:
            self.stdout.write(
                "DJANGO_SUPERUSER_USERNAME / DJANGO_SUPERUSER_PASSWORD "
                "not set — skipping admin creation."
            )
            return

        User = get_user_model()

        user, created = User.objects.get_or_create(
            username=username,
            defaults={"email": email},
        )

        user.email = email or user.email
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save()

        if created:
            self.stdout.write(self.style.SUCCESS(f"Created admin user '{username}'."))
        else:
            self.stdout.write(self.style.SUCCESS(f"Updated admin user '{username}'."))
