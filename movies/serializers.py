from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"
        read_only_fields = ["id", "user"]
        extra_kwargs = {
            "title": {},
            "duration": {},
            "premiere": {},
            "budget": {},
            "default": {"required": True},
        }
