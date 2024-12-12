from django.contrib import admin
from django.urls import path, include
from users.api.views import UserRegistrationView, UserProfileView, AddressListCreateView, AddressDetailView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='profile'),
    path('addresses/', AddressListCreateView.as_view(), name='address-list-create'),
    path('addresses/<int:pk>/', AddressDetailView.as_view(), name='address-detail'),
    path('api/', include('users.api.urls')),
] 