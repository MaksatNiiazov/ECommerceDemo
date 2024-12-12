from rest_framework import serializers
from ..models import CustomUser, Address

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'password_confirm']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        if validated_data['password'] != validated_data['password_confirm']:
            raise serializers.ValidationError({"password": "Пароли не совпадают."})

        user = CustomUser(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'street', 'city', 'state', 'postal_code', 'is_primary'] 