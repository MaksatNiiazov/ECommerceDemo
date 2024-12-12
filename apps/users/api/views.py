from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .serializers import UserRegistrationSerializer, UserProfileSerializer, AddressSerializer
from ..models import CustomUser, Address


class UserRegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer


class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserProfileSerializer


class AddressListCreateView(generics.ListCreateAPIView):
    serializer_class = AddressSerializer

    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)


class AddressDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)


# JWT Views
class CustomTokenObtainPairView(TokenObtainPairView):
    pass


class CustomTokenRefreshView(TokenRefreshView):
    pass


class CustomTokenVerifyView(TokenVerifyView):
    pass
