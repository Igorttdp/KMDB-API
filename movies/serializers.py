from rest_framework import serializers
from .validators import MinValueValidator
from .models import Movie
from genres.serializers import GenreSerializer
from genres.models import Genre


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)

    class Meta:
        model = Movie
        exclude = ["user"]
        extra_kwargs = {
            "title": {"required": True},
            "duration": {"required": True},
            "premiere": {"required": True},
            "budget": {"required": True, "validators": [MinValueValidator(0)]},
            "genres": {"required": True},
        }

    def create(self, validated_data):
        genres_list: list = validated_data.pop("genres")

        handled_genres = []

        for genre in genres_list:
            genre_name = genre["name"]
            obj, created = Genre.objects.get_or_create(name=genre_name)
            handled_genres.append(obj)

        movie = Movie.objects.create(**validated_data)
        movie.genres.set(handled_genres)

        return movie
