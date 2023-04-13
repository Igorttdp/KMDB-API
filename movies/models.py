from django.db import models
from uuid import uuid4


class Movie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=127)
    duration = models.DurationField()
    premiere = models.DateField()
    budget = models.DecimalField(max_digits=12, decimal_places=2)
    overview = models.TextField(null=True)

    genres = models.ManyToManyField("genres.Genre", related_name="movies")
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="movies"
    )

    def __str__(self) -> str:
        return f"Movie<{self.title}>"
