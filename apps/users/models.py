from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

class Address(models.Model):
    user = models.ForeignKey(CustomUser, related_name='addresses', on_delete=models.CASCADE)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}, {self.postal_code}"
