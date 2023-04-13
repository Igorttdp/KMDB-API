from django.db import models
from uuid import uuid4


class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    stars = models.IntegerField()
    review = models.TextField()
    spoilers = models.BooleanField(default=False)

    movie = models.ForeignKey(
        "movies.Movie", related_name="reviews", on_delete=models.CASCADE
    )
    critic = models.ForeignKey(
        "users.User", related_name="reviews", on_delete=models.CASCADE
    )
