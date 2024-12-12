from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, verbose_name=_("Email Address"))

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        help_text=_('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        verbose_name=_('groups')
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        help_text=_('Specific permissions for this user.'),
        verbose_name=_('user permissions')
    )

    def __str__(self):
        return self.email

class Address(models.Model):
    user = models.ForeignKey(CustomUser, related_name='addresses', on_delete=models.CASCADE, verbose_name=_("User"))
    street = models.CharField(max_length=255, verbose_name=_("Street"))
    city = models.CharField(max_length=100, verbose_name=_("City"))
    state = models.CharField(max_length=100, verbose_name=_("State"))
    postal_code = models.CharField(max_length=20, verbose_name=_("Postal Code"))
    is_primary = models.BooleanField(default=False, verbose_name=_("Is Primary"))

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}, {self.postal_code}"

    class Meta:
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")
