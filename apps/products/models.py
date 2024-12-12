from django.db import models
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Category Name"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Product Name"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Price"))
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name=_("Category"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

# ... существующий код ...
