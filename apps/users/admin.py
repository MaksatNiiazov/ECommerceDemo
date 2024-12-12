from django.contrib import admin
from .models import CustomUser, Address

class AddressInline(admin.TabularInline):  # Или используйте StackedInline для другого стиля
    model = Address
    extra = 0

# Регистрация модели CustomUser
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_active', 'is_staff')
    inlines = [AddressInline]

# Регистрация модели Address
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'street', 'city', 'state', 'postal_code', 'is_primary')
    search_fields = ('user__username', 'street', 'city', 'state', 'postal_code')
    list_filter = ('is_primary',)
