from users.models import User
from django.core.management.base import BaseCommand, CommandError
from rest_framework.validators import UniqueValidator
import ipdb


class Command(BaseCommand):
    help = "Create a unique admin user"

    def add_arguments(self, parser) -> None:
        parser.add_argument("--username", type=str, default="admin")
        parser.add_argument("--email", type=str)
        parser.add_argument("--password", type=str, default="admin1234")

    def handle(self, *args, **kwargs):
        username: str = kwargs.get("username")
        email: str = kwargs.get("email")
        password: str = kwargs.get("password")

        if email is None:
            email = f"{username}@example.com"

        if username:
            try:
                User.objects.get(username=username)
                raise CommandError(f"Username `{username}` already taken.")
            except User.DoesNotExist:
                ...

        if email:
            try:
                User.objects.get(email=email)
                raise CommandError(f"Email `{email}` already taken.")
            except User.DoesNotExist:
                ...

        User.objects.create_superuser(
            username=username,
            email=email,
            password=password,
        )

        self.stdout.write(
            self.style.SUCCESS(
                "Admin " + f"`{username}`" + " successfully created!"
            )
        )
