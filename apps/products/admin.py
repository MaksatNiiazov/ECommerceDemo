from django.contrib import admin
from django.utils.translation import gettext_lazy as _
import nested_admin
from .models import (
    Category, Color, Product, ProductColor, ProductImage, ProductVariant,
    ExtraFieldKey, ExtraFieldValue, SizeGroup, Size
)
from unfold.admin import ModelAdmin, TabularInline


class ProductImageInline(nested_admin.NestedTabularInline, TabularInline):
    model = ProductImage
    extra = 0


class ProductVariantInline(nested_admin.NestedTabularInline, TabularInline):
    model = ProductVariant
    extra = 0


class ProductColorInline(nested_admin.NestedTabularInline, TabularInline):
    model = ProductColor
    extra = 0
    inlines = [ProductImageInline, ProductVariantInline]


@admin.register(Product)
class ProductAdmin(nested_admin.NestedModelAdmin, ModelAdmin):
    list_display = ['name', 'category', 'created_at', 'updated_at']
    search_fields = ['name', 'category__name']
    list_filter = ['category']
    inlines = [ProductColorInline]


# Category Admin
@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ['name', 'size_group']
    search_fields = ['name']
    list_filter = ['size_group']


# Color Admin
@admin.register(Color)
class ColorAdmin(ModelAdmin):
    list_display = ['name', 'hex']
    search_fields = ['name']


class SizeInline(TabularInline):
    model = Size
    extra = 0

@admin.register(SizeGroup)
class SizeGroupAdmin(ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    inlines = [SizeInline]




class ExtraFieldValueInline(TabularInline):
    model = ExtraFieldValue
    extra = 0

@admin.register(ExtraFieldKey)
class ExtraFieldKeyAdmin(ModelAdmin):
    list_display = ['key']
    search_fields = ['key']
    inlines = [ExtraFieldValueInline]
