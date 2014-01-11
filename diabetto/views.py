# -*- coding: utf-8 -*-

from django.views.generic import TemplateView, ListView, DetailView

from diabetto import models

__all__ = (
    'IndexView',
)


class IndexView(TemplateView):
    template_name = 'index.html'


class ProductIndexView(ListView):
    model = models.Product
    context_object_name = 'products'
    template_name = 'index_product.html'


class ProductDetailView(DetailView):
    model = models.Product
    context_object_name = 'product'
    template_name = 'detail_product.html'
