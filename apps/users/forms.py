from django import forms
from .models import CustomUser, Address

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)  # Поле для подтверждения пароля

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'password_confirm']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Пароли не совпадают.")

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name']

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street', 'city', 'state', 'postal_code', 'is_primary']