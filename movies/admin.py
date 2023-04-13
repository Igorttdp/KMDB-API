from django.contrib import admin
from .models import Movie


class CustomMoviesAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "duration",
        "premiere",
        "budget",
        "overview",
        "user",
    ]

    ordering = ["title", "duration"]


admin.site.register(Movie, CustomMoviesAdmin)
