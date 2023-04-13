from django.contrib import admin
from .models import Genre


class CustomGenreAdmin(admin.ModelAdmin):
    list_display = ["name", "id"]


admin.site.register(Genre, CustomGenreAdmin)
