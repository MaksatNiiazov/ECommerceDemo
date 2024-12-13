from django.contrib import admin
from django.urls import path, include
from .views import (UserRegistrationView, UserProfileView, AddressCreateView, AddressUpdateView, AddressDeleteView,
                    LoginView, LogoutView)

urlpatterns = [
    path('api/', include('apps.users.api.urls')),

    path('addresses/create/', AddressCreateView.as_view(), name='address_create'),
    path('addresses/update/<int:pk>/', AddressUpdateView.as_view(), name='address_update'),
    path('addresses/delete/<int:pk>/', AddressDeleteView.as_view(), name='address_delete'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),

]