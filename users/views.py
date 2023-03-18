# Generic Views
from rest_framework.generics import ListCreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication

# Permissions
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrReadOnly

# Model
from .models import User

# Serializer
from .serializers import UserSerializer


class UserView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    queryset = User.objects.all()
    serializer_class = UserSerializer
