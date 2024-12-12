from django.urls import path
from .views import (UserRegistrationView, UserProfileView, AddressListCreateView, AddressDetailView,
                    CustomTokenObtainPairView, CustomTokenRefreshView, CustomTokenVerifyView)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='api_register'),
    path('profile/', UserProfileView.as_view(), name='api_profile'),
    path('addresses/', AddressListCreateView.as_view(), name='api_address-list-create'),
    path('addresses/<int:pk>/', AddressDetailView.as_view(), name='api_address-detail'),
    path('login/', CustomTokenObtainPairView.as_view(), name='api_token_obtain_pair'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='api_token_refresh'),
    path('token/verify/', CustomTokenVerifyView.as_view(), name='api_token_verify'),
] 