from rest_framework import serializers
from .models import Review
from users.serializers import ReviewCustomUserSerializer
from .validators import StarsValidator


class ReviewSerializer(serializers.ModelSerializer):
    critic = ReviewCustomUserSerializer(read_only=True)
    movie_id = serializers.UUIDField(source="movie.id", read_only=True)

    class Meta:
        model = Review
        exclude = ["movie"]
        read_only_fields = ["id", "critic"]
        extra_kwargs = {
            "stars": {"validators": [StarsValidator(1, 5)]},
            "spoilers": {"required": False, "default": False},
        }
