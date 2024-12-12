from django.urls import path
from .views import UserRegistrationView, UserProfileView, AddressListCreateView, AddressDetailView, CustomTokenObtainPairView, CustomTokenRefreshView, CustomTokenVerifyView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='profile'),
    path('addresses/', AddressListCreateView.as_view(), name='address-list-create'),
    path('addresses/<int:pk>/', AddressDetailView.as_view(), name='address-detail'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', CustomTokenVerifyView.as_view(), name='token_verify'),
] 