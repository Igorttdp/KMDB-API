from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsCriticOrAdminOrReadOnly
from .models import Review
from movies.models import Movie
from .serializers import ReviewSerializer


class ReviewView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCriticOrAdminOrReadOnly]

    serializer_class = ReviewSerializer

    def get_queryset(self):
        movie = generics.get_object_or_404(Movie, id=self.kwargs["movie_id"])
        if self.request.method == "GET":
            return Review.objects.filter(movie=movie)

        return Review.objects.all()

    def perform_create(self, serializer):
        movie = generics.get_object_or_404(Movie, id=self.kwargs["movie_id"])
        serializer.save(critic=self.request.user, movie=movie)
