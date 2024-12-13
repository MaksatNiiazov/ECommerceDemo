from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'  # Укажите путь к вашему шаблону
    context_object_name = 'products'
    paginate_by = 10  # Укажите количество элементов на странице

    def get_queryset(self):
        # Оптимизация запросов с помощью select_related и prefetch_related
        queryset = Product.objects.select_related(
            'category'  # Связь с Category
        ).prefetch_related(
            'extra_fields',  # Связь с ExtraFieldKey (ManyToManyField)
            'product_images__color',  # Связь с Color через ProductImage
            'product_images__images',  # Связь с изображениями через ProductImage
            'product_images__variants__size',  # Связь с Variant и Size через ProductImage
        )
        return queryset


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_queryset(self):
        # Оптимизация запросов
        return Product.objects.select_related(
            'category'  # ForeignKey к Category
        ).prefetch_related(
            'extra_fields',  # ManyToManyField к ExtraFieldKey
            'product_images__color',  # Связь с Color через ProductImage
            'product_images__variants__size'  # Связь с Variant и Size через ProductImage
        )
