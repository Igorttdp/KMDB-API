# Generated by Django 4.1 on 2023-03-17 15:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("genres", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(max_length=127)),
                ("duration", models.DurationField()),
                ("premiere", models.DateField()),
                ("budget", models.DecimalField(decimal_places=2, max_digits=12)),
                ("overview", models.TextField(null=True)),
                (
                    "genres",
                    models.ManyToManyField(related_name="movies", to="genres.genre"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="movies",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
