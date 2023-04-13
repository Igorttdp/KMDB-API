from django.contrib import admin
from .models import Review


class CustomReviewAdmin(admin.ModelAdmin):
    list_display = ["movie", "stars", "spoilers", "review", "critic", "id"]


admin.site.register(Review, CustomReviewAdmin)
