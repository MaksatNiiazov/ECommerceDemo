from django.db import models
from django.utils.translation import gettext_lazy as _
from colorfield.fields import ColorField

from apps.common.models import ImageModel, BasicModel


class Category(BasicModel):
    name = models.CharField(max_length=100, verbose_name=_("Category Name"))
    size_group = models.ForeignKey('SizeGroup', related_name='categories', on_delete=models.CASCADE,
                                   verbose_name=_("Size Group"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class Color(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("Color Name"))
    hex = ColorField(default='#ffffff', verbose_name=_("Color Hex"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Color")
        verbose_name_plural = _("Colors")


class Product(BasicModel):

    name = models.CharField(max_length=100, verbose_name=_("Product Name"))
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE,
                                 verbose_name=_("Category"))
    extra_fields = models.ManyToManyField("ExtraFieldKey", blank=True, verbose_name=_("Extra Fields"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")


class ProductColor(models.Model):
    product = models.ForeignKey(Product, related_name='product_images', on_delete=models.CASCADE,
                                verbose_name=_("Product"))
    color = models.ForeignKey(Color, related_name='product_images', on_delete=models.CASCADE, verbose_name=_("Color"))

    def __str__(self):
        return f"{self.product.name} - {self.color.name}"

    class Meta:
        verbose_name = _("Product Color")
        verbose_name_plural = _("Product Color")


class ProductImage(ImageModel):
    product_color = models.ForeignKey(ProductColor, related_name='images', on_delete=models.CASCADE,
                                      verbose_name=_("Product"))
    image = models.ImageField(upload_to='product_images/', verbose_name=_("Image"))

    def __str__(self):
        return f"{self.product_color.product.name} - {self.product_color.color.name}"

    class Meta:
        verbose_name = _("Product Image")
        verbose_name_plural = _("Product Images")


class ProductVariant(BasicModel):
    product_color = models.ForeignKey(ProductColor, related_name='variants', on_delete=models.CASCADE,
                                      verbose_name=_("Product Color"))
    size = models.ForeignKey('Size', related_name='variants', on_delete=models.CASCADE, verbose_name=_("Size"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Variant Price"))
    stock = models.PositiveIntegerField(default=0, verbose_name=_("Stock"))

    def __str__(self):
        return f"{self.product_color.product.name} - {self.product_color.color.name} - {self.size.name}"

    class Meta:
        verbose_name = _("Product Variant")
        verbose_name_plural = _("Product Variants")


class ExtraFieldKey(models.Model):
    key = models.CharField(max_length=100, verbose_name=_("Field Key"))

    def __str__(self):
        return f"{self.key}"

    class Meta:
        verbose_name = _("Extra Field")
        verbose_name_plural = _("Extra Fields")


class ExtraFieldValue(models.Model):
    key = models.ForeignKey(ExtraFieldKey, related_name='values', on_delete=models.CASCADE, verbose_name=_("Field Key"))
    value = models.CharField(max_length=100, verbose_name=_("Field Value"))

    def __str__(self):
        return f"{self.key}: {self.value} for {self.variant}"

    class Meta:
        verbose_name = _("Extra Field Value")
        verbose_name_plural = _("Extra Field Values")


class SizeGroup(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("Size Group Name"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Size Group")
        verbose_name_plural = _("Size Groups")


class Size(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("Size Name"))
    group = models.ForeignKey(SizeGroup, related_name='sizes', on_delete=models.CASCADE, verbose_name=_("Size Group"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Size")
        verbose_name_plural = _("Sizes")
